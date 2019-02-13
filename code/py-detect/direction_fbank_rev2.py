import numpy as np

# sign_threshold is the sensitivity of the direction finding
# algorithm

# Setting the sensitivity threshold for new sign and angle calculation to one dBm.
sign_threshold = 0.01
sens_threshold = 1.0

def dir(x_sig_str, y_sig_str,x_prev, y_prev , angle):
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

        update_angle = np.arctan2(y_sig_str,x_sig_str)*360/(2*np.pi)
        return x_prev,y_prev,update_angle
    else:

        x_prev = x_sig_str
        y_prev = y_sig_str
        return x_prev,y_prev,angle