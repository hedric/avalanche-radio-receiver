import numpy as np
from gnuradio import filter
from gnuradio.filter import firdes

samp_rate = 768000
decimation = 200
decim_total = samp_rate/decimation

samp_rate_decimated = samp_rate/decimation
transition_bw = samp_rate_decimated/4
cutoff = samp_rate_decimated*0.5


transition_bw_fbank = 40
cutoff_fbank        = 10


taps1 = firdes.low_pass(1, samp_rate, samp_rate_decimated*0.5,transition_bw, firdes.WIN_RECTANGULAR, 6.76)

taps2 = firdes.low_pass_2(1, samp_rate, samp_rate_decimated*0.5, 70,transition_bw, firdes.WIN_HAMMING, 6.76) 

taps_filter_bank = firdes.low_pass(1, samp_rate_decimated, cutoff_fbank,transition_bw_fbank, firdes.WIN_RECTANGULAR, 6.76)

taps_bp = firdes.complex_band_pass(1, samp_rate/decim_total, -20, 20, 10, firdes.WIN_HAMMING, 6.76)

tasp_lowpass = firdes.low_pass(1, samp_rate_decimated, cutoff_fbank, transition_bw_fbank, firdes.WIN_HAMMING, 6.76)


print("Transition BW = " + str(transition_bw))
print("Cut-off frequency = " + str(cutoff))
print("Number of taps lowpass1  = " +str(len(taps1))) 
print("Number of taps lowpass2  = " +str(len(taps2))) 
print("Number of taps filter bank  = " +str(len(taps_bp))) 

print("LOWPASS-TASP: " + str(len(tasp_lowpass)))