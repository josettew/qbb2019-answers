#!/usr/bin/env python3

from fasta import FASTAReader
import sys

target = FASTAReader(open(sys.argv[1])) #subset.fa
query = FASTAReader(open(sys.argv[2])) #droYak2_seq.fa
k = int(sys.argv[3])

target_dict = {}
target_sequence = {}
dict_3 = {}

for ident, sequence in target:
   sequence = sequence.upper()
   target_sequence[ident] = sequence
   for i in range(0, len(sequence) - k +1):
       kmer = sequence[i:i+k]
       if kmer in target_dict:
           target_dict[kmer].append((ident,i))
       else:
           target_dict[kmer]=[(ident,i)]


  # print(target_dict)

for ident, sequence1 in query: # get idenity and seq from fasta
   sequence1 = sequence.upper()
   for j in range(0, len(sequence1) - k +1): # get kmer
       kmer = sequence1[j:j+k]
       if kmer in target_dict:
           for ident, i in target_dict[kmer]: # if theres multiple target matches get individual tuples
               target_seq = target_sequence[ident]
               length_target_seq = len(target_seq)
               length_query_seq = len(sequence1)
               extend_right = True
               entended_kmer = kmer
               while True:      # boolean to extend right
                   if extend_right:
                       if sequence1[j+k+1] == target_seq[i+k+1]:
                           j += 1
                           i += 1
                           extended_kmer += sequence1[j+k+1]
                       else:
                           extened_right = False
                   else:
                       #this is where i would add extension to dict_3  
                       break
                   if (i+k) == length_target_seq or (j+k) == length_query_seq:
                       extend_right = False
                           
               #print(ident, j, i, kmer)
                #kmers are matched

