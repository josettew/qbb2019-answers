#!/usr/bin/env python3

"""
Usage: ./01-boxplot.py <gene_name> <FPKMs.csv>
Boxplot all trnascripts for a given gene
"""
## input:  ./01-boxplot1.py Sxl all.csv 

import sys
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import pandas as pd

gene_name = sys.argv[1]
fpkm_file = sys.argv[2]
# by indexing the t_name columns we are making it the row name, no longer a column
df = pd.read_csv(fpkm_file, index_col = "t_name")
# list of trues and falses (25 trues=# of columns)
goi = df.loc[:,"gene_names"] == gene_name
#valus that we want to boxplot
fpkms = df.drop( columns = "gene_names")

filtered_fpkms = fpkms.loc[goi,:]

#list comprehesion - make list out of another list
male_ids = [y for y in list(filtered_fpkms) if y.startswith('male')]
male_transcripts = np.log2(filtered_fpkms[male_ids] + 0.001)
# again for females
female_ids = [x for x in list(filtered_fpkms) if x.startswith('female')]
female_transcripts = np.log2(filtered_fpkms[female_ids] + 0.001)

male_x_axis = [j[5:]for j in male_ids]
female_x_axis = [q[7:] for q in female_ids]

fig, (ax1, ax2) = plt.subplots(nrows = 2)
# # .T is for transpose
ax1.boxplot(male_transcripts.T)
ax2.boxplot(female_transcripts.T)
ax1.set_title("Homework Exercise 1-Sxl Males")
ax1.set_xlabel("Embryonic stage")
ax1.set_xticklabels(male_x_axis)
ax1.set_ylabel("Transcripts")
ax2.set_title("Homework Exercise 1-Sxl Females")
ax2.set_xlabel("Embryonic stage")
ax2.set_xticklabels(female_x_axis)
ax2.set_ylabel("Transcripts")
plt.tight_layout()
fig.savefig("boxplot.png")
plt.close(fig)