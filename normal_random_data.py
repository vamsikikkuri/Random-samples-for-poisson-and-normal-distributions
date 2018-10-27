# -*- coding: utf-8 -*-
"""
@author: vamsi
"""

import numpy as np
import matplotlib.pyplot as plt
import random
mean = 0
sd = 0.1
no_of_samples = 1000
def GenerateNormalSamples():
    dataNormal = np.random.normal(mean, sd, no_of_samples)
    PlotHistogram(dataNormal)
    np.mean(dataNormal)
    SampleHundredData(dataNormal)

def PlotHistogram(dataNormal):
    count, bins, ignored = plt.hist(dataNormal, 14, density = True)
    plt.plot(bins, 1/(sd * np.sqrt(2 * np.pi)) * np.exp(- (bins - mean)**2/(2 * sd**2)), linewidth = 3, color = 'green')
    plt.show()
    
def SampleHundredData(dataNormal):
    extract_hundred = []
    for i in range(100):
        extract_hundred.append(random.choice(dataNormal))
        
        np.mean(extract_hundred)

GenerateNormalSamples()    

"""
If we observe the histograms plotted for the random data in normal form we can see that most of the data
comes under the curve. This shows few properties of Normal Distribution which are, most of the area will
be under 2 standard deviations of the mean that is approximately 95%. We can also see that the graph plotted 
has a bell shaped curve with almost symmetric on both sides. And also the graphs are denser at center and 
much less dense at the edges. 
"""