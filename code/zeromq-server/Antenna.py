import numpy as np

class Antenna:
    
    power_threshold_dB = -80
    vect_size = 384

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

        power_threshold_dB = -80
        vect_size = 384

        filter0_buffer  = self.data[0*vect_size:1*vect_size-1]
        filter1_buffer  = self.data[1*vect_size:2*vect_size-1]
        filter2_buffer  = self.data[2*vect_size:3*vect_size-1]
        filter3_buffer  = self.data[3*vect_size:4*vect_size-1]
        filter4_buffer  = self.data[4*vect_size:5*vect_size-1]
        filter5_buffer  = self.data[5*vect_size:6*vect_size-1]
        filter6_buffer  = self.data[6*vect_size:7*vect_size-1]
        filter7_buffer  = self.data[7*vect_size:8*vect_size-1]
        filter8_buffer  = self.data[8*vect_size:9*vect_size-1]
        filter9_buffer  = self.data[9*vect_size:10*vect_size-1]
        filter10_buffer = self.data[10*vect_size:11*vect_size-1]

        filter_bank_max_mean = np.zeros(11, dtype = np.float32)

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

        #prev_max_mean = self.prev_max_mean
        

        self.curr_max_mean    = max(filter_bank_max_mean)
        self.curr_max_index   = np.argmax(filter_bank_max_mean)
        self.curr_max_mean_dB = 10*np.log10(self.curr_max_mean) - 30

        if self.curr_max_mean > self.prev_max_mean and self.curr_max_mean_dB > power_threshold_dB:
            self.prev_max_mean = self.curr_max_mean
            self.prev_max_index = self.curr_max_index
            self.prev_max_mean_dB = self.curr_max_mean_dB
            self.meas_ctr = self.meas_ctr + 1
            #self.prev_max_mean = self.prev_max_mean
            return False

        #elif curr_max_mean < prev_max_mean and  meas_ctr > 1 and prev_max_dB > power_threshold_dB:    
        if self.curr_max_mean < self.prev_max_mean and self.prev_max_mean_dB > power_threshold_dB:
            if self.max_ctr <= 2:
                self.max_str_buffer[self.max_ctr] = self.prev_max_mean
                self.max_ind_buffer[self.max_ctr] = self.prev_max_index
                self.max_ctr = self.max_ctr + 1
                
                return False
            else:
                self.max_ctr = 0
                self.def_max = max(self.max_str_buffer)
                self.def_max_dB = 10*np.log10(self.def_max) - 30
                self.def_filter = max(self.max_ind_buffer)
                return True
        #elif self.curr_max_mean < self.prev_max_mean and self.prev_max_mean_dB > power_threshold_dB:   
            #print("----- DETECTION -----")
            #print("Signal strength: " + str(prev_max_dB) + " dB, located in filter " + str (prev_max_index))
            #print("Signal power: "+ str(prev_max_mean))
            #self.curr_max_mean = self.prev_max_mean
            #self.curr_max_mean_dB = self.prev_max_mean_dB
            #self.curr_max_index = self.prev_max_index
            #print("Measurement_ctr: " + str(meas_ctr))
            #self.meas_ctr = 0
            #self.prev_max_mean = 0.0
            