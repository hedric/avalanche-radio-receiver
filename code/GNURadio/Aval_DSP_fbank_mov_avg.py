#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Aval Dsp Fbank Mov Avg
# Generated: Fri Jan 18 14:33:35 2019
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


class Aval_DSP_fbank_mov_avg(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Aval Dsp Fbank Mov Avg")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 768000
        self.decim_total = decim_total = 200*8
        self.transition_bw_fbank = transition_bw_fbank = 20
        self.samp_rate_decimated = samp_rate_decimated = samp_rate/decim_total
        self.cutoff_fbank = cutoff_fbank = 20
        self.vect_size = vect_size = 1
        self.transition_bw = transition_bw = samp_rate_decimated/4
        self.center_freq_offset = center_freq_offset = 120
        self.center_freq = center_freq = 457e3
        self.bp_decimation = bp_decimation = 16
        self.bandpass_taps = bandpass_taps = firdes.complex_band_pass (1, samp_rate_decimated, -1*cutoff_fbank, cutoff_fbank, transition_bw_fbank, firdes.WIN_HAMMING, 6.76)

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
        self.blocks_complex_to_mag_squared_0_2_0 = blocks.complex_to_mag_squared(1)
        self.blocks_complex_to_mag_squared_0_2 = blocks.complex_to_mag_squared(1)
        self.band_pass_filter_0_1 = filter.fir_filter_ccc(bp_decimation, firdes.complex_band_pass(
        	1, samp_rate_decimated, -cutoff_fbank, cutoff_fbank, transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_1 = filter.fir_filter_ccc(bp_decimation, firdes.complex_band_pass(
        	1, samp_rate_decimated, 0*cutoff_fbank, 2*cutoff_fbank, transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_1 = filter.fir_filter_ccc(bp_decimation, firdes.complex_band_pass(
        	1, samp_rate_decimated, -6*cutoff_fbank, -4*cutoff_fbank, transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0_2 = filter.fir_filter_ccc(bp_decimation, firdes.complex_band_pass(
        	1, samp_rate_decimated, 1*cutoff_fbank, 3*cutoff_fbank, transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0_1_0 = filter.fir_filter_ccc(bp_decimation, firdes.complex_band_pass(
        	1, samp_rate_decimated, -5*cutoff_fbank, -3*cutoff_fbank, transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0_1 = filter.fir_filter_ccc(bp_decimation, firdes.complex_band_pass(
        	1, samp_rate_decimated, -5*cutoff_fbank, -3*cutoff_fbank, transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0_0_2 = filter.fir_filter_ccc(bp_decimation, firdes.complex_band_pass(
        	1, samp_rate_decimated, 2*cutoff_fbank, 4*cutoff_fbank, transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0_0_1_0 = filter.fir_filter_ccc(bp_decimation, firdes.complex_band_pass(
        	1, samp_rate_decimated, -4*cutoff_fbank, -2*cutoff_fbank, transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0_0_1 = filter.fir_filter_ccc(bp_decimation, firdes.complex_band_pass(
        	1, samp_rate_decimated, -4*cutoff_fbank, -2*cutoff_fbank, transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0_0_0_2 = filter.fir_filter_ccc(bp_decimation, firdes.complex_band_pass(
        	1, samp_rate_decimated, 3*cutoff_fbank, 5*cutoff_fbank, transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0_0_0_1_0 = filter.fir_filter_ccc(bp_decimation, firdes.complex_band_pass(
        	1, samp_rate_decimated, -3*cutoff_fbank, -cutoff_fbank, transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0_0_0_1 = filter.fir_filter_ccc(bp_decimation, firdes.complex_band_pass(
        	1, samp_rate_decimated, -3*cutoff_fbank, -cutoff_fbank, transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0_0_0_0_1 = filter.fir_filter_ccc(bp_decimation, firdes.complex_band_pass(
        	1, samp_rate_decimated, 4*cutoff_fbank, 6*cutoff_fbank, transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0_0_0_0_0_0 = filter.fir_filter_ccc(bp_decimation, firdes.complex_band_pass(
        	1, samp_rate_decimated, -2*cutoff_fbank, 0*cutoff_fbank, transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0_0_0_0_0 = filter.fir_filter_ccc(bp_decimation, firdes.complex_band_pass(
        	1, samp_rate_decimated, -2*cutoff_fbank, 0*cutoff_fbank, transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0_0_0_0 = filter.fir_filter_ccc(bp_decimation, firdes.complex_band_pass(
        	1, samp_rate_decimated, 4*cutoff_fbank, 6*cutoff_fbank, transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0_0_0 = filter.fir_filter_ccc(bp_decimation, firdes.complex_band_pass(
        	1, samp_rate_decimated, 3*cutoff_fbank, 5*cutoff_fbank, transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0_0 = filter.fir_filter_ccc(bp_decimation, firdes.complex_band_pass(
        	1, samp_rate_decimated, 2*cutoff_fbank, 4*cutoff_fbank, transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0 = filter.fir_filter_ccc(bp_decimation, firdes.complex_band_pass(
        	1, samp_rate_decimated, 1*cutoff_fbank, 3*cutoff_fbank, transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0 = filter.fir_filter_ccc(bp_decimation, firdes.complex_band_pass(
        	1, samp_rate_decimated, -6*cutoff_fbank, -4*cutoff_fbank, transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0 = filter.fir_filter_ccc(bp_decimation, firdes.complex_band_pass(
        	1, samp_rate_decimated, 0*cutoff_fbank, 2*cutoff_fbank, transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0 = filter.fir_filter_ccc(bp_decimation, firdes.complex_band_pass(
        	1, samp_rate_decimated, -cutoff_fbank, cutoff_fbank, transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.airspyhf_source_0_0 = osmosdr.source( args="numchan=" + str(1) + " " + 'C852D65D9DBF34DD' )
        self.airspyhf_source_0_0.set_sample_rate(samp_rate)
        self.airspyhf_source_0_0.set_center_freq(457000 , 0)
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
        self.connect((self.band_pass_filter_0, 0), (self.blocks_stream_mux_0, 5))
        self.connect((self.band_pass_filter_0_0, 0), (self.blocks_stream_mux_0, 4))
        self.connect((self.band_pass_filter_0_0_0, 0), (self.blocks_stream_mux_0, 10))
        self.connect((self.band_pass_filter_0_0_0_0, 0), (self.blocks_stream_mux_0, 3))
        self.connect((self.band_pass_filter_0_0_0_0_0, 0), (self.blocks_stream_mux_0, 2))
        self.connect((self.band_pass_filter_0_0_0_0_0_0, 0), (self.blocks_stream_mux_0, 1))
        self.connect((self.band_pass_filter_0_0_0_0_0_0_0, 0), (self.blocks_stream_mux_0, 0))
        self.connect((self.band_pass_filter_0_0_0_0_0_0_0_0, 0), (self.blocks_stream_mux_0, 6))
        self.connect((self.band_pass_filter_0_0_0_0_0_0_0_0_0, 0), (self.blocks_stream_mux_0_0, 6))
        self.connect((self.band_pass_filter_0_0_0_0_0_0_0_1, 0), (self.blocks_stream_mux_0_0, 0))
        self.connect((self.band_pass_filter_0_0_0_0_0_0_1, 0), (self.blocks_stream_mux_0, 7))
        self.connect((self.band_pass_filter_0_0_0_0_0_0_1_0, 0), (self.blocks_stream_mux_0_0, 7))
        self.connect((self.band_pass_filter_0_0_0_0_0_0_2, 0), (self.blocks_stream_mux_0_0, 1))
        self.connect((self.band_pass_filter_0_0_0_0_0_1, 0), (self.blocks_stream_mux_0, 8))
        self.connect((self.band_pass_filter_0_0_0_0_0_1_0, 0), (self.blocks_stream_mux_0_0, 8))
        self.connect((self.band_pass_filter_0_0_0_0_0_2, 0), (self.blocks_stream_mux_0_0, 2))
        self.connect((self.band_pass_filter_0_0_0_0_1, 0), (self.blocks_stream_mux_0, 9))
        self.connect((self.band_pass_filter_0_0_0_0_1_0, 0), (self.blocks_stream_mux_0_0, 9))
        self.connect((self.band_pass_filter_0_0_0_0_2, 0), (self.blocks_stream_mux_0_0, 3))
        self.connect((self.band_pass_filter_0_0_0_1, 0), (self.blocks_stream_mux_0_0, 10))
        self.connect((self.band_pass_filter_0_0_1, 0), (self.blocks_stream_mux_0_0, 4))
        self.connect((self.band_pass_filter_0_1, 0), (self.blocks_stream_mux_0_0, 5))
        self.connect((self.blocks_complex_to_mag_squared_0_2, 0), (self.blocks_stream_to_vector_1_0_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_0_2_0, 0), (self.blocks_stream_to_vector_1_0_0_0, 0))
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
        self.connect((self.freq_xlating_fir_filter_DEC_LP, 0), (self.band_pass_filter_0_0_0_0_0_0_0, 0))
        self.connect((self.freq_xlating_fir_filter_DEC_LP, 0), (self.band_pass_filter_0_0_0_0_0_0_0_0, 0))
        self.connect((self.freq_xlating_fir_filter_DEC_LP, 0), (self.band_pass_filter_0_0_0_0_0_0_1, 0))
        self.connect((self.freq_xlating_fir_filter_DEC_LP, 0), (self.band_pass_filter_0_0_0_0_0_1, 0))
        self.connect((self.freq_xlating_fir_filter_DEC_LP, 0), (self.band_pass_filter_0_0_0_0_1, 0))
        self.connect((self.freq_xlating_fir_filter_DEC_LP_0, 0), (self.band_pass_filter_0_0_0_0_0_0_0_0_0, 0))
        self.connect((self.freq_xlating_fir_filter_DEC_LP_0, 0), (self.band_pass_filter_0_0_0_0_0_0_0_1, 0))
        self.connect((self.freq_xlating_fir_filter_DEC_LP_0, 0), (self.band_pass_filter_0_0_0_0_0_0_1_0, 0))
        self.connect((self.freq_xlating_fir_filter_DEC_LP_0, 0), (self.band_pass_filter_0_0_0_0_0_0_2, 0))
        self.connect((self.freq_xlating_fir_filter_DEC_LP_0, 0), (self.band_pass_filter_0_0_0_0_0_1_0, 0))
        self.connect((self.freq_xlating_fir_filter_DEC_LP_0, 0), (self.band_pass_filter_0_0_0_0_0_2, 0))
        self.connect((self.freq_xlating_fir_filter_DEC_LP_0, 0), (self.band_pass_filter_0_0_0_0_1_0, 0))
        self.connect((self.freq_xlating_fir_filter_DEC_LP_0, 0), (self.band_pass_filter_0_0_0_0_2, 0))
        self.connect((self.freq_xlating_fir_filter_DEC_LP_0, 0), (self.band_pass_filter_0_0_0_1, 0))
        self.connect((self.freq_xlating_fir_filter_DEC_LP_0, 0), (self.band_pass_filter_0_0_1, 0))
        self.connect((self.freq_xlating_fir_filter_DEC_LP_0, 0), (self.band_pass_filter_0_1, 0))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_samp_rate_decimated(self.samp_rate/self.decim_total)
        self.freq_xlating_fir_filter_DEC_LP_0.set_taps((firdes.low_pass(1, self.samp_rate, self.samp_rate_decimated*0.5,self.transition_bw, firdes.WIN_HAMMING, 6.76)))
        self.freq_xlating_fir_filter_DEC_LP.set_taps((firdes.low_pass(1, self.samp_rate, self.samp_rate_decimated*0.5,self.transition_bw, firdes.WIN_HAMMING, 6.76)))
        self.airspyhf_source_0_0.set_sample_rate(self.samp_rate)
        self.airspyhf_source_0.set_sample_rate(self.samp_rate)

    def get_decim_total(self):
        return self.decim_total

    def set_decim_total(self, decim_total):
        self.decim_total = decim_total
        self.set_samp_rate_decimated(self.samp_rate/self.decim_total)

    def get_transition_bw_fbank(self):
        return self.transition_bw_fbank

    def set_transition_bw_fbank(self, transition_bw_fbank):
        self.transition_bw_fbank = transition_bw_fbank
        self.set_bandpass_taps(firdes.complex_band_pass (1, self.samp_rate_decimated, -1*self.cutoff_fbank, self.cutoff_fbank, self.transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_1.set_taps(firdes.complex_band_pass(1, self.samp_rate_decimated, -self.cutoff_fbank, self.cutoff_fbank, self.transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_1.set_taps(firdes.complex_band_pass(1, self.samp_rate_decimated, 0*self.cutoff_fbank, 2*self.cutoff_fbank, self.transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_1.set_taps(firdes.complex_band_pass(1, self.samp_rate_decimated, -6*self.cutoff_fbank, -4*self.cutoff_fbank, self.transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0_2.set_taps(firdes.complex_band_pass(1, self.samp_rate_decimated, 1*self.cutoff_fbank, 3*self.cutoff_fbank, self.transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0_1_0.set_taps(firdes.complex_band_pass(1, self.samp_rate_decimated, -5*self.cutoff_fbank, -3*self.cutoff_fbank, self.transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0_1.set_taps(firdes.complex_band_pass(1, self.samp_rate_decimated, -5*self.cutoff_fbank, -3*self.cutoff_fbank, self.transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0_0_2.set_taps(firdes.complex_band_pass(1, self.samp_rate_decimated, 2*self.cutoff_fbank, 4*self.cutoff_fbank, self.transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0_0_1_0.set_taps(firdes.complex_band_pass(1, self.samp_rate_decimated, -4*self.cutoff_fbank, -2*self.cutoff_fbank, self.transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0_0_1.set_taps(firdes.complex_band_pass(1, self.samp_rate_decimated, -4*self.cutoff_fbank, -2*self.cutoff_fbank, self.transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0_0_0_2.set_taps(firdes.complex_band_pass(1, self.samp_rate_decimated, 3*self.cutoff_fbank, 5*self.cutoff_fbank, self.transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0_0_0_1_0.set_taps(firdes.complex_band_pass(1, self.samp_rate_decimated, -3*self.cutoff_fbank, -self.cutoff_fbank, self.transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0_0_0_1.set_taps(firdes.complex_band_pass(1, self.samp_rate_decimated, -3*self.cutoff_fbank, -self.cutoff_fbank, self.transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0_0_0_0_1.set_taps(firdes.complex_band_pass(1, self.samp_rate_decimated, 4*self.cutoff_fbank, 6*self.cutoff_fbank, self.transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0_0_0_0_0_0.set_taps(firdes.complex_band_pass(1, self.samp_rate_decimated, -2*self.cutoff_fbank, 0*self.cutoff_fbank, self.transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0_0_0_0_0.set_taps(firdes.complex_band_pass(1, self.samp_rate_decimated, -2*self.cutoff_fbank, 0*self.cutoff_fbank, self.transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0_0_0_0.set_taps(firdes.complex_band_pass(1, self.samp_rate_decimated, 4*self.cutoff_fbank, 6*self.cutoff_fbank, self.transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0_0_0.set_taps(firdes.complex_band_pass(1, self.samp_rate_decimated, 3*self.cutoff_fbank, 5*self.cutoff_fbank, self.transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0_0.set_taps(firdes.complex_band_pass(1, self.samp_rate_decimated, 2*self.cutoff_fbank, 4*self.cutoff_fbank, self.transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0.set_taps(firdes.complex_band_pass(1, self.samp_rate_decimated, 1*self.cutoff_fbank, 3*self.cutoff_fbank, self.transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0.set_taps(firdes.complex_band_pass(1, self.samp_rate_decimated, -6*self.cutoff_fbank, -4*self.cutoff_fbank, self.transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0.set_taps(firdes.complex_band_pass(1, self.samp_rate_decimated, 0*self.cutoff_fbank, 2*self.cutoff_fbank, self.transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0.set_taps(firdes.complex_band_pass(1, self.samp_rate_decimated, -self.cutoff_fbank, self.cutoff_fbank, self.transition_bw_fbank, firdes.WIN_HAMMING, 6.76))

    def get_samp_rate_decimated(self):
        return self.samp_rate_decimated

    def set_samp_rate_decimated(self, samp_rate_decimated):
        self.samp_rate_decimated = samp_rate_decimated
        self.set_transition_bw(self.samp_rate_decimated/4)
        self.freq_xlating_fir_filter_DEC_LP_0.set_taps((firdes.low_pass(1, self.samp_rate, self.samp_rate_decimated*0.5,self.transition_bw, firdes.WIN_HAMMING, 6.76)))
        self.freq_xlating_fir_filter_DEC_LP.set_taps((firdes.low_pass(1, self.samp_rate, self.samp_rate_decimated*0.5,self.transition_bw, firdes.WIN_HAMMING, 6.76)))
        self.set_bandpass_taps(firdes.complex_band_pass (1, self.samp_rate_decimated, -1*self.cutoff_fbank, self.cutoff_fbank, self.transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_1.set_taps(firdes.complex_band_pass(1, self.samp_rate_decimated, -self.cutoff_fbank, self.cutoff_fbank, self.transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_1.set_taps(firdes.complex_band_pass(1, self.samp_rate_decimated, 0*self.cutoff_fbank, 2*self.cutoff_fbank, self.transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_1.set_taps(firdes.complex_band_pass(1, self.samp_rate_decimated, -6*self.cutoff_fbank, -4*self.cutoff_fbank, self.transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0_2.set_taps(firdes.complex_band_pass(1, self.samp_rate_decimated, 1*self.cutoff_fbank, 3*self.cutoff_fbank, self.transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0_1_0.set_taps(firdes.complex_band_pass(1, self.samp_rate_decimated, -5*self.cutoff_fbank, -3*self.cutoff_fbank, self.transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0_1.set_taps(firdes.complex_band_pass(1, self.samp_rate_decimated, -5*self.cutoff_fbank, -3*self.cutoff_fbank, self.transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0_0_2.set_taps(firdes.complex_band_pass(1, self.samp_rate_decimated, 2*self.cutoff_fbank, 4*self.cutoff_fbank, self.transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0_0_1_0.set_taps(firdes.complex_band_pass(1, self.samp_rate_decimated, -4*self.cutoff_fbank, -2*self.cutoff_fbank, self.transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0_0_1.set_taps(firdes.complex_band_pass(1, self.samp_rate_decimated, -4*self.cutoff_fbank, -2*self.cutoff_fbank, self.transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0_0_0_2.set_taps(firdes.complex_band_pass(1, self.samp_rate_decimated, 3*self.cutoff_fbank, 5*self.cutoff_fbank, self.transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0_0_0_1_0.set_taps(firdes.complex_band_pass(1, self.samp_rate_decimated, -3*self.cutoff_fbank, -self.cutoff_fbank, self.transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0_0_0_1.set_taps(firdes.complex_band_pass(1, self.samp_rate_decimated, -3*self.cutoff_fbank, -self.cutoff_fbank, self.transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0_0_0_0_1.set_taps(firdes.complex_band_pass(1, self.samp_rate_decimated, 4*self.cutoff_fbank, 6*self.cutoff_fbank, self.transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0_0_0_0_0_0.set_taps(firdes.complex_band_pass(1, self.samp_rate_decimated, -2*self.cutoff_fbank, 0*self.cutoff_fbank, self.transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0_0_0_0_0.set_taps(firdes.complex_band_pass(1, self.samp_rate_decimated, -2*self.cutoff_fbank, 0*self.cutoff_fbank, self.transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0_0_0_0.set_taps(firdes.complex_band_pass(1, self.samp_rate_decimated, 4*self.cutoff_fbank, 6*self.cutoff_fbank, self.transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0_0_0.set_taps(firdes.complex_band_pass(1, self.samp_rate_decimated, 3*self.cutoff_fbank, 5*self.cutoff_fbank, self.transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0_0.set_taps(firdes.complex_band_pass(1, self.samp_rate_decimated, 2*self.cutoff_fbank, 4*self.cutoff_fbank, self.transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0.set_taps(firdes.complex_band_pass(1, self.samp_rate_decimated, 1*self.cutoff_fbank, 3*self.cutoff_fbank, self.transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0.set_taps(firdes.complex_band_pass(1, self.samp_rate_decimated, -6*self.cutoff_fbank, -4*self.cutoff_fbank, self.transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0.set_taps(firdes.complex_band_pass(1, self.samp_rate_decimated, 0*self.cutoff_fbank, 2*self.cutoff_fbank, self.transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0.set_taps(firdes.complex_band_pass(1, self.samp_rate_decimated, -self.cutoff_fbank, self.cutoff_fbank, self.transition_bw_fbank, firdes.WIN_HAMMING, 6.76))

    def get_cutoff_fbank(self):
        return self.cutoff_fbank

    def set_cutoff_fbank(self, cutoff_fbank):
        self.cutoff_fbank = cutoff_fbank
        self.set_bandpass_taps(firdes.complex_band_pass (1, self.samp_rate_decimated, -1*self.cutoff_fbank, self.cutoff_fbank, self.transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_1.set_taps(firdes.complex_band_pass(1, self.samp_rate_decimated, -self.cutoff_fbank, self.cutoff_fbank, self.transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_1.set_taps(firdes.complex_band_pass(1, self.samp_rate_decimated, 0*self.cutoff_fbank, 2*self.cutoff_fbank, self.transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_1.set_taps(firdes.complex_band_pass(1, self.samp_rate_decimated, -6*self.cutoff_fbank, -4*self.cutoff_fbank, self.transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0_2.set_taps(firdes.complex_band_pass(1, self.samp_rate_decimated, 1*self.cutoff_fbank, 3*self.cutoff_fbank, self.transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0_1_0.set_taps(firdes.complex_band_pass(1, self.samp_rate_decimated, -5*self.cutoff_fbank, -3*self.cutoff_fbank, self.transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0_1.set_taps(firdes.complex_band_pass(1, self.samp_rate_decimated, -5*self.cutoff_fbank, -3*self.cutoff_fbank, self.transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0_0_2.set_taps(firdes.complex_band_pass(1, self.samp_rate_decimated, 2*self.cutoff_fbank, 4*self.cutoff_fbank, self.transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0_0_1_0.set_taps(firdes.complex_band_pass(1, self.samp_rate_decimated, -4*self.cutoff_fbank, -2*self.cutoff_fbank, self.transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0_0_1.set_taps(firdes.complex_band_pass(1, self.samp_rate_decimated, -4*self.cutoff_fbank, -2*self.cutoff_fbank, self.transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0_0_0_2.set_taps(firdes.complex_band_pass(1, self.samp_rate_decimated, 3*self.cutoff_fbank, 5*self.cutoff_fbank, self.transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0_0_0_1_0.set_taps(firdes.complex_band_pass(1, self.samp_rate_decimated, -3*self.cutoff_fbank, -self.cutoff_fbank, self.transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0_0_0_1.set_taps(firdes.complex_band_pass(1, self.samp_rate_decimated, -3*self.cutoff_fbank, -self.cutoff_fbank, self.transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0_0_0_0_1.set_taps(firdes.complex_band_pass(1, self.samp_rate_decimated, 4*self.cutoff_fbank, 6*self.cutoff_fbank, self.transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0_0_0_0_0_0.set_taps(firdes.complex_band_pass(1, self.samp_rate_decimated, -2*self.cutoff_fbank, 0*self.cutoff_fbank, self.transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0_0_0_0_0.set_taps(firdes.complex_band_pass(1, self.samp_rate_decimated, -2*self.cutoff_fbank, 0*self.cutoff_fbank, self.transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0_0_0_0.set_taps(firdes.complex_band_pass(1, self.samp_rate_decimated, 4*self.cutoff_fbank, 6*self.cutoff_fbank, self.transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0_0_0.set_taps(firdes.complex_band_pass(1, self.samp_rate_decimated, 3*self.cutoff_fbank, 5*self.cutoff_fbank, self.transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0_0.set_taps(firdes.complex_band_pass(1, self.samp_rate_decimated, 2*self.cutoff_fbank, 4*self.cutoff_fbank, self.transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0_0.set_taps(firdes.complex_band_pass(1, self.samp_rate_decimated, 1*self.cutoff_fbank, 3*self.cutoff_fbank, self.transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0.set_taps(firdes.complex_band_pass(1, self.samp_rate_decimated, -6*self.cutoff_fbank, -4*self.cutoff_fbank, self.transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0.set_taps(firdes.complex_band_pass(1, self.samp_rate_decimated, 0*self.cutoff_fbank, 2*self.cutoff_fbank, self.transition_bw_fbank, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0.set_taps(firdes.complex_band_pass(1, self.samp_rate_decimated, -self.cutoff_fbank, self.cutoff_fbank, self.transition_bw_fbank, firdes.WIN_HAMMING, 6.76))

    def get_vect_size(self):
        return self.vect_size

    def set_vect_size(self, vect_size):
        self.vect_size = vect_size

    def get_transition_bw(self):
        return self.transition_bw

    def set_transition_bw(self, transition_bw):
        self.transition_bw = transition_bw
        self.freq_xlating_fir_filter_DEC_LP_0.set_taps((firdes.low_pass(1, self.samp_rate, self.samp_rate_decimated*0.5,self.transition_bw, firdes.WIN_HAMMING, 6.76)))
        self.freq_xlating_fir_filter_DEC_LP.set_taps((firdes.low_pass(1, self.samp_rate, self.samp_rate_decimated*0.5,self.transition_bw, firdes.WIN_HAMMING, 6.76)))

    def get_center_freq_offset(self):
        return self.center_freq_offset

    def set_center_freq_offset(self, center_freq_offset):
        self.center_freq_offset = center_freq_offset

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq

    def get_bp_decimation(self):
        return self.bp_decimation

    def set_bp_decimation(self, bp_decimation):
        self.bp_decimation = bp_decimation

    def get_bandpass_taps(self):
        return self.bandpass_taps

    def set_bandpass_taps(self, bandpass_taps):
        self.bandpass_taps = bandpass_taps


def main(top_block_cls=Aval_DSP_fbank_mov_avg, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
