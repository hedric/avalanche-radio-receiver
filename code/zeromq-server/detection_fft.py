#
#   Created by Richard Hedlund, richard.hedlund@afconsult.com, oct 2018
#   

import time
import zmq
import struct
import numpy as np
import threading

context = zmq.Context()

socket1 = context.socket(zmq.PULL)
socket2 = context.socket(zmq.PULL)

socket1.connect("tcp://127.0.0.1:5555")
socket2.connect("tcp://127.0.0.1:5556")


#the_connection = mavutil.mavlink_connection('/dev/ttySAC0',115200)

power_threshold_dB = -100
calib_factor = 1.044

x_prev = 0.0
y_prev = 0.0

x_dir = 1.0
y_dir = 1.0
angle = 0.0

sign_threshold = 0.01

buffer1 = np.zeros(4, dtype = np.float32)
buffer2 = np.zeros(4, dtype = np.float32)
buff_ctr = 0

while True:
    
    message1 = socket1.recv()
    message2 = socket2.recv()

    arr1 = np.fromstring(message1, dtype = np.float32)
    arr2 = np.fromstring(message2, dtype = np.float32)*calib_factor
    
    #arr1_max = max(arr1[61:67]) # 457 kHz +- 90 Hz
    #arr2_max = max(arr2[61:67]) # 457 kHz +- 90 Hz

    arr1_max = max(arr1[1:7]) # 457 kHz +- 90 Hz
    arr2_max = max(arr2[1:7]) # 457 kHz +- 90 Hz

    arr1_max_dB = 10*np.log10(arr1_max) - 30
    arr2_max_dB = 10*np.log10(arr2_max) - 30

    if buff_ctr == 4:
        x_sig_str = max(buffer1)
        y_sig_str = max(buffer2)
        #print("X: " + str(x_sig_str)) + " Y: " + str(y_sig_str))

        if np.abs(x_sig_str - x_prev) > sign_threshold and np.abs(y_sig_str - y_prev) > sign_threshold:
            print("True")
            print("|x_sig_str - x_prev| = " + str(np.abs(x_sig_str - x_prev)))
            print("|y_sig_str - y_prev| = " + str(np.abs(y_sig_str - y_prev)))
            # If true we know that direction is in 1st or 4th quadrant
            if x_sig_str > x_prev:
                print("x_sig_str > x_prev")
                # If true we know that the direction is on the 1st quadrant
                if y_sig_str > y_prev:
                    # Now make sure the sign of x and y are positive
                    # Update sign
                    x_dir = np.abs(x_sig_str)
                    y_dir = np.abs(y_sig_str)

                # If true we know that the direction is in the 4th quadrant
                elif y_sig_str < y_prev:
                    # Update sign
                    x_dir = np.abs(x_sig_str)
                    y_dir = -1*np.abs(y_sig_str)
                
                x_prev = x_sig_str
                y_prev = y_sig_str

            # If true we know that direction is in 2nd or 3rd quadrant
            if x_sig_str < x_prev:
                print("x_sig_str < x_prev")
                # If true we know that the direction is in the 2nd quadrant
                if y_sig_str > y_prev:
                    x_dir = -1*np.abs(x_sig_str)
                    y_dir = np.abs(y_sig_str)
                # If true we know that the direction is in the 3rd quadrant 
                if y_sig_str < y_prev:
                    x_dir = -1*np.abs(x_sig_str)
                    y_dir = -1*np.abs(y_sig_str)
                
                x_prev = x_sig_str
                y_prev = y_sig_str

        angle = np.arctan2(y_dir,x_dir)*360/(2*np.pi)

        print("Antenna X: " + str(x_dir))
        print("Antenna Y: " + str(y_dir))
        print("Angle: " + str(angle) + " degrees")

        #output to UART
        #the_connection.mav.debug_vect_send('Detection', time_usec, x_dir, y_dir, angle)

        buff_ctr = 0
      


    if  arr1_max_dB > power_threshold_dB or arr1_max_dB > power_threshold_dB:
        buffer1[buff_ctr] = arr1_max
        buffer2[buff_ctr] = arr2_max
        buff_ctr = buff_ctr + 1

    
