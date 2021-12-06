# -*- coding: utf-8 -*-
"""
Naive Discrete Fourier Transformer
"""

import math
import enum
import matplotlib.pyplot as plt

from Utils.ConversionUtils import ConversionUtils
    
# -----------------------------------------------------------------------------   
class FourierTransformer:
    def __init__(self, signalInstance):
        
        self._signalInstance = signalInstance
        
        # Lazy initialized properties
        self._fourierTransform = None
        self._fourierTransformAmplitudes = None
        self._fourierTransformAmplitudesIndB = None
        self._fourierTransformPhases = None
        self._fourierTransformFrequencies = None
        
    @property
    def Signal(self):
        return self._signalInstance
    
    @property
    def Transform(self):
        """
        Lazy-initialized property containing the Fourier transform as a list of complex numbers
        """   
        
        if (self._fourierTransform == None):
            self._fourierTransform = self.__GetFourierTransform()
        
        return self._fourierTransform
    
    @property
    def TransformAmplitudes(self):
        """
        Lazy-initialized property containing the Fourier transform's amplitudes
        """   
        if (self._fourierTransformAmplitudes == None):
            self._fourierTransformAmplitudes = self.__GetFourierTransformAmplitudes()
        
        return self._fourierTransformAmplitudes
    
    @property
    def TransformAmplitudesIndB(self):
        """
        Lazy-initialized property containing the Fourier transform's amplitudes in dB
        """   
        if (self._fourierTransformAmplitudesIndB == None):
            self._fourierTransformAmplitudesIndB = self.__GetFourierTransformAmplitudesIndB()
            
        return self._fourierTransformAmplitudesIndB
    
    @property
    def TransformPhases(self):
        """
        Lazy-initialized property containing the Fourier transform's phases in deg
        """
        if (self._fourierTransformPhases == None):
            self._fourierTransformPhases = self.__GetFourierTransformPhases()
        
        return self._fourierTransformPhases
    
    @property
    def TransformFrequencies(self):
        """
        Lazy-initialized property containing the Fourier transform's frequencies
        """
        if (self._fourierTransformFrequencies == None):
            self._fourierTransformFrequencies = self.__GetFourierTransformFrequencies()
        
        return self._fourierTransformFrequencies
    
    
    def __GetFourierTransform(self):
        
        fourierTransform = []
        timeDomainSamples = self.Signal.Samples
        numberOfSamples = self.Signal.NumberOfSamples
        
        # Iteration on frequencies
        for k in range(numberOfSamples):
            
            transformedSample = complex(0.0, 0.0)
            
            # Iteration on samples
            for n in range(numberOfSamples):
                
                realPart = math.cos(-2 * math.pi * k * n / numberOfSamples)
                imaginaryPart = math.sin(-2 * math.pi * k * n / numberOfSamples)
                
                transformedSample += timeDomainSamples[n] * complex(realPart, imaginaryPart)
            
            fourierTransform.append(transformedSample)
            
        return fourierTransform
    
    
    def __GetFourierTransformAmplitudes(self):
        
        amplitudes = []
        numberOfSamples = self.Signal.NumberOfSamples
        
        for i in range(numberOfSamples):
            amplitudes.append(math.sqrt(math.pow(self.Transform[abs(i)].real, 2) + math.pow(self.Transform[abs(i)].imag,2)))
        
        return amplitudes
    
    
    def __GetFourierTransformAmplitudesIndB(self):
        
        numberOfSamples = self.Signal.NumberOfSamples
        amplitudesIndB = []
        
        for i in range(numberOfSamples):
            amplitudesIndB.append(ConversionUtils.AmplitudeTodB(self.TransformAmplitudes[i]))
        
        return amplitudesIndB
    
    def __GetFourierTransformPhases(self):
        
        numberOfSamples = self.Signal.NumberOfSamples
        phasesInDeg = []
        
        for i in range(numberOfSamples):
            phasesInDeg.append(math.atan(self.Transform[i].imag / self.Transform[i].real) * 180.0 / math.pi)
        
        return phasesInDeg
    
    def __GetFourierTransformFrequencies(self):
        
        numberOfSamples = self.Signal.NumberOfSamples
        sampleRate = self.Signal.SampleRate
        frequencies = []
        
        for i in range(numberOfSamples):
            frequencies.append(i * sampleRate / numberOfSamples)
        
        return frequencies

    
    def GetGraph(self, graphType = "AMPLITUDE"):
        """
        Show and return a graph of the fourier transform amplitude of the signal instance
        the transformer's constructor was called.
        
        Arguments:
            graphType: can be "AMPLITUDE", "AMPLITUDE_DB" or "PHASE"
        """
        
        numberOfSamples = self.Signal.NumberOfSamples
        sampleRate = self.Signal.SampleRate
        collectionToPlot = None
        
        if(graphType == "AMPLITUDE"):
            collectionToPlot = self.TransformAmplitudes
        elif(graphType == "AMPLITUDE_DB"):
            collectionToPlot = self.TransformAmplitudesIndB
        elif(graphType == "PHASE"):
            collectionToPlot = self.TransformPhases
        else:
            raise Exception("graphType must be 'AMPLITUDE', 'AMPLITUDE_DB' or 'PHASE', it cannot be", graphType);
        
        xAxis = []
        yAxis = []
        
        # The transform is perdiodical, for representation purpose, we plot it in ]-sampleRate/2, sampleRate/2]
        for i in range(-math.floor(numberOfSamples / 2), math.floor(numberOfSamples / 2) + 1):
            
            xAxis.append(i * sampleRate / numberOfSamples)
            yAxis.append(collectionToPlot[abs(i)])

        plt.figure(figsize=(12.8,9.6))
        plt.plot(xAxis, yAxis)
        plt.xlabel(graphType)
        plt.ylabel("AMPLITUDE")
        
        return plt
    
# ----------------------------------------------------------------------------- 