#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Avalanche Beacon Detection
# Author: Richard Hedlund
# Description: A signal processing chain that utilizes a matched filter for detecting avalanche beacons at 457 kHz
# Generated: Fri Jan 25 13:10:53 2019
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


class DSP_matched(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Avalanche Beacon Detection")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 768e3
        self.decim_total = decim_total = 200*8
        self.samp_rate_decimated = samp_rate_decimated = samp_rate/decim_total
        self.vec_len = vec_len = 480
        self.transition_bw = transition_bw = samp_rate_decimated/4
        self.center_freq = center_freq = 457e3
        self.FIR_taps_matched_48 = FIR_taps_matched_48 = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

        ##################################################
        # Blocks
        ##################################################
        self.zeromq_push_sink_Y = zeromq.push_sink(gr.sizeof_float, vec_len, "tcp://127.0.0.1:5556", 100, False, -1)
        self.zeromq_push_sink_X = zeromq.push_sink(gr.sizeof_float, vec_len, "tcp://127.0.0.1:5555", 100, False, -1)
        self.freq_xlating_fir_filter_DEC_LP_Y = filter.freq_xlating_fir_filter_ccc(decim_total, (firdes.low_pass(1, samp_rate,( samp_rate_decimated/2)*0.5,transition_bw, firdes.WIN_HAMMING, 6.76)), 0, samp_rate)
        self.freq_xlating_fir_filter_DEC_LP_X = filter.freq_xlating_fir_filter_ccc(decim_total, (firdes.low_pass(1, samp_rate,( samp_rate_decimated/2)*0.5,transition_bw, firdes.WIN_HAMMING, 6.76)), 0, samp_rate)
        self.fir_filter_matched_Y = filter.fir_filter_ccc(1, (FIR_taps_matched_48))
        self.fir_filter_matched_Y.declare_sample_delay(0)
        self.fir_filter_matched_X = filter.fir_filter_ccc(1, (FIR_taps_matched_48))
        self.fir_filter_matched_X.declare_sample_delay(0)
        self.blocks_stream_to_vector_1_0_0_0 = blocks.stream_to_vector(gr.sizeof_float*1, vec_len)
        self.blocks_stream_to_vector_1_0_0 = blocks.stream_to_vector(gr.sizeof_float*1, vec_len)
        self.blocks_multiply_const_Y = blocks.multiply_const_vcc((0.020833, ))
        self.blocks_multiply_const_X = blocks.multiply_const_vcc((0.020833, ))
        self.blocks_complex_to_mag_0_0_0 = blocks.complex_to_mag(1)
        self.blocks_complex_to_mag_0_0 = blocks.complex_to_mag(1)
        self.airspyhf_source_Y = osmosdr.source( args="numchan=" + str(1) + " " + 'airspyhf=1' )
        self.airspyhf_source_Y.set_sample_rate(samp_rate)
        self.airspyhf_source_Y.set_center_freq(center_freq, 0)
        self.airspyhf_source_Y.set_freq_corr(0, 0)
        self.airspyhf_source_Y.set_iq_balance_mode(0, 0)
        self.airspyhf_source_Y.set_gain_mode(False, 0)
        self.airspyhf_source_Y.set_gain(6, "LNA", 0)
        self.airspyhf_source_Y.set_gain(0, "ATT", 0)

        self.airspyhf_source_X = osmosdr.source( args="numchan=" + str(1) + " " + 'airspyhf=0' )
        self.airspyhf_source_X.set_sample_rate(samp_rate)
        self.airspyhf_source_X.set_center_freq(center_freq, 0)
        self.airspyhf_source_X.set_freq_corr(0, 0)
        self.airspyhf_source_X.set_iq_balance_mode(0, 0)
        self.airspyhf_source_X.set_gain_mode(False, 0)
        self.airspyhf_source_X.set_gain(6, "LNA", 0)
        self.airspyhf_source_X.set_gain(0, "ATT", 0)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.airspyhf_source_X, 0), (self.freq_xlating_fir_filter_DEC_LP_X, 0))
        self.connect((self.airspyhf_source_Y, 0), (self.freq_xlating_fir_filter_DEC_LP_Y, 0))
        self.connect((self.blocks_complex_to_mag_0_0, 0), (self.blocks_stream_to_vector_1_0_0, 0))
        self.connect((self.blocks_complex_to_mag_0_0_0, 0), (self.blocks_stream_to_vector_1_0_0_0, 0))
        self.connect((self.blocks_multiply_const_X, 0), (self.blocks_complex_to_mag_0_0, 0))
        self.connect((self.blocks_multiply_const_Y, 0), (self.blocks_complex_to_mag_0_0_0, 0))
        self.connect((self.blocks_stream_to_vector_1_0_0, 0), (self.zeromq_push_sink_X, 0))
        self.connect((self.blocks_stream_to_vector_1_0_0_0, 0), (self.zeromq_push_sink_Y, 0))
        self.connect((self.fir_filter_matched_X, 0), (self.blocks_multiply_const_X, 0))
        self.connect((self.fir_filter_matched_Y, 0), (self.blocks_multiply_const_Y, 0))
        self.connect((self.freq_xlating_fir_filter_DEC_LP_X, 0), (self.fir_filter_matched_X, 0))
        self.connect((self.freq_xlating_fir_filter_DEC_LP_Y, 0), (self.fir_filter_matched_Y, 0))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_samp_rate_decimated(self.samp_rate/self.decim_total)
        self.freq_xlating_fir_filter_DEC_LP_Y.set_taps((firdes.low_pass(1, self.samp_rate,( self.samp_rate_decimated/2)*0.5,self.transition_bw, firdes.WIN_HAMMING, 6.76)))
        self.freq_xlating_fir_filter_DEC_LP_X.set_taps((firdes.low_pass(1, self.samp_rate,( self.samp_rate_decimated/2)*0.5,self.transition_bw, firdes.WIN_HAMMING, 6.76)))
        self.airspyhf_source_Y.set_sample_rate(self.samp_rate)
        self.airspyhf_source_X.set_sample_rate(self.samp_rate)

    def get_decim_total(self):
        return self.decim_total

    def set_decim_total(self, decim_total):
        self.decim_total = decim_total
        self.set_samp_rate_decimated(self.samp_rate/self.decim_total)

    def get_samp_rate_decimated(self):
        return self.samp_rate_decimated

    def set_samp_rate_decimated(self, samp_rate_decimated):
        self.samp_rate_decimated = samp_rate_decimated
        self.set_transition_bw(self.samp_rate_decimated/4)
        self.freq_xlating_fir_filter_DEC_LP_Y.set_taps((firdes.low_pass(1, self.samp_rate,( self.samp_rate_decimated/2)*0.5,self.transition_bw, firdes.WIN_HAMMING, 6.76)))
        self.freq_xlating_fir_filter_DEC_LP_X.set_taps((firdes.low_pass(1, self.samp_rate,( self.samp_rate_decimated/2)*0.5,self.transition_bw, firdes.WIN_HAMMING, 6.76)))

    def get_vec_len(self):
        return self.vec_len

    def set_vec_len(self, vec_len):
        self.vec_len = vec_len

    def get_transition_bw(self):
        return self.transition_bw

    def set_transition_bw(self, transition_bw):
        self.transition_bw = transition_bw
        self.freq_xlating_fir_filter_DEC_LP_Y.set_taps((firdes.low_pass(1, self.samp_rate,( self.samp_rate_decimated/2)*0.5,self.transition_bw, firdes.WIN_HAMMING, 6.76)))
        self.freq_xlating_fir_filter_DEC_LP_X.set_taps((firdes.low_pass(1, self.samp_rate,( self.samp_rate_decimated/2)*0.5,self.transition_bw, firdes.WIN_HAMMING, 6.76)))

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq
        self.airspyhf_source_Y.set_center_freq(self.center_freq, 0)
        self.airspyhf_source_X.set_center_freq(self.center_freq, 0)

    def get_FIR_taps_matched_48(self):
        return self.FIR_taps_matched_48

    def set_FIR_taps_matched_48(self, FIR_taps_matched_48):
        self.FIR_taps_matched_48 = FIR_taps_matched_48
        self.fir_filter_matched_Y.set_taps((self.FIR_taps_matched_48))
        self.fir_filter_matched_X.set_taps((self.FIR_taps_matched_48))


def main(top_block_cls=DSP_matched, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
