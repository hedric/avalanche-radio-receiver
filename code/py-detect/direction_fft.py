import numpy as np

# sign_threshold is the sensitivity of the direction finding
# algorithm

# Setting the sensitivity threshold for new sign and angle calculation to one dBm.
sign_threshold = 0.01
sens_threshold = 1.0

def dir(x_sig_str, x_prev, y_sig_str, y_prev, angle):
    #print(str(x_sig_str))
    x_sig_dBm = 10*np.log10(x_sig_str) - 30
    y_sig_dBm = 10*np.log10(y_sig_str) - 30

    if (x_sig_dBm <= -20 and x_sig_dBm > -40) and (y_sig_dBm <= -20 and y_sig_dBm > -40):
        sign_threshold = 1e-2

    elif (x_sig_dBm <= -40 and x_sig_dBm > -60) and (y_sig_dBm <= -40 and y_sig_dBm > -60):
        sign_threshold = 1e-3

    elif (x_sig_dBm <= -60 and x_sig_dBm > -80) and (y_sig_dBm <= -60 and y_sig_dBm > -80):
        sign_threshold = 1e-6
    
    elif (x_sig_dBm <= -80 and x_sig_dBm > -100) and (y_sig_dBm <= -80 and y_sig_dBm > -100):
        sign_threshold = 1e-8
    
    elif x_sig_dBm <= -100  and y_sig_dBm <= -100:
        sign_threshold = 1e-9
    else:
        sign_threshold = 0.01
    
    if np.abs(x_sig_str - x_prev) > sign_threshold and np.abs(y_sig_str - y_prev) > sign_threshold:
        print("sign_threshold:  " + str(sign_threshold))

        # If true we know that direction is in 1st or 4th quadrant
        if x_sig_str > x_prev:
        
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
                
            # If true we know that the direction is in the 2nd quadrant
            if y_sig_str > y_prev:

                #Update sign
                x_dir = -1*np.abs(x_sig_str)
                y_dir = np.abs(y_sig_str)
                
                # If true we know that the direction is in the 3rd quadrant 
            if y_sig_str < y_prev:
                
                #Update sign
                x_dir = -1*np.abs(x_sig_str)
                y_dir = -1*np.abs(y_sig_str)
                
        x_prev = x_sig_str
        y_prev = y_sig_str

        update_angle = np.arctan2(y_dir,x_dir)*360/(2*np.pi)

        return update_angle, x_prev, y_prev
    else:
        return angle, x_prev, y_prev