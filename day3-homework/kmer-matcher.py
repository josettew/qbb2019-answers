#!/usr/bin/env python3


from fasta import FASTAReader
import sys

target=FASTAReader(open(sys.argv[1]))
query=FASTAReader(open(sys.argv[2]))

k=int(sys.argv[3])
dic_target={}

for ident, sequence in target:
   sequence=sequence.upper()
   for i in range (0, len(sequence)-k+1):
       kmertarget=sequence[i:i+k]
       if kmertarget not in dic_target:
           dic_target[kmertarget]=[(i,ident)]
       else:
           dic_target[kmertarget].append((i, ident))
           #print(dic_target)

for identifier, sequence1 in query:
   sequence1=sequence1.upper()
   for a in range(0,len(sequence1) -k +1):
       kmerquery=sequence1[a:a+k]
       if kmerquery in dic_target:
           print(dic_target[kmerquery], str(a), kmerquery)
            