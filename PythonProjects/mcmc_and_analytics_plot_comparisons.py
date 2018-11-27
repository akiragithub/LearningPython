# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 13:11:26 2018

Appication script for Advance Algorithmic trading 

@author: SuXess

This script compares MCMC algorithm (Metropolis) analyses results with a simple beta algorithm

"""

import matplotlib.pyplot as plt
import numpy as np
import pymc3
import scipy.stats as stats

plt.style.use("ggplot")

#Parameter values for prior and analytic posterior
alpha = 12
beta = 12
n = 50
z = 10
posterior_alpha = 22
posterior_beta = 52

#Plotting the analytic prior and posteriorn beta distribution
##Plotting the prior analytic
x = np.linspace(0,1,100)
y = stats.beta.pdf(x,alpha,beta) # y for the prior 
plt.plot(x,y,'--',label="prior",color="blue")

##Plotting the posterior analytic
y = stats.beta.pdf(x,posterior_alpha,posterior_beta)
plt.plot(x,y,label="posterior",color="green")

#Plotting the MCMC analytics
#Number of iterations of the metropolis algorithm to carry out for the MCMC
iterations = 100000

#use pyMC3 to construct a model
basic_model = pymc3.Model()

with basic_model :
    #Define the prior belief of the coin's fairness using the beta distribution
    tetha = pymc3.Beta("theta",alpha=alpha,beta=beta)

    #Define the Bernouilli likelihood function
    y = pymc3.Binomial("y", n=n,p=tetha,observed=z)
    
    #Carry out the MCMC analysis using the metropolis algorithm
    #Use the metropolis algorithm 
    #Using the Maximum A posteriori (MAP) optimisation for the first value for MCMC
    start = pymc3.find_MAP()
    #Defining the way to step
    step = pymc3.Metropolis()
    #Calculate the trace
    trace = pymc3.sample(iterations, step=step, start=start, random_seed=1, progressbar=True, cores=1) # if 
                        # variable cores not set to 1, leads to error
    #trace = pymc3.sample(2000, tune=1000, cores=1)
    
    #Plot the posterior from MCMC analysis
bins=50
#pymc3.summary(trace)
plt.hist(trace["theta"], bins, histtype="step", normed=True, label="Posterior (MCMC)", color="red")
    
#Update the graph labels
plt.legend(title="Parameters", loc="best")
plt.xlabel("$\\theta$, Fairness")
plt.ylabel("Density")
plt.show()

#Showing the trace plot
pymc3.traceplot(trace)
plt.show()    
