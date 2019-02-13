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

previous_measurement = 0.0
meas_ctr = 0

pot_max_mean = np.zeros(3, dtype = np.float32)
pot_max_mean_dB = np.zeros(3, dtype = np.float32)
pot_max_index = np.zeros(3, dtype = np.int8)



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


    potential_max_mean    = np.max(filter_bank_max_mean)
    potential_max_index   = np.argmax(filter_bank_max_mean)
    potential_max_mean_dB = 10*np.log10(potential_max_mean) - 30

    
    
    if potential_max_mean > previous_measurement 
        #print("Potential detection = " + str(potential_max_mean_dB) + " dB, located in filter " + str (potential_max_index))
        previous_measurement = potential_max_mean
        previous_measurement_dB = potential_max_mean_dB
        previous_measurement_filter_index = potential_max_index

    elif potential_max_mean < previous_measurement and  previous_measurement_dB >= power_threshold_dB:
        #print("Signal detection = " + str(previous_measurement_dB) + " dB, located in filter " + str (previous_measurement_filter_index))
        
        pot_max_mean[meas_ctr] = previous_measurement
        pot_max_index[meas_ctr] = previous_measurement_filter_index
        pot_max_mean_dB[meas_ctr] = previous_measurement_dB

        meas_ctr = meas_ctr + 1;
        
        previous_measurement = 0.0
        previous_measurement_dB = -300
        potential_max_mean = 0.0

    if meas_ctr == 2:
        final_index = np.argmax(pot_max_mean)
        final_max_mean = pot_max_mean[final_index]
        final_max_mean_dB = pot_max_mean_dB[final_index]
        print("Signal detection = " + str(final_max_mean_dB) + " dB, located in filter " + str (pot_max_index[final_index]))
        meas_ctr = 0
            
    #np.max()
    #max()

    # TODO
    # 1.    Implement a good way to close the communication, and add comments to the code.
    # 2.    Implement the communcation if the value max(array) is above some threshold value
    # 3.    Implement the communcation between zmq-server.py and the Odroid XU4 I2C-bus.
    # 4.    Fix and use better names for variables etc, implement functions.
    # 5.    Calibrate power scaling factor

    #  Sleep for one second
    # time.sleep(1)