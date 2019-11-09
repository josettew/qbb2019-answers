#!/usr/bin/env python3

"""From .txt file to make an array of the data for numpy to generate heat map and compare gene expression"""

import sys
import numpy as np
import matplotlib.pylab as plt 
import scipy
import seaborn as sns  
import pandas as pd 
from scipy.cluster.hierarchy import dendrogram, linkage,leaves_list



data = pd.read_csv(sys.argv[1], sep = "\t", header = 0, index_col = "gene")

#Methods 'centroid', 'median' and 'ward' 
linkage_1 = linkage(data, method = 'average')

leaves_list_1 = leaves_list(linkage_1)
#pass Z to leaves list

new_data = data.iloc[leaves_list_1]

#Then transpose
sorted_new_data = new_data.transpose()
linkage2 = linkage(sorted_new_data, method = 'average')
leaves2 = leaves_list(linkage2)
#Then linkage, leaves list

#reorganize
finished_data = sorted_new_data.iloc[leaves2]
finished = finished_data.transpose()

#print(data)
sns.heatmap(finished)
plt.savefig("heatmap.png")
plt.close()

fig = plt.figure
label_list = ["CFU", "poly", "unk", "int", "mys", "mid"]
labels = np.array(label_list)
sort_label = labels[leaves2]


ax1 = dendrogram(linkage2, labels = sort_label)
plt.savefig("Dendrogram.png")
plt.close()


cfu = data["CFU"].values
poly = data["poly"].values
int1 = data["int"].values
unk = data["unk"].values

from pandas import DataFrame
from sklearn.cluster import KMeans

Data = {'x':cfu,
        'y': poly
       }
  
df = DataFrame(Data,columns=['x','y'])
#print (df)

kmeans = KMeans(n_clusters=5).fit(df)
centroids = kmeans.cluster_centers_


plt.scatter(df['x'], df['y'], c= kmeans.labels_.astype(float), s=50, alpha=0.5)
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50)
plt.xlabel("CFU")
plt.ylabel("poly")
plt.savefig("K-means.png")
plt.show()


from scipy import stats


diff_exp_high = ((data['CFU'] + data['unk'])/2)/((data['poly'] + data['int'])/2) >= 2
diff_exp_low = ((data['CFU'] + data['unk'])/2)/((data['poly'] + data['int'])/2) <= 0.5

diff_exp_genes = data[diff_exp_high | diff_exp_low]
print(diff_exp_genes)
for gene_name, row in diff_exp_genes.iterrows():
    sample1 = [row['CFU'], row['unk']]
    sample2 = [row['poly'], row['int']]
    # print(gene_name, stats.ttest_rel(sample1, sample2).pvalue)
    pval = stats.ttest_rel(sample1, sample2).pvalue
    if pval <= 0.05:
        print(gene_name, pval)
 
labels = list(kmeans.labels_)
genes = list(data.index.values)

#Adcy6
goi_index = genes.index(sys.argv[2])
goi_cluster = labels[goi_index]

related_genes = []
for i, gene in enumerate(genes):
    if labels[i] == goi_cluster:
        related_genes.append(gene)

print(related_genes)
    