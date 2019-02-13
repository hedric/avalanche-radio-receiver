#
#   Created by Richard Hedlund, richard.hedlund@afconsult.com, oct 2018
#   

import time
import zmq
import struct
import numpy as np
import threading
import direction_fft

context = zmq.Context()

socket1 = context.socket(zmq.PULL)
socket2 = context.socket(zmq.PULL)

socket1.connect("tcp://127.0.0.1:5555")
socket2.connect("tcp://127.0.0.1:5556")

# the_connection = mavutil.mavlink_connection('/dev/ttySAC0',115200)

power_threshold_dB = -115
calib_factor = 1.044

x_prev = 0.0
y_prev = 0.0

x_dir = 1.0
y_dir = 1.0
angle = 0.0

buffer1 = np.zeros(4, dtype = np.float32)
buffer2 = np.zeros(4, dtype = np.float32)
buff_ctr = 0

buffer_flag = False

while True:
    
    message1 = socket1.recv()
    message2 = socket2.recv()

    arr1 = np.fromstring(message1, dtype = np.float32)
    arr2 = np.fromstring(message2, dtype = np.float32)*calib_factor
    
    arr1_max = max(arr1[1:7]) # 457 kHz +- 90 Hz
    arr2_max = max(arr2[1:7]) # 457 kHz +- 90 Hz

    arr1_max_dB = 10*np.log10(arr1_max) - 30
    arr2_max_dB = 10*np.log10(arr2_max) - 30

    # If signal detected, buffer the 3 next incoming measurements. Because of the pulse width assumed to be approx 100ms.
    # Every frequency bin in the FFT is 30 Hz -> 33.333... ms
    if  arr1_max_dB > power_threshold_dB and arr2_max_dB and buff_ctr <=3 and buffer_flag == False:

       buffer_flag = True
    
    if buffer_flag == True:
        

        if buff_ctr < 4:
            buffer1[buff_ctr] = arr1_max
            buffer2[buff_ctr] = arr2_max
            buff_ctr = buff_ctr + 1

        else:
            x_sig_str = max(buffer1)
            y_sig_str = max(buffer2)

            x_sig_str_dB = 10*np.log10(x_sig_str) -30
            y_sig_str_dB = 10*np.log10(y_sig_str) -30

            print("")
            print("Antenna X signal strength: " + str(x_sig_str_dB) + " dBm")
            print("Antenna Y signal strength: " + str(y_sig_str_dB) + " dBm")
        
            # vector_sum = np.sqrt( np.square(x_sig_str) + np.square(y_sig_str) )
            # vector_sum_dB = 10*np.log10(vector_sum)-30

            # print("Vektorsumma:" + str(vector_sum_dB) + " dBm")
            
            update_angle, update_x_prev, update_y_prev = direction_fft.dir(x_sig_str, x_prev, y_sig_str, y_prev, angle)

            x_prev = update_x_prev
            y_prev = update_y_prev
            angle = update_angle

            print("Angle: " + str(angle))
            
            # output to UART
            # the_connection.mav.debug_vect_send('Detection', time_usec, x_dir, y_dir, angle)

            buff_ctr = 0
            buffer_flag = False