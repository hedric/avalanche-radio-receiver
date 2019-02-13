#
#   Created by Richard Hedlund, richard.hedlund@protonmail.com
#   Master thesis project in Engineering Physics
#   Uppsala University
#   


# Importing necessary libraries
import time
import zmq
import struct
import numpy as np
from pymavlink import mavutil

# Initialization of the ZeroMQ connection with GNU Radio
context = zmq.Context()

socketX = context.socket(zmq.PULL)
socketY = context.socket(zmq.PULL)

socketX.connect("tcp://127.0.0.1:5555")
socketY.connect("tcp://127.0.0.1:5556")

# Connection to the UART/Serial bus of the Odroid XU4
the_connection = mavutil.mavlink_connection('/dev/ttySAC0',115200)

# Power threshold which is tested and measured using a lab bench test.
# power_threshold_dBm will need to be adjusted according to the noise environment of the radio receiver.
power_threshold_dBm = -135

# Calibration factor due to the fact that the SDRs measure slightly different amplitude values
calib_factor = 1.044

while True:

    messageX = socketX.recv()
    messageY = socketY.recv()

    dataX = np.fromstring(messageX, dtype = np.float32)
    dataY = np.fromstring(messageY, dtype = np.float32)*calib_factor
    
    dataXX = np.square(dataX)
    dataYY = np.square(dataY)

    max_X = max(dataXX)
    max_Y = max(dataYY)
    
    X_dBm = 10*np.log10(max_X) - 30
    Y_dBm = 10*np.log10(max_Y) - 30

    if X_dBm > power_threshold_dBm or Y_dBm > power_threshold_dBm:
        
        # Time of detection
        time_usec = time.time()
        print("Max X: " + str(X_dBm) + " dBm")
        print("Max Y: " + str(Y_dBm) + " dBm")

        # Calculate the angle between the X and Y signal strength
        angle = np.arctan2(max_Y,max_X)*360/(2*np.pi)

        # Mavlink protocol output over UART
        the_connection.mav.debug_vect_send('Detection', time_usec, X_dBm, Y_dBm, angle)

    
    
    
