#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Mov Avg
# Generated: Mon Nov 19 13:19:26 2018
##################################################


if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import zeromq
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import osmosdr
import time
import wx


class mov_avg(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Mov Avg")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 768000
        self.decim_total = decim_total = 200
        self.samp_rate_decimated = samp_rate_decimated = samp_rate/decim_total
        self.vect_size = vect_size = 384
        self.transition_bw_fbank = transition_bw_fbank = 5
        self.transition_bw = transition_bw = samp_rate_decimated/4
        self.cutoff_fbank = cutoff_fbank = 5
        self.center_freq = center_freq = 457e3

        ##################################################
        # Blocks
        ##################################################
        self.zeromq_push_sink_0_0 = zeromq.push_sink(gr.sizeof_float, 11*vect_size, "tcp://127.0.0.1:5556", 100, False, -1)
        self.zeromq_push_sink_0 = zeromq.push_sink(gr.sizeof_float, 11*vect_size, "tcp://127.0.0.1:5555", 100, False, -1)
        self.freq_xlating_fir_filter_DEC_LP_0 = filter.freq_xlating_fir_filter_ccf(decim_total, (firdes.low_pass(1, samp_rate, samp_rate_decimated*0.5,transition_bw, firdes.WIN_HAMMING, 6.76)), 0, samp_rate)
        self.freq_xlating_fir_filter_DEC_LP = filter.freq_xlating_fir_filter_ccf(decim_total, (firdes.low_pass(1, samp_rate, samp_rate_decimated*0.5,transition_bw, firdes.WIN_HAMMING, 6.76)), 0, samp_rate)
        self.blocks_stream_to_vector_1_0_0_0 = blocks.stream_to_vector(gr.sizeof_float*1, 11*vect_size)
        self.blocks_stream_to_vector_1_0_0 = blocks.stream_to_vector(gr.sizeof_float*1, 11*vect_size)
        self.blocks_stream_mux_0_0 = blocks.stream_mux(gr.sizeof_gr_complex*1, (vect_size,vect_size,vect_size,vect_size,vect_size,vect_size,vect_size,vect_size,vect_size,vect_size,vect_size))
        self.blocks_stream_mux_0 = blocks.stream_mux(gr.sizeof_gr_complex*1, (vect_size,vect_size,vect_size,vect_size,vect_size,vect_size,vect_size,vect_size,vect_size,vect_size,vect_size))
        self.blocks_multiply_const_xx_0_0_0_0 = blocks.multiply_const_ff(1e-2)
        self.blocks_multiply_const_xx_0_0_0 = blocks.multiply_const_ff(1e-3)
        self.blocks_moving_average_xx_0_3 = blocks.moving_average_cc(384, 1, 4000)
        self.blocks_moving_average_xx_0_2_2 = blocks.moving_average_cc(vect_size, 1, 4000)
        self.blocks_moving_average_xx_0_2_1_1 = blocks.moving_average_cc(vect_size, 1, 4000)
        self.blocks_moving_average_xx_0_2_1_0_3 = blocks.moving_average_cc(vect_size, 1, 4000)
        self.blocks_moving_average_xx_0_2_1_0_2_1 = blocks.moving_average_cc(vect_size, 1, 4000)
        self.blocks_moving_average_xx_0_2_1_0_2_0_0 = blocks.moving_average_cc(vect_size, 1, 4000)
        self.blocks_moving_average_xx_0_2_1_0_2_0 = blocks.moving_average_cc(vect_size, 1, 4000)
        self.blocks_moving_average_xx_0_2_1_0_2 = blocks.moving_average_cc(vect_size, 1, 4000)
        self.blocks_moving_average_xx_0_2_1_0_1_0 = blocks.moving_average_cc(vect_size, 1, 4000)
        self.blocks_moving_average_xx_0_2_1_0_1 = blocks.moving_average_cc(vect_size, 1, 4000)
        self.blocks_moving_average_xx_0_2_1_0_0_0 = blocks.moving_average_cc(vect_size, 1, 4000)
        self.blocks_moving_average_xx_0_2_1_0_0 = blocks.moving_average_cc(vect_size, 1, 4000)
        self.blocks_moving_average_xx_0_2_1_0 = blocks.moving_average_cc(vect_size, 1, 4000)
        self.blocks_moving_average_xx_0_2_1 = blocks.moving_average_cc(vect_size, 1, 4000)
        self.blocks_moving_average_xx_0_2_0_0 = blocks.moving_average_cc(vect_size, 1, 4000)
        self.blocks_moving_average_xx_0_2_0 = blocks.moving_average_cc(vect_size, 1, 4000)
        self.blocks_moving_average_xx_0_2 = blocks.moving_average_cc(vect_size, 1, 4000)
        self.blocks_moving_average_xx_0_1_0 = blocks.moving_average_cc(vect_size, 1, 4000)
        self.blocks_moving_average_xx_0_1 = blocks.moving_average_cc(vect_size, 1, 4000)
        self.blocks_moving_average_xx_0_0_0 = blocks.moving_average_cc(384, 1, 4000)
        self.blocks_moving_average_xx_0_0 = blocks.moving_average_cc(384, 1, 4000)
        self.blocks_moving_average_xx_0 = blocks.moving_average_cc(384, 1, 4000)
        self.blocks_complex_to_mag_squared_0_2_0 = blocks.complex_to_mag_squared(1)
        self.blocks_complex_to_mag_squared_0_2 = blocks.complex_to_mag_squared(1)
        self.band_pass_filter_0_1 = filter.fir_filter_ccc(1, firdes.complex_band_pass(
        	1, samp_rate/decim_total, -20, 20, 10, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_2 = filter.fir_filter_ccc(1, firdes.complex_band_pass(
        	1, samp_rate/decim_total, -40, 0, 10, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_1_1 = filter.fir_filter_ccc(1, firdes.complex_band_pass(
        	1, samp_rate/decim_total, 0, 40, 10, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_1_0_1 = filter.fir_filter_ccc(1, firdes.complex_band_pass(
        	1, samp_rate/decim_total, 20, 60, 10, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_1_0_0_1 = filter.fir_filter_ccc(1, firdes.complex_band_pass(
        	1, samp_rate/decim_total, 40, 80, 10, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_1_0_0_0_1 = filter.fir_filter_ccc(1, firdes.complex_band_pass(
        	1, samp_rate/decim_total, 60, 100, 10, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_1_0_0_0_0_0 = filter.fir_filter_ccc(1, firdes.complex_band_pass(
        	1, samp_rate/decim_total, 80, 120, 10, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_1_0_0_0_0 = filter.fir_filter_ccc(1, firdes.complex_band_pass(
        	1, samp_rate/decim_total, 80, 120, 10, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_1_0_0_0 = filter.fir_filter_ccc(1, firdes.complex_band_pass(
        	1, samp_rate/decim_total, 60, 100, 10, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_1_0_0 = filter.fir_filter_ccc(1, firdes.complex_band_pass(
        	1, samp_rate/decim_total, 40, 80, 10, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_1_0 = filter.fir_filter_ccc(1, firdes.complex_band_pass(
        	1, samp_rate/decim_total, 20, 60, 10, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_1 = filter.fir_filter_ccc(1, firdes.complex_band_pass(
        	1, samp_rate/decim_total, 0, 40, 10, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_1 = filter.fir_filter_ccc(1, firdes.complex_band_pass(
        	1, samp_rate/decim_total, -60, -20, 10, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0_1 = filter.fir_filter_ccc(1, firdes.complex_band_pass(
        	1, samp_rate/decim_total, -80, -40, 10, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0_0_1 = filter.fir_filter_ccc(1, firdes.complex_band_pass(
        	1, samp_rate/decim_total, -100, -60, 10, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0_0_0_0 = filter.fir_filter_ccc(1, firdes.complex_band_pass(
        	1, samp_rate/decim_total, -120, -80, 10, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0_0_0 = filter.fir_filter_ccc(1, firdes.complex_band_pass(
        	1, samp_rate/decim_total, -120, -80, 10, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0_0 = filter.fir_filter_ccc(1, firdes.complex_band_pass(
        	1, samp_rate/decim_total, -100, -60, 10, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0 = filter.fir_filter_ccc(1, firdes.complex_band_pass(
        	1, samp_rate/decim_total, -80, -40, 10, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0 = filter.fir_filter_ccc(1, firdes.complex_band_pass(
        	1, samp_rate/decim_total, -60, -20, 10, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0 = filter.fir_filter_ccc(1, firdes.complex_band_pass(
        	1, samp_rate/decim_total, -40, 0, 10, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0 = filter.fir_filter_ccc(1, firdes.complex_band_pass(
        	1, samp_rate/decim_total, -20, 20, 10, firdes.WIN_HAMMING, 6.76))
        self.airspyhf_source_0_0 = osmosdr.source( args="numchan=" + str(1) + " " + 'C852D65D9DBF34DD' )
        self.airspyhf_source_0_0.set_sample_rate(samp_rate)
        self.airspyhf_source_0_0.set_center_freq(457000, 0)
        self.airspyhf_source_0_0.set_freq_corr(0, 0)
        self.airspyhf_source_0_0.set_iq_balance_mode(0, 0)
        self.airspyhf_source_0_0.set_gain_mode(False, 0)
        self.airspyhf_source_0_0.set_gain(6, "LNA", 0)
        self.airspyhf_source_0_0.set_gain(0, "ATT", 0)

        self.airspyhf_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + 'C852A98040343FD2' )
        self.airspyhf_source_0.set_sample_rate(samp_rate)
        self.airspyhf_source_0.set_center_freq(457000, 0)
        self.airspyhf_source_0.set_freq_corr(0, 0)
        self.airspyhf_source_0.set_iq_balance_mode(0, 0)
        self.airspyhf_source_0.set_gain_mode(False, 0)
        self.airspyhf_source_0.set_gain(6, "LNA", 0)
        self.airspyhf_source_0.set_gain(0, "ATT", 0)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.airspyhf_source_0, 0), (self.freq_xlating_fir_filter_DEC_LP, 0))
        self.connect((self.airspyhf_source_0_0, 0), (self.freq_xlating_fir_filter_DEC_LP_0, 0))
        self.connect((self.band_pass_filter_0, 0), (self.blocks_moving_average_xx_0_2_1, 0))
        self.connect((self.band_pass_filter_0_0, 0), (self.blocks_moving_average_xx_0_2_1_0, 0))
        self.connect((self.band_pass_filter_0_0_0, 0), (self.blocks_moving_average_xx_0_2_1_0_0, 0))
        self.connect((self.band_pass_filter_0_0_0_0, 0), (self.blocks_moving_average_xx_0_2_1_0_1, 0))
        self.connect((self.band_pass_filter_0_0_0_0_0, 0), (self.blocks_moving_average_xx_0_2_1_0_2, 0))
        self.connect((self.band_pass_filter_0_0_0_0_0_0, 0), (self.blocks_moving_average_xx_0_2_1_0_2_0, 0))
        self.connect((self.band_pass_filter_0_0_0_0_0_0_0, 0), (self.blocks_moving_average_xx_0_2_1_0_2_0_0, 0))
        self.connect((self.band_pass_filter_0_0_0_0_0_1, 0), (self.blocks_moving_average_xx_0_2_1_0_2_1, 0))
        self.connect((self.band_pass_filter_0_0_0_0_1, 0), (self.blocks_moving_average_xx_0_2_1_0_1_0, 0))
        self.connect((self.band_pass_filter_0_0_0_1, 0), (self.blocks_moving_average_xx_0_2_1_0_0_0, 0))
        self.connect((self.band_pass_filter_0_0_1, 0), (self.blocks_moving_average_xx_0_2_0, 0))
        self.connect((self.band_pass_filter_0_0_1_0, 0), (self.blocks_moving_average_xx_0_2, 0))
        self.connect((self.band_pass_filter_0_0_1_0_0, 0), (self.blocks_moving_average_xx_0_1, 0))
        self.connect((self.band_pass_filter_0_0_1_0_0_0, 0), (self.blocks_moving_average_xx_0_0, 0))
        self.connect((self.band_pass_filter_0_0_1_0_0_0_0, 0), (self.blocks_moving_average_xx_0, 0))
        self.connect((self.band_pass_filter_0_0_1_0_0_0_0_0, 0), (self.blocks_moving_average_xx_0_3, 0))
        self.connect((self.band_pass_filter_0_0_1_0_0_0_1, 0), (self.blocks_moving_average_xx_0_0_0, 0))
        self.connect((self.band_pass_filter_0_0_1_0_0_1, 0), (self.blocks_moving_average_xx_0_1_0, 0))
        self.connect((self.band_pass_filter_0_0_1_0_1, 0), (self.blocks_moving_average_xx_0_2_2, 0))
        self.connect((self.band_pass_filter_0_0_1_1, 0), (self.blocks_moving_average_xx_0_2_0_0, 0))
        self.connect((self.band_pass_filter_0_0_2, 0), (self.blocks_moving_average_xx_0_2_1_0_3, 0))
        self.connect((self.band_pass_filter_0_1, 0), (self.blocks_moving_average_xx_0_2_1_1, 0))
        self.connect((self.blocks_complex_to_mag_squared_0_2, 0), (self.blocks_multiply_const_xx_0_0_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_0_2_0, 0), (self.blocks_multiply_const_xx_0_0_0_0, 0))
        self.connect((self.blocks_moving_average_xx_0, 0), (self.blocks_stream_mux_0, 10))
        self.connect((self.blocks_moving_average_xx_0_0, 0), (self.blocks_stream_mux_0, 9))
        self.connect((self.blocks_moving_average_xx_0_0_0, 0), (self.blocks_stream_mux_0_0, 9))
        self.connect((self.blocks_moving_average_xx_0_1, 0), (self.blocks_stream_mux_0, 8))
        self.connect((self.blocks_moving_average_xx_0_1_0, 0), (self.blocks_stream_mux_0_0, 8))
        self.connect((self.blocks_moving_average_xx_0_2, 0), (self.blocks_stream_mux_0, 7))
        self.connect((self.blocks_moving_average_xx_0_2_0, 0), (self.blocks_stream_mux_0, 6))
        self.connect((self.blocks_moving_average_xx_0_2_0_0, 0), (self.blocks_stream_mux_0_0, 6))
        self.connect((self.blocks_moving_average_xx_0_2_1, 0), (self.blocks_stream_mux_0, 5))
        self.connect((self.blocks_moving_average_xx_0_2_1_0, 0), (self.blocks_stream_mux_0, 4))
        self.connect((self.blocks_moving_average_xx_0_2_1_0_0, 0), (self.blocks_stream_mux_0, 3))
        self.connect((self.blocks_moving_average_xx_0_2_1_0_0_0, 0), (self.blocks_stream_mux_0_0, 3))
        self.connect((self.blocks_moving_average_xx_0_2_1_0_1, 0), (self.blocks_stream_mux_0, 2))
        self.connect((self.blocks_moving_average_xx_0_2_1_0_1_0, 0), (self.blocks_stream_mux_0_0, 2))
        self.connect((self.blocks_moving_average_xx_0_2_1_0_2, 0), (self.blocks_stream_mux_0, 1))
        self.connect((self.blocks_moving_average_xx_0_2_1_0_2_0, 0), (self.blocks_stream_mux_0, 0))
        self.connect((self.blocks_moving_average_xx_0_2_1_0_2_0_0, 0), (self.blocks_stream_mux_0_0, 0))
        self.connect((self.blocks_moving_average_xx_0_2_1_0_2_1, 0), (self.blocks_stream_mux_0_0, 1))
        self.connect((self.blocks_moving_average_xx_0_2_1_0_3, 0), (self.blocks_stream_mux_0_0, 4))
        self.connect((self.blocks_moving_average_xx_0_2_1_1, 0), (self.blocks_stream_mux_0_0, 5))
        self.connect((self.blocks_moving_average_xx_0_2_2, 0), (self.blocks_stream_mux_0_0, 7))
        self.connect((self.blocks_moving_average_xx_0_3, 0), (self.blocks_stream_mux_0_0, 10))
        self.connect((self.blocks_multiply_const_xx_0_0_0, 0), (self.blocks_stream_to_vector_1_0_0, 0))
        self.connect((self.blocks_multiply_const_xx_0_0_0_0, 0), (self.blocks_stream_to_vector_1_0_0_0, 0))
        self.connect((self.blocks_stream_mux_0, 0), (self.blocks_complex_to_mag_squared_0_2, 0))
        self.connect((self.blocks_stream_mux_0_0, 0), (self.blocks_complex_to_mag_squared_0_2_0, 0))
        self.connect((self.blocks_stream_to_vector_1_0_0, 0), (self.zeromq_push_sink_0, 0))
        self.connect((self.blocks_stream_to_vector_1_0_0_0, 0), (self.zeromq_push_sink_0_0, 0))
        self.connect((self.freq_xlating_fir_filter_DEC_LP, 0), (self.band_pass_filter_0, 0))
        self.connect((self.freq_xlating_fir_filter_DEC_LP, 0), (self.band_pass_filter_0_0, 0))
        self.connect((self.freq_xlating_fir_filter_DEC_LP, 0), (self.band_pass_filter_0_0_0, 0))
        self.connect((self.freq_xlating_fir_filter_DEC_LP, 0), (self.band_pass_filter_0_0_0_0, 0))
        self.connect((self.freq_xlating_fir_filter_DEC_LP, 0), (self.band_pass_filter_0_0_0_0_0, 0))
        self.connect((self.freq_xlating_fir_filter_DEC_LP, 0), (self.band_pass_filter_0_0_0_0_0_0, 0))
        self.connect((self.freq_xlating_fir_filter_DEC_LP, 0), (self.band_pass_filter_0_0_1, 0))
        self.connect((self.freq_xlating_fir_filter_DEC_LP, 0), (self.band_pass_filter_0_0_1_0, 0))
        self.connect((self.freq_xlating_fir_filter_DEC_LP, 0), (self.band_pass_filter_0_0_1_0_0, 0))
        self.connect((self.freq_xlating_fir_filter_DEC_LP, 0), (self.band_pass_filter_0_0_1_0_0_0, 0))
        self.connect((self.freq_xlating_fir_filter_DEC_LP, 0), (self.band_pass_filter_0_0_1_0_0_0_0, 0))
        self.connect((self.freq_xlating_fir_filter_DEC_LP_0, 0), (self.band_pass_filter_0_0_0_0_0_0_0, 0))
        self.connect((self.freq_xlating_fir_filter_DEC_LP_0, 0), (self.band_pass_filter_0_0_0_0_0_1, 0))
        self.connect((self.freq_xlating_fir_filter_DEC_LP_0, 0), (self.band_pass_filter_0_0_0_0_1, 0))
        self.connect((self.freq_xlating_fir_filter_DEC_LP_0, 0), (self.band_pass_filter_0_0_0_1, 0))
        self.connect((self.freq_xlating_fir_filter_DEC_LP_0, 0), (self.band_pass_filter_0_0_1_0_0_0_0_0, 0))
        self.connect((self.freq_xlating_fir_filter_DEC_LP_0, 0), (self.band_pass_filter_0_0_1_0_0_0_1, 0))
        self.connect((self.freq_xlating_fir_filter_DEC_LP_0, 0), (self.band_pass_filter_0_0_1_0_0_1, 0))
        self.connect((self.freq_xlating_fir_filter_DEC_LP_0, 0), (self.band_pass_filter_0_0_1_0_1, 0))
        self.connect((self.freq_xlating_fir_filter_DEC_LP_0, 0), (self.band_pass_filter_0_0_1_1, 0))
        self.connect((self.freq_xlating_fir_filter_DEC_LP_0, 0), (self.band_pass_filter_0_0_2, 0))
        self.connect((self.freq_xlating_fir_filter_DEC_LP_0, 0), (self.band_pass_filter_0_1, 0))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_samp_rate_decimated(self.samp_rate/self.decim_total)
        self.freq_xlating_fir_filter_DEC_LP_0.set_taps((firdes.low_pass(1, self.samp_rate, self.samp_rate_decimated*0.5,self.transition_bw, firdes.WIN_HAMMING, 6.76)))
        self.freq_xlating_fir_filter_DEC_LP.set_taps((firdes.low_pass(1, self.samp_rate, self.samp_rate_decimated*0.5,self.transition_bw, firdes.WIN_HAMMING, 6.76)))
        self.band_pass_filter_0_1.set_taps(firdes.complex_band_pass(1, self.samp_rate/self.decim_total, -20, 20, 10, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_2.set_taps(firdes.complex_band_pass(1, self.samp_rate/self.decim_total, -40, 0, 10, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_1_1.set_taps(firdes.complex_band_pass(1, self.samp_rate/self.decim_total, 0, 40, 10, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_1_0_1.set_taps(firdes.complex_band_pass(1, self.samp_rate/self.decim_total, 20, 60, 10, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_1_0_0_1.set_taps(firdes.complex_band_pass(1, self.samp_rate/self.decim_total, 40, 80, 10, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_1_0_0_0_1.set_taps(firdes.complex_band_pass(1, self.samp_rate/self.decim_total, 60, 100, 10, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_1_0_0_0_0_0.set_taps(firdes.complex_band_pass(1, self.samp_rate/self.decim_total, 80, 120, 10, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_1_0_0_0_0.set_taps(firdes.complex_band_pass(1, self.samp_rate/self.decim_total, 80, 120, 10, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_1_0_0_0.set_taps(firdes.complex_band_pass(1, self.samp_rate/self.decim_total, 60, 100, 10, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_1_0_0.set_taps(firdes.complex_band_pass(1, self.samp_rate/self.decim_total, 40, 80, 10, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_1_0.set_taps(firdes.complex_band_pass(1, self.samp_rate/self.decim_total, 20, 60, 10, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_1.set_taps(firdes.complex_band_pass(1, self.samp_rate/self.decim_total, 0, 40, 10, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_1.set_taps(firdes.complex_band_pass(1, self.samp_rate/self.decim_total, -60, -20, 10, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0_1.set_taps(firdes.complex_band_pass(1, self.samp_rate/self.decim_total, -80, -40, 10, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0_0_1.set_taps(firdes.complex_band_pass(1, self.samp_rate/self.decim_total, -100, -60, 10, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0_0_0_0.set_taps(firdes.complex_band_pass(1, self.samp_rate/self.decim_total, -120, -80, 10, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0_0_0.set_taps(firdes.complex_band_pass(1, self.samp_rate/self.decim_total, -120, -80, 10, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0_0.set_taps(firdes.complex_band_pass(1, self.samp_rate/self.decim_total, -100, -60, 10, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0.set_taps(firdes.complex_band_pass(1, self.samp_rate/self.decim_total, -80, -40, 10, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0.set_taps(firdes.complex_band_pass(1, self.samp_rate/self.decim_total, -60, -20, 10, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0.set_taps(firdes.complex_band_pass(1, self.samp_rate/self.decim_total, -40, 0, 10, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0.set_taps(firdes.complex_band_pass(1, self.samp_rate/self.decim_total, -20, 20, 10, firdes.WIN_HAMMING, 6.76))
        self.airspyhf_source_0_0.set_sample_rate(self.samp_rate)
        self.airspyhf_source_0.set_sample_rate(self.samp_rate)

    def get_decim_total(self):
        return self.decim_total

    def set_decim_total(self, decim_total):
        self.decim_total = decim_total
        self.set_samp_rate_decimated(self.samp_rate/self.decim_total)
        self.band_pass_filter_0_1.set_taps(firdes.complex_band_pass(1, self.samp_rate/self.decim_total, -20, 20, 10, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_2.set_taps(firdes.complex_band_pass(1, self.samp_rate/self.decim_total, -40, 0, 10, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_1_1.set_taps(firdes.complex_band_pass(1, self.samp_rate/self.decim_total, 0, 40, 10, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_1_0_1.set_taps(firdes.complex_band_pass(1, self.samp_rate/self.decim_total, 20, 60, 10, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_1_0_0_1.set_taps(firdes.complex_band_pass(1, self.samp_rate/self.decim_total, 40, 80, 10, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_1_0_0_0_1.set_taps(firdes.complex_band_pass(1, self.samp_rate/self.decim_total, 60, 100, 10, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_1_0_0_0_0_0.set_taps(firdes.complex_band_pass(1, self.samp_rate/self.decim_total, 80, 120, 10, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_1_0_0_0_0.set_taps(firdes.complex_band_pass(1, self.samp_rate/self.decim_total, 80, 120, 10, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_1_0_0_0.set_taps(firdes.complex_band_pass(1, self.samp_rate/self.decim_total, 60, 100, 10, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_1_0_0.set_taps(firdes.complex_band_pass(1, self.samp_rate/self.decim_total, 40, 80, 10, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_1_0.set_taps(firdes.complex_band_pass(1, self.samp_rate/self.decim_total, 20, 60, 10, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_1.set_taps(firdes.complex_band_pass(1, self.samp_rate/self.decim_total, 0, 40, 10, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_1.set_taps(firdes.complex_band_pass(1, self.samp_rate/self.decim_total, -60, -20, 10, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0_1.set_taps(firdes.complex_band_pass(1, self.samp_rate/self.decim_total, -80, -40, 10, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0_0_1.set_taps(firdes.complex_band_pass(1, self.samp_rate/self.decim_total, -100, -60, 10, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0_0_0_0.set_taps(firdes.complex_band_pass(1, self.samp_rate/self.decim_total, -120, -80, 10, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0_0_0.set_taps(firdes.complex_band_pass(1, self.samp_rate/self.decim_total, -120, -80, 10, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0_0.set_taps(firdes.complex_band_pass(1, self.samp_rate/self.decim_total, -100, -60, 10, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0.set_taps(firdes.complex_band_pass(1, self.samp_rate/self.decim_total, -80, -40, 10, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0.set_taps(firdes.complex_band_pass(1, self.samp_rate/self.decim_total, -60, -20, 10, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0.set_taps(firdes.complex_band_pass(1, self.samp_rate/self.decim_total, -40, 0, 10, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0.set_taps(firdes.complex_band_pass(1, self.samp_rate/self.decim_total, -20, 20, 10, firdes.WIN_HAMMING, 6.76))

    def get_samp_rate_decimated(self):
        return self.samp_rate_decimated

    def set_samp_rate_decimated(self, samp_rate_decimated):
        self.samp_rate_decimated = samp_rate_decimated
        self.set_transition_bw(self.samp_rate_decimated/4)
        self.freq_xlating_fir_filter_DEC_LP_0.set_taps((firdes.low_pass(1, self.samp_rate, self.samp_rate_decimated*0.5,self.transition_bw, firdes.WIN_HAMMING, 6.76)))
        self.freq_xlating_fir_filter_DEC_LP.set_taps((firdes.low_pass(1, self.samp_rate, self.samp_rate_decimated*0.5,self.transition_bw, firdes.WIN_HAMMING, 6.76)))

    def get_vect_size(self):
        return self.vect_size

    def set_vect_size(self, vect_size):
        self.vect_size = vect_size
        self.blocks_moving_average_xx_0_2_2.set_length_and_scale(self.vect_size, 1)
        self.blocks_moving_average_xx_0_2_1_1.set_length_and_scale(self.vect_size, 1)
        self.blocks_moving_average_xx_0_2_1_0_3.set_length_and_scale(self.vect_size, 1)
        self.blocks_moving_average_xx_0_2_1_0_2_1.set_length_and_scale(self.vect_size, 1)
        self.blocks_moving_average_xx_0_2_1_0_2_0_0.set_length_and_scale(self.vect_size, 1)
        self.blocks_moving_average_xx_0_2_1_0_2_0.set_length_and_scale(self.vect_size, 1)
        self.blocks_moving_average_xx_0_2_1_0_2.set_length_and_scale(self.vect_size, 1)
        self.blocks_moving_average_xx_0_2_1_0_1_0.set_length_and_scale(self.vect_size, 1)
        self.blocks_moving_average_xx_0_2_1_0_1.set_length_and_scale(self.vect_size, 1)
        self.blocks_moving_average_xx_0_2_1_0_0_0.set_length_and_scale(self.vect_size, 1)
        self.blocks_moving_average_xx_0_2_1_0_0.set_length_and_scale(self.vect_size, 1)
        self.blocks_moving_average_xx_0_2_1_0.set_length_and_scale(self.vect_size, 1)
        self.blocks_moving_average_xx_0_2_1.set_length_and_scale(self.vect_size, 1)
        self.blocks_moving_average_xx_0_2_0_0.set_length_and_scale(self.vect_size, 1)
        self.blocks_moving_average_xx_0_2_0.set_length_and_scale(self.vect_size, 1)
        self.blocks_moving_average_xx_0_2.set_length_and_scale(self.vect_size, 1)
        self.blocks_moving_average_xx_0_1_0.set_length_and_scale(self.vect_size, 1)
        self.blocks_moving_average_xx_0_1.set_length_and_scale(self.vect_size, 1)

    def get_transition_bw_fbank(self):
        return self.transition_bw_fbank

    def set_transition_bw_fbank(self, transition_bw_fbank):
        self.transition_bw_fbank = transition_bw_fbank

    def get_transition_bw(self):
        return self.transition_bw

    def set_transition_bw(self, transition_bw):
        self.transition_bw = transition_bw
        self.freq_xlating_fir_filter_DEC_LP_0.set_taps((firdes.low_pass(1, self.samp_rate, self.samp_rate_decimated*0.5,self.transition_bw, firdes.WIN_HAMMING, 6.76)))
        self.freq_xlating_fir_filter_DEC_LP.set_taps((firdes.low_pass(1, self.samp_rate, self.samp_rate_decimated*0.5,self.transition_bw, firdes.WIN_HAMMING, 6.76)))

    def get_cutoff_fbank(self):
        return self.cutoff_fbank

    def set_cutoff_fbank(self, cutoff_fbank):
        self.cutoff_fbank = cutoff_fbank

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq


def main(top_block_cls=mov_avg, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
