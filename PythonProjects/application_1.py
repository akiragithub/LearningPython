# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 07:54:03 2018

Appication script for Advance Algorithmic trading 

@author: SuXess

This script realizes different charts based on the beta distribution

"""
import numpy as np
from scipy.stats import beta
import matplotlib.pyplot as plt
import seaborn as sns

if __name__ == "__main__" :
    sns.set_palette("deep", desat=.6)
    sns.set_context(rc={"figure.figsize":(8, 4)})
    x = np.linspace(0,1,100)
    params = [
            (0.5, 0.5),
            (1, 1),
            (4, 3),
            (2, 5),
            (6, 6)   
            ]
    for p in params :
        y = beta.pdf(x, p[0],p[1])
        plt.plot(x, y, label="$\\alpha=%s$,$\\beta=%s$" % p)
    plt.xlabel("$\\theta$,fairness")
    plt.ylabel("density")
    plt.legend(title="Parameters")
    plt.show()
