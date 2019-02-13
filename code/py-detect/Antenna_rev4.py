import numpy as np

class Antenna:
    
    power_threshold_dB = -120
    vect_size = 1

    # Define what an Antenna is in the initialization function
    def __init__(self, 
                data, 
                curr_max_mean,
                curr_max_mean_dB,
                curr_max_index,
                prev_max_mean,
                prev_max_index,
                meas_ctr,
                max_str_buffer,
                max_ind_buffer,
                max_ctr,
                def_max,
                def_max_dB,
                def_filter
                ):



        self.data               = data
        self.curr_max_mean      = curr_max_mean
        self.curr_max_mean_dB   = curr_max_mean_dB
        self.curr_max_index     = curr_max_index
        
        self.prev_max_mean      = prev_max_mean
        self.prev_max_index     = prev_max_index
        
        self.meas_ctr           = meas_ctr 
        self.max_str_buffer     = max_str_buffer
        self.max_ind_buffer     = max_ind_buffer
        self.max_ctr            = max_ctr

        self.def_max            = def_max
        self.def_max_dB         = def_max_dB
        self.def_filter         = def_filter

    def detection(self):

        power_threshold_dB = -120

        filter_bank_mean = np.zeros(11, dtype = np.float32)

        filter_bank_mean[0] = self.data[0]
        filter_bank_mean[1] = self.data[1]
        filter_bank_mean[2] = self.data[2]
        filter_bank_mean[3] = self.data[3]
        filter_bank_mean[4] = self.data[4]
        filter_bank_mean[5] = self.data[5]
        filter_bank_mean[6] = self.data[6]
        filter_bank_mean[7] = self.data[7]
        filter_bank_mean[8] = self.data[8]
        filter_bank_mean[9] = self.data[9]
        filter_bank_mean[10] = self.data[10]
    

        self.curr_max_mean    = max(filter_bank_mean)
        self.curr_max_index   = np.argmax(filter_bank_mean)
        self.curr_max_mean_dB = 10*np.log10(self.curr_max_mean)-30

        if self.curr_max_mean > self.prev_max_mean and self.curr_max_mean_dB > power_threshold_dB:
            self.prev_max_mean = self.curr_max_mean
            self.prev_max_index = self.curr_max_index
            self.prev_max_mean_dB = self.curr_max_mean_dB
            self.meas_ctr = self.meas_ctr + 1
        
            return False

         
        if self.curr_max_mean < self.prev_max_mean and self.prev_max_mean_dB > power_threshold_dB:
            
            if self.max_ctr <= 2:
                self.max_str_buffer[self.max_ctr] = self.prev_max_mean
                self.max_ind_buffer[self.max_ctr] = self.prev_max_index
                self.max_ctr = self.max_ctr + 1
                
                return False
            else:
                self.max_ctr = 0
                self.def_max = max(self.max_str_buffer)
                self.def_max_dB = 10*np.log10(self.def_max)-30
                self.def_filter = max(self.max_ind_buffer)
                return True
