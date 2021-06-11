# -*- coding: utf-8 -*-
"""
Created on Fri May  7 15:21:57 2021

@author: ericj
"""

import numpy as np
import matplotlib.pyplot as plt
import csv
def PieChart():
    total_saving_amt = 0
    total_checking_amt = 0
    with open('savings.csv', 'r') as csvfile:
        checkings_reader = csv.reader(csvfile, delimiter=',')
        for i in checkings_reader:
            saving_amt = float(i[4])
            total_saving_amt += saving_amt
                
    with open('checkings.csv', 'r') as csvfile:
        checkings_reader = csv.reader(csvfile, delimiter=',')
        for i in checkings_reader:
            checking_amt = float(i[4])  
            total_checking_amt += checking_amt
    # Creating dataset
    states = ['Savings', 'Checkings']
    data = [total_saving_amt, total_checking_amt]
    # Creating explode dat
    explode = (0.1, 0.3) 
    # Creating color parameters
    colors = ( "orange", "cyan")
    # Wedge properties
    wp = { 'linewidth' : 1, 'edgecolor' : "black" }
    
    fig, ax = plt.subplots(figsize =(10, 7))
    wedges, texts, autotexts = ax.pie(data, 
                                  autopct = lambda pct: func(pct, data),
                                  explode = explode, 
                                  labels = states,
                                  shadow = True,
                                  colors = colors,
                                  startangle = 90,
                                  wedgeprops = wp,
                                  textprops = dict(color ="black"))
# Adding legend
    ax.legend(wedges, states,
          title ="Account Types:",
          loc ="center left",
          bbox_to_anchor =(1, 0, 0.5, 1))
    plt.setp(autotexts, size = 8, weight ="bold")
    title = ('Total Amount: Savings vs Checkings')
    ax.set_title(title)
    # show plot
    plt.show()
    # Creating autocpt arguments
    
def func(pct, allvalues):
    absolute = int(pct / 100.*np.sum(allvalues))
    return "{:.1f}%\n({:d} T)".format(pct, absolute)
















