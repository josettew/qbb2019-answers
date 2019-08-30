#!/usr/bin/env python3

import sys
import numpy as py
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import scipy

#FBtr0302347

df = pd.read_csv(sys.argv[1], sep = "\t", index_col = "t_name")
df2 = pd.read_csv(sys.argv[2], sep = "\t", index_col = 0, header = None) #histone.out files do not have header
df3 = pd.read_csv(sys.argv[3], sep = "\t", index_col = 0, header = None) #t_name is col 0
df4 = pd.read_csv(sys.argv[4], sep = "\t", index_col = 0, header = None)

histone_dict = {"FPKM" : df.loc[:,"FPKM"],
                "H3K4me1": df2.iloc[:,-1],  ##i to specify column
                "H3K4me3": df3.iloc[:,-1],
                "H3K9me3": df4.iloc[:,-1]}
                
histone_df = pd.DataFrame(histone_dict)
#print(histone_df)
model = sm.formula.ols(formula = "FPKM ~ H3K4me1 + H3K4me3 + H3K9me3", data = histone_df)
ols_result = model.fit()
#print(ols_result.resid)

fig, ax = plt.subplots()
ax.hist(ols_result.resid, bins = 50, density = True)
plt.title("Residuals Linear Regression")
ax.set_xlabel("Residual")
ax.set_ylabel("Frequency Count")
fig.savefig("hist_resid.png")
plt.close(fig)