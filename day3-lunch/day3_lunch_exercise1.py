#!/usr/bin/env python3

import sys

#argument 1 = BDGP6.ENsemble.81.gtf

gene_list = []

for line in open(sys.argv[1]):
    fields = line.rstrip("\n").split()
    if fields[0] == "3R" and fields[2] == "gene" and "protein_coding" in line:
        count = 8
        for i in fields[8:]:
            count += 1
            if i == "gene_name":
                gene_name = fields[count]
                break
        gene_list.append((gene_name, int(fields[3]), int(fields[4])))
## creates my list with the gene name, the start position and end position

##Binary Search
lo = 0
hi = len(gene_list)-1
mid = 0
number_iterations = 0
mutation = 21378950

while (lo <= hi):
   mid = int((hi + lo) / 2)
   number_iterations = number_iterations +1
   if mid == hi or mid == lo:
       #print(gene_list[mid][0])
       #print(number_iterations)
       break
   if ( mutation < int(gene_list[mid][1])):
       hi = mid
   elif (mutation > int(gene_list[mid][1])):
       lo = mid
       
if (abs(gene_list[lo][2] - mutation)) > (abs(gene_list[hi][1]-mutation)):
    mid = hi
    print(abs(gene_list[hi][1]-mutation))
if (abs(gene_list[lo][2] - mutation)) < (abs(gene_list[hi][1]-mutation)):
    mid = lo
    print (abs(gene_list[lo][2] - mutation))

print(gene_list[mid])
print (number_iterations)

#27 bp away
#tin is gene_name
#takes 12 interations
