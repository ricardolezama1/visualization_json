# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

import numpy as np


def plot_terms_body(topic, data, minimum_frequency):
    """
    The np.aranage attribute is to understand how to best and programmatically 
    plot the data. Intervals are determined by the counts within the dictionary. 
    The user does not need to predefine the graph. Instead, the second line takes the 
    frequency.
    Args: Topic is the name of the plot/category. The 'data' is  a dictionary. 
    
    No object returned. However, plot is automatically generated.
    """
    #The bar plot should be optimized for the max and min size of
    filter_ones = {term:frequency for term, frequency in data.items() if frequency > minimum_frequency}  
    filtered = {term:frequency for term, frequency in data.items() if frequency > round(sum(filter_ones.values())/len(filter_ones))  }   
    print(round(sum(filtered.values())/len(filtered)), "Average count as result of total terms minus once identified terms divided by all terms.")
    terms = filtered.keys()
    frequency = filtered.values()   
    y_pos = np.arange(len(terms),step=1)
    # min dictionary value, max filtered value ; 
    x_pos = np.arange(min(filtered.values()), max(filtered.values()), step=round(sum(filtered.values())/len(filtered)))
    plt.barh(y_pos, frequency, align='center', alpha=1)
    plt.yticks(y_pos, terms, fontsize=12)
    plt.xticks(x_pos)
    plt.xlabel('Frecuencia en encabezados')
    plt.title(str(topic), fontsize=14)
    plt.tight_layout()
    plt.show()
