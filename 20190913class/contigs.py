#!/usr/bin/env python3

import sys
from fasta import FASTAReader

f = sys.stdin
reader = FASTAReader(f)

contigs = []
for indent, sequence in reader:
    contigs.append(sequence)
contigs = sorted(contigs, reverse = True)
    
print(len(contigs))

sequence_length = []
for sequence in contigs:
    sequence_length.append(len(sequence))
   
print(min(sequence_length))
print(max(sequence_length))
print(sum(sequence_length)/len(contigs))
print(sum(sequence_length)/2) 

sorted_length = sorted(sequence_length, reverse = True)

count = 0
for i, item in enumerate(sorted_length):
    count += item
    if count >= 23358:
    #if count >= (sum(sequence_length)/2): would also work here
        break
print(sorted_length[i]) #length of N50 contig
print(i) #N50 contig number
        
    	#real	0m0.048s
    	#user	0m0.027s
    	#sys	0m0.010s

