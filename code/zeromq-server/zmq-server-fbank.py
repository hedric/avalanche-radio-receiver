#
#
#   Created by Richard Hedlund, richard.hedlund@afconsult.com, oct 2018
#   
#


import time
import zmq
import struct
import numpy as np

context = zmq.Context()
socket = context.socket(zmq.PULL)
socket.connect("tcp://127.0.0.1:5555")

# The power scaling factor is calibrated using a signal generator of known output power
power_scaling_factor = 1

vect_size = 128
vect_ctr = 1

# The number of vectors we want to store in buffer, 30 vectors = 1 second of data.
# We want to store 1 second of data for each filter.
num_of_vect = 30

filter0_buffer = np.zeros(num_of_vect*vect_size, dtype = np.float32)
filter1_buffer = np.zeros(num_of_vect*vect_size, dtype = np.float32)
filter2_buffer = np.zeros(num_of_vect*vect_size, dtype = np.float32)
filter3_buffer = np.zeros(num_of_vect*vect_size, dtype = np.float32)
filter4_buffer = np.zeros(num_of_vect*vect_size, dtype = np.float32)
filter5_buffer = np.zeros(num_of_vect*vect_size, dtype = np.float32)
filter6_buffer = np.zeros(num_of_vect*vect_size, dtype = np.float32)
filter7_buffer = np.zeros(num_of_vect*vect_size, dtype = np.float32)
filter8_buffer = np.zeros(num_of_vect*vect_size, dtype = np.float32)
filter9_buffer = np.zeros(num_of_vect*vect_size, dtype = np.float32)
filter10_buffer = np.zeros(num_of_vect*vect_size, dtype = np.float32)

while True:
    #  Wait for next request from client
    # start = time.time()
   
    # end = time.time()
    # print("Tid: " + str(end - start))
    # #print(str(end - start))
    
    # Receave from GNU Radio client socket.
    message = socket.recv()
    # Convert the binary string data from GNU Radio to numpy array with 32 bit float values
    data = np.fromstring(message, dtype = np.float32)
    data = np.array(data)

    power_threshold_dB = -100

    if vect_ctr <= 30:
        filter0_buffer[vect_size*(vect_ctr-1) : vect_size*vect_ctr-1] = data[0*vect_size:1*vect_size-1]
        filter1_buffer[vect_size*(vect_ctr-1) : vect_size*vect_ctr-1] = data[1*vect_size:2*vect_size-1]
        filter2_buffer[vect_size*(vect_ctr-1) : vect_size*vect_ctr-1] = data[2*vect_size:3*vect_size-1]
        vect_ctr = vect_ctr + 1
        
    if vect_ctr == 30:
        mean_filter0 = np.mean(filter0_buffer, dtype = np.float32)
        mean_filter1 = np.mean(filter1_buffer, dtype = np.float32)
        mean_filter2 = np.mean(filter2_buffer, dtype = np.float32)

        mean_filter0_dB = 10*np.log10(mean_filter0) - 30
        mean_filter1_dB = 10*np.log10(mean_filter1) - 30
        mean_filter2_dB = 10*np.log10(mean_filter2) - 30

        print("Mean value in filter0 = " + str(mean_filter0_dB) + " dB")
        print("Mean value in filter1 = " + str(mean_filter1_dB) + " dB")
        print("Mean value in filter2 = " + str(mean_filter2_dB) + " dB")

        vect_ctr = 1


    # TODO
    # 1.    Implement a good way to close the communication, and add comments to the code.
    # 2.    Implement the communcation if the value max(array) is above some threshold value
    # 3.    Implement the communcation between zmq-server.py and the Odroid XU4 I2C-bus.
    # 4.    Fix and use better names for variables etc, implement functions.
    # 5.    Calibrate power scaling factor

    #  Sleep for one second
    # time.sleep(1)

