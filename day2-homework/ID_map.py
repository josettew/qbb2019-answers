#!/usr/bin/env python3

import sys

## Argument should be:
    ## 1: fly_id_columns.txt (FB_ID and Uniprot_ID columns)
    ## 2: t_data.ctab (comparison set of FB_IDs)
    ## 3: either "default" or "nothing"

gene_dict = {}

for i, line in enumerate(open(sys.argv[1])):
    columns = line.rstrip("\n").split()
    gene_name = columns[0]
    uniprot = columns[1]
    if gene_name in gene_dict:
        continue
    else:
        gene_dict[gene_name] = uniprot

for i, line in enumerate(open(sys.argv[2])):
    columns = line.split("\t")
    gene_ID = columns[8]
    if gene_ID in gene_dict:
        print(line.strip("\n"), gene_dict[gene_ID])
        #if you want to run the nothing option type nothing as your 3rd argument
    elif gene_ID not in gene_dict and sys.argv[3] == "nothing":
        continue
        #if you want to have N/A in non-matching lines, use default as 3rd argument
    elif gene_ID not in gene_dict and sys.argv[3] == "default":
        print(line.strip("\n"), "N/A")
    
        