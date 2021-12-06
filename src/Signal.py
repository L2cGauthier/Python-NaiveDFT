# -*- coding: utf-8 -*-
"""
Signal class
"""
import math
import matplotlib.pyplot as plt
    
# -----------------------------------------------------------------------------   
class Signal:

    def __init__(self, timeDomainSamples, sampleRate):
        """
        Represent a sampled signal
        Arguments:
            samplesInTimeDomain: a list of float representing the sampled signal
            sampleRate: the sampling rate in Hz
        Returns:
            A new instance of Signal
        """    
        self._samples = timeDomainSamples
        self._sampleRate = sampleRate
        self._numberOfSamples = len(self._samples)

    @property
    def SampleRate(self):
        return self._sampleRate
    
    @property
    def Samples(self):
        return self._samples
    
    @property
    def NumberOfSamples(self):
        return self._numberOfSamples
         
    
    def ShowTimeDomainGraph(self):
        """
        Print a Signal instance in the time domain
        """    
        xAxis = []
        for i in range(self.NumberOfSamples):
            xAxis.append(i / self.SampleRate)
        
        yAxis = self.Samples
            
        plt.plot(xAxis, yAxis)
        plt.xlabel("TIME")
        plt.ylabel("SIGNAL")
        plt.show()  
    
    @classmethod    
    def GetMockupCosSignal(cls, frequency, numberOfSamples, sampleRate):
        """
        Static function instantiating and returning a sampled cos signal
        Arguments:
            frequency: frequency of the mockup signal
            numberOfSamples: number of sampled values
            sampleRate: the sampling rate in Hz
        Returns:
            An instance of Signal representing a simple cos signal
        """    
        samplesInTimeDomain = []
        
        # Iteration over samples
        for i in range(numberOfSamples):
            
            time = i / sampleRate
            samplesInTimeDomain.append(math.cos(2 * math.pi * frequency * time))
            
        return Signal(samplesInTimeDomain, sampleRate)
    
    @classmethod    
    def GetMockupSinSignal(cls, frequency, numberOfSamples, sampleRate):
        """
        Static function instantiating and returning a sampled sin signal
        Arguments:
            frequency: frequency of the mockup signal
            numberOfSamples: number of sampled values
            sampleRate: the sampling rate in Hz
        Returns:
            An instance of Signal representing a simple sin signal
        """    
        samplesInTimeDomain = []
        
        # Iteration over samples
        for i in range(numberOfSamples):
            
            time = i / sampleRate
            samplesInTimeDomain.append(math.sin(2 * math.pi * frequency * time))
            
        return Signal(samplesInTimeDomain, sampleRate)
    
    @classmethod     
    def GetMockupStepSignal(cls, start, size, numberOfSamples, sampleRate):
        """
        Static function instantiating and returning a sampled step signal
        Arguments:
            start: time threshold where the signal goes from 0 to 1
            size: number of samples where signal = 1
            numberOfSamples: number of sampled values
            sampleRate: the sampling rate in Hz
        Returns:
            An instance of Signal representing a simple step
        """    
        samplesInTimeDomain = []
        
        # Iteration over samples
        for i in range(numberOfSamples):
            
            # If is in [start, start+size]
            if ((i /sampleRate ) > start and (i / sampleRate) < start + size):
                samplesInTimeDomain.append(1)
            else:
                 samplesInTimeDomain.append(0)    
                 
        return Signal(samplesInTimeDomain, sampleRate)
# -----------------------------------------------------------------------------    


    

    