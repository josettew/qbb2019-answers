#!/usr/bin/env python3 

import sys
import numpy as py
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import scipy
from sklearn.decomposition import PCA


ctab = pd.read_csv(sys.argv[1], sep = "\t")
all_start_end_values = ctab.loc[:,["chr", "strand", "t_name", "start", "end"]]


print("Chr" + "\t" + "t_name" + "\t" + "promoter start" + "\t" + "promoter end") #labels
for index, row in all_start_end_values.iterrows(): #iterate thru rows of data frame
   if row.loc["strand"] == "+":
       promoterStart = int(row.loc["start"])
       promoter_start_plus_500 = promoterStart + 500
       promoter_start_minus_500 = promoterStart - 500
       print(str(row.loc["chr"]) + "\t" + str(row.loc["t_name"]) + "\t" + str(promoter_start_minus_500) + "\t" + str( promoter_start_plus_500))
   elif row.loc["strand"] == "-":
       promoterStart = int(row.loc["end"])
       promoter_start_plus_500 = promoterStart + 500
       promoter_start_minus_500 = promoterStart - 500
       print(str(row.loc["chr"]) + "\t" + str(row.loc["t_name"]) + "\t" + str(promoter_start_minus_500) + "\t" + str( promoter_start_plus_500))