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
power_threshold_dB = -80

vect_size = 128
# vect_ctr = 1

prev_max_mean = 0.0
meas_ctr = 0


# The number of vectors we want to store in buffer, 30 vectors = 1 second of data.
# We want to store 1 second of data for each filter.
# num_of_vect = 30

filter0_buffer = np.zeros(vect_size, dtype = np.float32)
filter1_buffer = np.zeros(vect_size, dtype = np.float32)
filter2_buffer = np.zeros(vect_size, dtype = np.float32)
filter3_buffer = np.zeros(vect_size, dtype = np.float32)
filter4_buffer = np.zeros(vect_size, dtype = np.float32)
filter5_buffer = np.zeros(vect_size, dtype = np.float32)
filter6_buffer = np.zeros(vect_size, dtype = np.float32)
filter7_buffer = np.zeros(vect_size, dtype = np.float32)
filter8_buffer = np.zeros(vect_size, dtype = np.float32)
filter9_buffer = np.zeros(vect_size, dtype = np.float32)
filter10_buffer = np.zeros(vect_size, dtype = np.float32)

filter_bank_max_mean = np.zeros(11, dtype = np.float32)

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

   

    # Creating a vector containing the maximum value of each vector coming from the moving average filter i GNU Radio
    # The vector will be of length 11 since that is the amounf of band-pass filters we use in the filter bank in GNU Radio.

    # Create a function that takes the whole data vector and separates the data into the respective filter buffers
    # Perhaps put this in an antenna class.

    # Antenna
    # 11 filter buffers
    # filter bank max mean for each filter buffer
    # potential max_mean
    # potential max_index
    # max_mean_dB

    filter0_buffer  = data[0*vect_size:1*vect_size-1]
    filter1_buffer  = data[1*vect_size:2*vect_size-1]
    filter2_buffer  = data[2*vect_size:3*vect_size-1]
    filter3_buffer  = data[3*vect_size:4*vect_size-1]
    filter4_buffer  = data[4*vect_size:5*vect_size-1]
    filter5_buffer  = data[5*vect_size:6*vect_size-1]
    filter6_buffer  = data[6*vect_size:7*vect_size-1]
    filter7_buffer  = data[7*vect_size:8*vect_size-1]
    filter8_buffer  = data[8*vect_size:9*vect_size-1]
    filter9_buffer  = data[9*vect_size:10*vect_size-1]
    filter10_buffer = data[10*vect_size:11*vect_size-1]

    filter_bank_max_mean[0] = max(filter0_buffer)
    filter_bank_max_mean[1] = max(filter1_buffer)
    filter_bank_max_mean[2] = max(filter2_buffer)
    filter_bank_max_mean[3] = max(filter3_buffer)
    filter_bank_max_mean[4] = max(filter4_buffer)
    filter_bank_max_mean[5] = max(filter5_buffer)
    filter_bank_max_mean[6] = max(filter6_buffer)
    filter_bank_max_mean[7] = max(filter7_buffer)
    filter_bank_max_mean[8] = max(filter8_buffer)
    filter_bank_max_mean[9] = max(filter9_buffer)
    filter_bank_max_mean[10] = max(filter10_buffer)

    curr_max_mean    = np.max(filter_bank_max_mean)
    curr_max_index   = np.argmax(filter_bank_max_mean)
    curr_max_mean_dB = 10*np.log10(curr_max_mean) - 30

   # print("Signal detection = " + str(curr_max_mean_dB) + " dB, located in filter " + str (curr_max_index))

    if curr_max_mean > prev_max_mean and curr_max_mean_dB > power_threshold_dB:
        prev_max_mean = curr_max_mean
        prev_max_index = curr_max_index
        prev_max_dB = curr_max_mean_dB
        meas_ctr = meas_ctr + 1
     

    #elif curr_max_mean < prev_max_mean and  meas_ctr > 1 and prev_max_dB > power_threshold_dB:    
    elif curr_max_mean < prev_max_mean and meas_ctr > 1 and prev_max_dB > power_threshold_dB:     
        #print("----- DETECTION -----")
        print("Signal strength: " + str(prev_max_dB) + " dB, located in filter " + str (prev_max_index))
        print("Signal power: "+ str(prev_max_mean))
        #print("Measurement_ctr: " + str(meas_ctr))
        meas_ctr = 0
        prev_max_mean = 0.0
        # prev_max_mean = curr_max_mean
        # Send data over mavlink protocol
        # Use separate threads for each antenna, do parallell computation for each antenna.

    