# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 13:34:32 2018
@author: SuXess

This script displays a random dataset using a noisy linear process

"""

import numpy as np
import pandas as pd
import seaborn as sns
import pymc3 as pm

def simulate_linear_data(N,beta_0,beta_1,eps_sigma_sq):
    
    """
    Simulate a random dataset using a noisy linbear procvess
    N: number of points to generate
    beta_0: The intercept
    beta_1: The slope of univariante predictor,X
    eps_sigma_sq: The square of the standard deviation ie the variance
    
    """

    # Create a pandas Dataframe containing N uniformely sampled values from 0.0 to 1.0
    
    df = pd.DataFrame(
            {
            'x':
                np.random.RandomState(42).choice(
                        map(
                                lambda x: float(x)/100.0, 
                                np.arange(100)
                                ), N, replace=False
                        )
            }
    )
    
    # Use a linear model (y~beta_0 + beta_1x + epsilon) to column "y" of responses based on 'x'
    
    eps_mean = 0.0
    df["y"] = beta_0 + beta_1*df["x"] + np.random.RandomState(42).normal(eps_mean, eps_sigma_sq, N)
    return df

def glm_mcmc_inference(df, iterations=5000):
    """
    Calculates the Markov Chain Monte Carlo trace of a generalised linear model bayesian linear regression model on a supplied data
    df: DataFrame containing the supplied data
    iterations: number of iterations to carry out MCMC for
    """
    
    # Use pymc3 to construct a model context
    basic_model = pm.Model()
    with basic_model :
        # Create a generalised linear model (glm) according to df
        # Use the normal family distribution for the likelihood
        pm.glm.GLM.from_formula('y ~ x', df, family=pm.glm.families.Normal())
        # Use Maximum A Posteori (MAP) as initial value for MCMC
        start = pm.find_MAP()
        # Setting the steps with the No-U-Turn Sampler algorithm
        step = pm.NUTS()
        # Calculate the trace
        trace = pm.sample(iterations, step, start, random_seed=42, progressbar=True, cores=1)
    return trace
        

if __name__=="__main__" :
    #Setting or parameters
    beta_0 = 1.0
    beta_1 = 2.0
    #Simulate 100 points with a variance of 0.5
    N = 100
    eps_sigma_sq = 0.5
    #Simulate the linear noisy data
    simulate_linear_data(N,beta_0,beta_1,eps_sigma_sq)
    #plot the data and a frequentist linear regression fit 
    sns.lmplot(x="x", y="y", data=df, size=10)
    plt.xlim(0.0, 1.0)
    
    trace = glm_mcmc_inference(df, iterations=5000)
    pm.traceplot(trace[500:])
    plt.show()
    
    # Plot a sample of posterior regression lines
    sns.lmplot(x="x", y="y", data=df, size=10, fit_reg=False)
    plt.xlim(0.0,1.0)
    plt.ylim(0.0,4.0)
    pm.plot_posterior_predictive_glm
    
    
    
    
    