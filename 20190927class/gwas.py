#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt
import os
import numpy as np


colors = ['#42D4F4', '#911EB4']

for file_name in os.listdir(os.getcwd()):
    if file_name.endswith("qassoc"):
        qassoc_file = open(file_name)
        manhattan = {}
        for i, line in enumerate(qassoc_file):
            if i == 0:
                continue
            fields = line.rstrip("\n").split()
            chromosome = fields[0]
            p_value = fields[-1]
            if p_value == "NA":
                continue
            manhattan.setdefault(chromosome, [])
            manhattan[chromosome].append(-1*np.log10(float(p_value)))
        fig, ax = plt.subplots()
        previous_points = 0
        for i, chromosome in enumerate(manhattan):
            ax.scatter( [x+previous_points for x in range(len(manhattan[chromosome]))],manhattan[chromosome], color = colors[i%2])
            previous_points += len(manhattan[chromosome])
        plt.tick_params(axis='x',which='both',bottom=False,top=False,labelbottom=False)
        plt.xlabel("chromosomes")
        plt.ylabel("log-10 pvalue")
        plt.title(file_name)
        fig.savefig(file_name + '.png')
        plt.close(fig)
    
        

        
        
        
        