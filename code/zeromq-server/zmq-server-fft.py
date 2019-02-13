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


while True:
    #  Wait for next request from client
    start = time.time()
    message = socket.recv()
    end = time.time()
    # print("Tid: " + str(end - start))


    #print(str(end - start))
    #  Convert the binary string data from GNU Radio to numpy array with 32 bit float values
    # array = np.fromstring(message, dtype = np.float32)
    array = np.fromstring(message, dtype = np.float32)
    

    
    #data    = 0.01*array
    #data_dB = 10*np.log10(data) 
    #max_data_dB = max(array)
    #   end = time.time()
    #  Print the maximum value of the array
    #if max_data_dB >= -30.0:
    #    print(str(time.time() - 1539006500) + ": " + str(max_data_dB))
    #print("Max value in filter1 = " + str(max(array)) + " dB")
    #  Print the length of the array as a sanity check
    # print(str(len(array)))


    # TODO
    # 1.    Implement a good way to close the communication, and add comments to the code.
    # 2.    Implement the communcation if the value max(array) is above some threshold value
    # 3.    Implement the communcation between zmq-server.py and the Odroid XU4 I2C-bus.
    # 4.    Fix and use better names for variables etc, implement functions.

    #  Sleep for one second
    # time.sleep(1)

