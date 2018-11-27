# -*- coding: utf-8 -*-
"""
Appication script for Advance Algorithmic trading 

Created on Wed Nov  7 09:14:12 2018

@author: akira

This scripts simulates some bernouillis experiences and adjust it with the bayesian statistics
before printing as a char;
it does not require any parameter

"""

import numpy as np
from scipy import stats
from matplotlib import pyplot

if __name__ == "__main__" :
    
    # Creating a list containing the number of trials; (each trial is a bernouilli trial)
    number_of_trial = [0,2,10,20,50,500]
    # Initialize an experience consisting of 500 trials
    data = stats.bernoulli.rvs(0.5,size = number_of_trial[-1])
    # Discretize the x axis into 100 separate values
    x = np.linspace(0,1,100)
    # Launch the experimentation
    for i,N in enumerate(number_of_trial):
        #Accumulating the number of heads for the current element of number_of_trial
        heads = data[:N].sum()
        #Create an axis subplot for each update
        ax = pyplot.subplot(len(number_of_trial)/2,2,i+1)
        ax.set_title("%s trials,%s heads"%(N,heads))
        #Adding labels to axis and hiding labels on Y-Axis
        pyplot.xlabel("$(PH)$, Probability of heads")
        pyplot.ylabel("Density")
        #Formatting output for the first experimentation : ie i = 0
        if i == 0:
            pyplot.ylim([0.0,2.0])
            
        pyplot.setp(ax.get_yticklabels(), visible = False)
        #Create a beta distribution to represent the experimentation
        y = stats.beta.pdf(x, heads + 1 , 1+ N - heads)
        #plot it
        pyplot.plot(x,y,label = "Observe %d tosses, \n %d heads"%(N,heads))
        pyplot.fill_between(x, 0, y, color="#aaaadd", alpha=0.5)
    #expand plot to cover the allocated screen and show it
    pyplot.tight_layout()
    pyplot.show()
