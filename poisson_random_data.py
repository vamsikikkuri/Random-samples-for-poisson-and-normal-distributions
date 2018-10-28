# -*- coding: utf-8 -*-
"""
@author: vamsi
"""

import numpy as np
import matplotlib.pyplot as plt
import random
from scipy.special import factorial


mean = 10
no_of_samples = 1000
def GeneratePoissonSamples():
    dataPoisson = np.random.poisson(mean, no_of_samples)
    PlotHistogram(dataPoisson)
    np.mean(dataPoisson)
    SampleHundredData(dataPoisson)


def PlotHistogram(dataPoisson):
    count, bins, ignored =  plt.hist(dataPoisson, 14, normed = True)
    plt.plot(bins, np.exp(-mean)*np.power(mean, bins)/factorial(bins), linewidth = 3, color = 'green')
    plt.title('Poisson Distribution for random samples(1000) with mean = 10')
    plt.show()

def PlotHistogramForExtractedHundred(extract_hundred):
    count, bins, ignored =  plt.hist(extract_hundred, 14, normed = True)
    plt.plot(bins, np.exp(-mean)*np.power(mean, bins)/factorial(bins), linewidth = 3, color = 'green')
    plt.title('Poisson Distribution for extracted samples from the 1000 samples above with mean = 10')
    plt.show()
    
def SampleHundredData(dataPoisson):
    extract_hundred = []
    for i in range(100):
        extract_hundred.append(random.choice(dataPoisson))
    
    PlotHistogramForExtractedHundred(extract_hundred)
    np.mean(extract_hundred)
    
GeneratePoissonSamples()

    
"""
Poisson Distribution is used to know the probability of occurance of an event
in a given time period. We can see from histogram, the average number of success 
that can occur in a specified region.
"""

