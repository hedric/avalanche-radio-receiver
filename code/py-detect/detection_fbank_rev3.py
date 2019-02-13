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

sign_threshold = 0.01

# Connection to the UART/Serial bus of the Odroid XU4
#the_connection = mavutil.mavlink_connection('/dev/ttySAC0',115200)

while True:

    messageX = socketX.recv()
    messageY = socketY.recv()

    dataX = np.fromstring(messageX, dtype = np.float32)
    dataY = np.fromstring(messageY, dtype = np.float32)

    antennaX.data = np.array(dataX)
    antennaY.data = np.array(dataY)*calib_factor
    

    if antennaX_flag == False:

        if antennaX.detection() == True:
            antennaX_flag = True
            x_sig_str = antennaX.def_max
            x_sig_str_dB = antennaX.def_max_dB
            x_sig_filter = antennaX.def_filter
            x_sig_meas_ctr = antennaX.meas_ctr

    if antennaY_flag == False:
        if antennaY.detection() == True:
            antennaY_flag = True
            y_sig_str = antennaY.def_max
            y_sig_str_dB = antennaY.def_max_dB
            y_sig_filter = antennaY.def_filter
            y_sig_meas_ctr = antennaY.meas_ctr
  
    if antennaX_flag == True and antennaY_flag == True:
     
        angle = np.arctan2(y_sig_str,x_sig_str)*360/(2*np.pi)
        time_usec = time.time()

        # Send this data over UART using debug_vect
        the_connection.mav.debug_vect_send('Detection', time_usec, x_dir, y_dir, angle)

        # Set detection flags to False
        antennaX.meas_ctr = 0
        antennaX.prev_max_mean = 0.0
        antennaX_flag = False

        antennaY.meas_ctr = 0
        antennaY.prev_max_mean = 0.0
        antennaY_flag = False