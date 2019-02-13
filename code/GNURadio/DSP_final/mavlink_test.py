#!/usr/bin/env python2
#
#   Created by Richard Hedlund, richard.hedlund@protonmail.com
#   Master thesis project in Engineering Physics
#   Uppsala University
#   

# This is a dummy-script created to test the Mavlink protocol using pymavlink.
# Mavlink docs: https://mavlink.io/en/messages/common.html

# The script was tested and verified using a logic analyzer which received the messages once every second.

# Importing necessary libraries
import time
import struct
import numpy as np
from pymavlink import mavutil


# Connection to the UART/Serial bus of the Odroid XU4
# Baud rate set to 115200
the_connection = mavutil.mavlink_connection('/dev/ttySAC0',115200)

dummy_value1 = 1.0
dummy_value2 = 2.0
dummy_value3 = 3.0

while True:
    
    # Intetionally make the program wait for 1 second, before sending another dummy message.
    time.sleep(1)
    time_usec = time.time()
    the_connection.mav.debug_vect_send('Detection', time_usec, dummy_value1 , dummy_value2, dummy_value3)

    

