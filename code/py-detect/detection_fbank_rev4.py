#
#
#   Created by Richard Hedlund, richard.hedlund@afconsult.com, oct 2018
#   
#

import time
import zmq
import struct
import numpy as np
from pymavlink import mavutil

from Antenna_rev4 import Antenna

context = zmq.Context()

socketX = context.socket(zmq.PULL)
socketY = context.socket(zmq.PULL)

socketX.connect("tcp://127.0.0.1:5555")
socketY.connect("tcp://127.0.0.1:5556")

vect_size = 1

antennaX = Antenna(np.zeros(11*vect_size, dtype = np.float32),0.0,0.0,0,0.0,0,0, np.zeros(3, dtype = np.float32), [0]*3, 0, 0.0, 0.0, 0)
antennaY = Antenna(np.zeros(11*vect_size, dtype = np.float32),0.0,0.0,0,0.0,0,0, np.zeros(3, dtype = np.float32), [0]*3, 0, 0.0, 0.0, 0)

antennaX_flag = False
antennaY_flag = False

calib_factor = 1.044

x_prev = 0.0
y_prev = 0.0

x_dir = 1.0
y_dir = 1.0
angle = 0.0

sign_threshold = 0.01

# Connection to the UART/Serial bus of the Odroid XU4
# the_connection = mavutil.mavlink_connection('/dev/ttySAC0',115200)

while True:

    messageX = socketX.recv()
    messageY = socketY.recv()

    dataX = np.fromstring(messageX, dtype = np.float32)
    dataY = np.fromstring(messageY, dtype = np.float32)

    #antennaX.data = np.array(dataX)
    #antennaY.data = np.array(dataY)*calib_factor

    max_X = max(dataX)
    max_Y = max(dataY)

    max_X = 10*np.log10(max_X) - 30
    max_Y = 10*np.log10(max_Y) - 30

    if max_X > -130:
        print("Max X: " + str(max_X) + " dBm")
    
    if max_Y > -130:
        print("Max Y: " + str(max_Y) + " dBm")

    
    