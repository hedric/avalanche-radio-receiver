#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Data Export
# Generated: Tue Jan 22 14:06:44 2019
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
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import numpy as np
import osmosdr
import time
import wx


class DATA_export(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Data Export")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 768e3
        self.decim_total = decim_total = 200*8
        self.samp_rate_decimated = samp_rate_decimated = samp_rate/decim_total
        self.vec_len = vec_len = 480
        self.transition_bw_fbank = transition_bw_fbank = 20
        self.transition_bw = transition_bw = samp_rate_decimated/4
        self.samp_rate_0 = samp_rate_0 = 768000
        self.cutoff_fbank = cutoff_fbank = 20
        self.center_freq_offset = center_freq_offset = 120
        self.center_freq = center_freq = 457e3
        self.bp_decimation = bp_decimation = 16
        self.FIR_taps_matched_48 = FIR_taps_matched_48 = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        self.FIR_taps_matched_24 = FIR_taps_matched_24 = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

        ##################################################
        # Blocks
        ##################################################
        self.freq_xlating_fir_filter_DEC_LP = filter.freq_xlating_fir_filter_ccc(decim_total, (firdes.low_pass(1, samp_rate,( samp_rate_decimated/2)*0.5,transition_bw, firdes.WIN_HAMMING, 6.76)), 0, samp_rate)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_gr_complex*1, '/home/hedric/thesis/data/2019-01-22/ONnoisefloor-480sps', False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.airspyhf_source_1 = osmosdr.source( args="numchan=" + str(1) + " " + 'airspyhf=0' )
        self.airspyhf_source_1.set_sample_rate(samp_rate)
        self.airspyhf_source_1.set_center_freq(457000, 0)
        self.airspyhf_source_1.set_freq_corr(0, 0)
        self.airspyhf_source_1.set_iq_balance_mode(0, 0)
        self.airspyhf_source_1.set_gain_mode(False, 0)
        self.airspyhf_source_1.set_gain(6, "LNA", 0)
        self.airspyhf_source_1.set_gain(0, "ATT", 0)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.airspyhf_source_1, 0), (self.freq_xlating_fir_filter_DEC_LP, 0))
        self.connect((self.freq_xlating_fir_filter_DEC_LP, 0), (self.blocks_file_sink_0, 0))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_samp_rate_decimated(self.samp_rate/self.decim_total)
        self.freq_xlating_fir_filter_DEC_LP.set_taps((firdes.low_pass(1, self.samp_rate,( self.samp_rate_decimated/2)*0.5,self.transition_bw, firdes.WIN_HAMMING, 6.76)))
        self.airspyhf_source_1.set_sample_rate(self.samp_rate)

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
        self.freq_xlating_fir_filter_DEC_LP.set_taps((firdes.low_pass(1, self.samp_rate,( self.samp_rate_decimated/2)*0.5,self.transition_bw, firdes.WIN_HAMMING, 6.76)))

    def get_vec_len(self):
        return self.vec_len

    def set_vec_len(self, vec_len):
        self.vec_len = vec_len

    def get_transition_bw_fbank(self):
        return self.transition_bw_fbank

    def set_transition_bw_fbank(self, transition_bw_fbank):
        self.transition_bw_fbank = transition_bw_fbank

    def get_transition_bw(self):
        return self.transition_bw

    def set_transition_bw(self, transition_bw):
        self.transition_bw = transition_bw
        self.freq_xlating_fir_filter_DEC_LP.set_taps((firdes.low_pass(1, self.samp_rate,( self.samp_rate_decimated/2)*0.5,self.transition_bw, firdes.WIN_HAMMING, 6.76)))

    def get_samp_rate_0(self):
        return self.samp_rate_0

    def set_samp_rate_0(self, samp_rate_0):
        self.samp_rate_0 = samp_rate_0

    def get_cutoff_fbank(self):
        return self.cutoff_fbank

    def set_cutoff_fbank(self, cutoff_fbank):
        self.cutoff_fbank = cutoff_fbank

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

    def get_FIR_taps_matched_48(self):
        return self.FIR_taps_matched_48

    def set_FIR_taps_matched_48(self, FIR_taps_matched_48):
        self.FIR_taps_matched_48 = FIR_taps_matched_48

    def get_FIR_taps_matched_24(self):
        return self.FIR_taps_matched_24

    def set_FIR_taps_matched_24(self, FIR_taps_matched_24):
        self.FIR_taps_matched_24 = FIR_taps_matched_24


def main(top_block_cls=DATA_export, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
