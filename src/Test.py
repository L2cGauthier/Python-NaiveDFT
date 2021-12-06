# -*- coding: utf-8 -*-
"""
Test class
"""

import NaiveDiscreteFourierTransform as NDFT
from Signal import Signal

# -----------------------------------------------------------------------------
if __name__ == "__main__":
    
    # ===== TEST 1: simple cos =====
    cosSignalFrequency = 10        # Hz
    cosSignalNumberOfSample = 320 
    cosSignalSampleRate = 120      # Hz
    
    mockupSignal = Signal.GetMockupCosSignal(cosSignalFrequency, cosSignalNumberOfSample, cosSignalSampleRate)
    mockupSignal.ShowTimeDomainGraph()
    
    transformer = NDFT.FourierTransformer(mockupSignal)
    transformer.GetGraph(graphType="AMPLITUDE").show()
    # ===============================

    # ===== TEST 1.1: simple sin =====
    sinSignalFrequency = 20        # Hz
    sinSignalNumberOfSample = 320 
    sinSignalSampleRate = 120      # Hz
    
    mockupSignal = Signal.GetMockupSinSignal(sinSignalFrequency, sinSignalNumberOfSample, sinSignalSampleRate)
    mockupSignal.ShowTimeDomainGraph()
    
    transformer = NDFT.FourierTransformer(mockupSignal)
    transformer.GetGraph(graphType="AMPLITUDE").show()
    # ===============================
    
    # ===== TEST 2: simple step =====
    stepStart = 0.5              # sec
    stepLength = 1               # sec
    setpNumberOfSamples = 200
    stepSampleRate = 100         # Hz
    
    mockupSignal = Signal.GetMockupStepSignal(stepStart, stepLength, setpNumberOfSamples, stepSampleRate)
    mockupSignal.ShowTimeDomainGraph()
    
    transformer = NDFT.FourierTransformer(mockupSignal)
    transformer.GetGraph(graphType="AMPLITUDE").show()
    # ===============================

# -----------------------------------------------------------------------------

