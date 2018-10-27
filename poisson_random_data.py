# -*- coding: utf-8 -*-
"""
@author: vamsi
"""

import numpy as np
import matplotlib.pyplot as plt
import random

mean = 10
no_of_samples = 1000
def GeneratePoissonSamples():
    dataPoisson = np.random.poisson(mean, no_of_samples)
    PlotHistogram(dataPoisson)
    np.mean(dataPoisson)
    SampleHundredData(dataPoisson)

def PlotHistogram(dataPoisson):
    count, bins, ignored =  plt.hist(dataPoisson, 14, normed = True)
    plt.show()

def SampleHundredData(dataPoisson):
    extract_hundred = []
    for i in range(100):
        extract_hundred.append(random.choice(dataPoisson))
    
    np.mean(extract_hundred)
    
#for j in range(3):
    GeneratePoissonSamples()
    
    
"""
Poisson Distribution is used to know the probability of occurance of an event
in a given time period. We can see from histogram, the average number of success 
that can occur in a specified region.
"""

