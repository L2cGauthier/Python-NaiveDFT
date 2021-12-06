# -*- coding: utf-8 -*-
"""
ConversionUtils
"""

import math

class ConversionUtils:
    
    @classmethod
    def AmplitudeTodB(cls, amplitude):
        return 20.0 * math.log10(amplitude)
    
    @classmethod
    def dBToAmplitude(cls, dB):
        return math.pow(10.0, dB / 20.0)
    