#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Dsp New
# Generated: Thu Jan 17 15:30:51 2019
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

from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import osmosdr
import time
import wx


class DSP_new(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Dsp New")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 768000
        self.decim_total = decim_total = 200
        self.samp_rate_decimated = samp_rate_decimated = samp_rate/decim_total
        self.transition_bw = transition_bw = samp_rate_decimated/4
        self.vect_size = vect_size = 1
        self.center_freq = center_freq = 457e3
        self.Xlating_fir_taps = Xlating_fir_taps = firdes.low_pass(1, samp_rate, samp_rate_decimated*0.5,transition_bw, firdes.WIN_HAMMING, 6.76)

        ##################################################
        # Blocks
        ##################################################
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_c(
        	self.GetWin(),
        	baseband_freq=0,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate/decim_total,
        	fft_size=512,
        	fft_rate=25,
        	average=False,
        	avg_alpha=None,
        	title='FFT',
        	peak_hold=False,
        )
        self.Add(self.wxgui_fftsink2_0.win)
        self.freq_xlating_fir_filter_xxx_0 = filter.freq_xlating_fir_filter_ccc(decim_total, (Xlating_fir_taps), 0, samp_rate)
        self.airspyhf_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + 'airspyhf=0' )
        self.airspyhf_source_0.set_sample_rate(samp_rate)
        self.airspyhf_source_0.set_center_freq(center_freq, 0)
        self.airspyhf_source_0.set_freq_corr(0, 0)
        self.airspyhf_source_0.set_iq_balance_mode(0, 0)
        self.airspyhf_source_0.set_gain_mode(False, 0)
        self.airspyhf_source_0.set_gain(6, "LNA", 0)
        self.airspyhf_source_0.set_gain(0, "ATT", 0)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.airspyhf_source_0, 0), (self.freq_xlating_fir_filter_xxx_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.wxgui_fftsink2_0, 0))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_Xlating_fir_taps(firdes.low_pass(1, self.samp_rate, self.samp_rate_decimated*0.5,self.transition_bw, firdes.WIN_HAMMING, 6.76))
        self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate/self.decim_total)
        self.set_samp_rate_decimated(self.samp_rate/self.decim_total)
        self.airspyhf_source_0.set_sample_rate(self.samp_rate)

    def get_decim_total(self):
        return self.decim_total

    def set_decim_total(self, decim_total):
        self.decim_total = decim_total
        self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate/self.decim_total)
        self.set_samp_rate_decimated(self.samp_rate/self.decim_total)

    def get_samp_rate_decimated(self):
        return self.samp_rate_decimated

    def set_samp_rate_decimated(self, samp_rate_decimated):
        self.samp_rate_decimated = samp_rate_decimated
        self.set_Xlating_fir_taps(firdes.low_pass(1, self.samp_rate, self.samp_rate_decimated*0.5,self.transition_bw, firdes.WIN_HAMMING, 6.76))
        self.set_transition_bw(self.samp_rate_decimated/4)

    def get_transition_bw(self):
        return self.transition_bw

    def set_transition_bw(self, transition_bw):
        self.transition_bw = transition_bw
        self.set_Xlating_fir_taps(firdes.low_pass(1, self.samp_rate, self.samp_rate_decimated*0.5,self.transition_bw, firdes.WIN_HAMMING, 6.76))

    def get_vect_size(self):
        return self.vect_size

    def set_vect_size(self, vect_size):
        self.vect_size = vect_size

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq
        self.airspyhf_source_0.set_center_freq(self.center_freq, 0)

    def get_Xlating_fir_taps(self):
        return self.Xlating_fir_taps

    def set_Xlating_fir_taps(self, Xlating_fir_taps):
        self.Xlating_fir_taps = Xlating_fir_taps
        self.freq_xlating_fir_filter_xxx_0.set_taps((self.Xlating_fir_taps))


def main(top_block_cls=DSP_new, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
