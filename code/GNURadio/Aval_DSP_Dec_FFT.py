#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Aval Dsp Dec Fft
# Generated: Wed Jan 16 15:43:16 2019
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
from gnuradio import fft
from gnuradio import filter
from gnuradio import gr
from gnuradio import zeromq
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import osmosdr
import time
import wx


class Aval_DSP_Dec_FFT(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Aval Dsp Dec Fft")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 768000
        self.decim_total = decim_total = 800*2*2
        self.samp_rate_decimated = samp_rate_decimated = samp_rate/decim_total
        self.transition_bw = transition_bw = samp_rate_decimated/4
        self.decimation2 = decimation2 = 20
        self.decimation1 = decimation1 = 10
        self.center_freq = center_freq = 457e3
        self.calibration = calibration = 0.0225
        self.FFT_size = FFT_size = samp_rate_decimated/30

        ##################################################
        # Blocks
        ##################################################
        self.zeromq_push_sink_0_0 = zeromq.push_sink(gr.sizeof_float, FFT_size, "tcp://127.0.0.1:5556", 100, False, -1)
        self.zeromq_push_sink_0 = zeromq.push_sink(gr.sizeof_float, FFT_size, "tcp://127.0.0.1:5555", 100, False, -1)
        self.freq_xlating_fir_filter_xxx_0_0_0 = filter.freq_xlating_fir_filter_ccc(decim_total, (firdes.low_pass(1, samp_rate, samp_rate_decimated*0.5,transition_bw, firdes.WIN_HAMMING, 6.76)), 0, samp_rate)
        self.freq_xlating_fir_filter_xxx_0_0 = filter.freq_xlating_fir_filter_ccc(decim_total, (firdes.low_pass(1, samp_rate, samp_rate_decimated*0.5,transition_bw, firdes.WIN_HAMMING, 6.76)), 0, samp_rate)
        self.fft_vxx_1_0_0 = fft.fft_vcc(FFT_size, True, (window.rectangular(8)), True, 1)
        self.fft_vxx_1_0 = fft.fft_vcc(FFT_size, True, (window.rectangular(8)), True, 1)
        self.blocks_vector_to_stream_0_0 = blocks.vector_to_stream(gr.sizeof_float*1, FFT_size)
        self.blocks_vector_to_stream_0 = blocks.vector_to_stream(gr.sizeof_float*1, FFT_size)
        self.blocks_stream_to_vector_1_0 = blocks.stream_to_vector(gr.sizeof_float*1, FFT_size)
        self.blocks_stream_to_vector_1 = blocks.stream_to_vector(gr.sizeof_float*1, FFT_size)
        self.blocks_stream_to_vector_0_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, FFT_size)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, FFT_size)
        self.blocks_multiply_const_xx_0_0 = blocks.multiply_const_ff(calibration)
        self.blocks_multiply_const_xx_0 = blocks.multiply_const_ff(calibration)
        self.blocks_complex_to_mag_squared_1_0_0 = blocks.complex_to_mag_squared(FFT_size)
        self.blocks_complex_to_mag_squared_1_0 = blocks.complex_to_mag_squared(FFT_size)
        self.airspyhf_source_0_0 = osmosdr.source( args="numchan=" + str(1) + " " + 'airspyhf=C852D65D9DBF34DD' )
        self.airspyhf_source_0_0.set_sample_rate(samp_rate)
        self.airspyhf_source_0_0.set_center_freq(457000, 0)
        self.airspyhf_source_0_0.set_freq_corr(0, 0)
        self.airspyhf_source_0_0.set_iq_balance_mode(0, 0)
        self.airspyhf_source_0_0.set_gain_mode(False, 0)
        self.airspyhf_source_0_0.set_gain(0, "LNA", 0)
        self.airspyhf_source_0_0.set_gain(0, "ATT", 0)

        self.airspyhf_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + 'airspyhf=C852A98040343FD2' )
        self.airspyhf_source_0.set_sample_rate(samp_rate)
        self.airspyhf_source_0.set_center_freq(457000, 0)
        self.airspyhf_source_0.set_freq_corr(0, 0)
        self.airspyhf_source_0.set_iq_balance_mode(0, 0)
        self.airspyhf_source_0.set_gain_mode(False, 0)
        self.airspyhf_source_0.set_gain(0, "LNA", 0)
        self.airspyhf_source_0.set_gain(0, "ATT", 0)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.airspyhf_source_0, 0), (self.freq_xlating_fir_filter_xxx_0_0, 0))
        self.connect((self.airspyhf_source_0_0, 0), (self.freq_xlating_fir_filter_xxx_0_0_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_1_0, 0), (self.blocks_vector_to_stream_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_1_0_0, 0), (self.blocks_vector_to_stream_0_0, 0))
        self.connect((self.blocks_multiply_const_xx_0, 0), (self.blocks_stream_to_vector_1, 0))
        self.connect((self.blocks_multiply_const_xx_0_0, 0), (self.blocks_stream_to_vector_1_0, 0))
        self.connect((self.blocks_stream_to_vector_0, 0), (self.fft_vxx_1_0, 0))
        self.connect((self.blocks_stream_to_vector_0_0, 0), (self.fft_vxx_1_0_0, 0))
        self.connect((self.blocks_stream_to_vector_1, 0), (self.zeromq_push_sink_0, 0))
        self.connect((self.blocks_stream_to_vector_1_0, 0), (self.zeromq_push_sink_0_0, 0))
        self.connect((self.blocks_vector_to_stream_0, 0), (self.blocks_multiply_const_xx_0, 0))
        self.connect((self.blocks_vector_to_stream_0_0, 0), (self.blocks_multiply_const_xx_0_0, 0))
        self.connect((self.fft_vxx_1_0, 0), (self.blocks_complex_to_mag_squared_1_0, 0))
        self.connect((self.fft_vxx_1_0_0, 0), (self.blocks_complex_to_mag_squared_1_0_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0_0, 0), (self.blocks_stream_to_vector_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0_0_0, 0), (self.blocks_stream_to_vector_0_0, 0))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_samp_rate_decimated(self.samp_rate/self.decim_total)
        self.freq_xlating_fir_filter_xxx_0_0_0.set_taps((firdes.low_pass(1, self.samp_rate, self.samp_rate_decimated*0.5,self.transition_bw, firdes.WIN_HAMMING, 6.76)))
        self.freq_xlating_fir_filter_xxx_0_0.set_taps((firdes.low_pass(1, self.samp_rate, self.samp_rate_decimated*0.5,self.transition_bw, firdes.WIN_HAMMING, 6.76)))
        self.airspyhf_source_0_0.set_sample_rate(self.samp_rate)
        self.airspyhf_source_0.set_sample_rate(self.samp_rate)

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
        self.set_FFT_size(self.samp_rate_decimated/30)
        self.freq_xlating_fir_filter_xxx_0_0_0.set_taps((firdes.low_pass(1, self.samp_rate, self.samp_rate_decimated*0.5,self.transition_bw, firdes.WIN_HAMMING, 6.76)))
        self.freq_xlating_fir_filter_xxx_0_0.set_taps((firdes.low_pass(1, self.samp_rate, self.samp_rate_decimated*0.5,self.transition_bw, firdes.WIN_HAMMING, 6.76)))

    def get_transition_bw(self):
        return self.transition_bw

    def set_transition_bw(self, transition_bw):
        self.transition_bw = transition_bw
        self.freq_xlating_fir_filter_xxx_0_0_0.set_taps((firdes.low_pass(1, self.samp_rate, self.samp_rate_decimated*0.5,self.transition_bw, firdes.WIN_HAMMING, 6.76)))
        self.freq_xlating_fir_filter_xxx_0_0.set_taps((firdes.low_pass(1, self.samp_rate, self.samp_rate_decimated*0.5,self.transition_bw, firdes.WIN_HAMMING, 6.76)))

    def get_decimation2(self):
        return self.decimation2

    def set_decimation2(self, decimation2):
        self.decimation2 = decimation2

    def get_decimation1(self):
        return self.decimation1

    def set_decimation1(self, decimation1):
        self.decimation1 = decimation1

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq

    def get_calibration(self):
        return self.calibration

    def set_calibration(self, calibration):
        self.calibration = calibration
        self.blocks_multiply_const_xx_0_0.set_k(self.calibration)
        self.blocks_multiply_const_xx_0.set_k(self.calibration)

    def get_FFT_size(self):
        return self.FFT_size

    def set_FFT_size(self, FFT_size):
        self.FFT_size = FFT_size


def main(top_block_cls=Aval_DSP_Dec_FFT, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
