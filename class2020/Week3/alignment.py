#!/usr/bin/env python3

import sys
import numpy as np
import re
from collections import Counter

def sigma(s, t):# s and t are the bases; want A to be zero, C to be 1, G is 2, T is 3
#use the bases as the index and then return the sigma value as part of the function
  
  #                   A     C     G     U
  sigma_score = [ [   91, -114,  -31, -123 ],
                  [ -114,  100, -125,  -31 ],
                  [  -31, -125,  100, -114 ],
                  [ -123,  -31, -114,   91 ] ]
  nucleotide = ["A","C","G","T"] 
  nts = s, t
  for nt1 in enumerate(nucleotide):
    for nt2 in enumerate(nucleotide):
      indx = nt1[0],nt2[0]
      nt_pair = nt1[1],nt2[1]
      if nts != nt_pair:
        continue
      elif nts == nt_pair:
        pos = indx
        score = sigma_score[pos[0]][pos[1]]
        return score 

gap = 300
def needlemanwunch(seq1, seq2):
  n = len(seq1) + 1 # number of columns in our matrix, plus header
  m = len(seq2) + 1 # number of rows in our matrix, plus header 
  # initialize alightnment matrix of zeroes
  alignment = np.zeros((m, n), dtype = float) 
  walkback = np.zeros((m, n), dtype = int) # where the pointer will go 
  # fill gap penalty in the first row and first column
  #Initialization
  for i in range(m):
      alignment[i][0] = (-gap)*i
  for j in range(n):
      alignment[0][j] = (-gap)*j
  for i in range(1, m):
    for j in range(1, n):
      v = alignment[i][j-1] - gap
      h = alignment[i-1][j] - gap
      d = alignment[i-1][j-1] + sigma(seq2[i-1],seq1[j-1])
      alignment[i][j] = max(v,h,d)
     
      if alignment[i][j] == d: # diagonal --> match or mismatch
        walkback[i][j] = 1
      elif alignment[i][j] == h: #
        walkback[i][j] = 2
      elif alignment[i][j] == v: #
        walkback[i][j] = 3
     
  return alignment, walkback
def print_alignment( alignment, walkback, seq1, seq2 ):  
  align1 = ""
  align2 = ""
  i = len(seq2)
  j = len(seq1)

  align_score = alignment[i][j]
  while i > 0 and j > 0:
    if walkback[i][j] == 1: # diagonal 
      align1 += seq2[i-1]
      align2 += seq1[j-1]
      i -= 1
      j -= 1
    elif walkback[i][j] == 2: # horizontal
      align1 += seq2[i-1]
      align2 += "-"
      i -= 1
    elif walkback[i][j] == 3: # vertical
      align1 += "-"
      align2 += seq1[j-1]
      j -= 1
  align1 = align1[::-1]
  align2 = align2[::-1]
  
  print ("Gap:" + "\n" + str(gap) + "\n")
  print ("Alignment 1:" + "\n" + align1 + "\n") 
  print ("Alignment 2:" + "\n" + align2 + "\n") 
  print ("Score: " + "\n" + str(align_score))
 
  
def main():
    seq2 = 'GGGGCTGCCAACACAGAGGTGCAACCATGGTGCTGTCCGCTGCTGACAAGAACAACGTCAAGGGCATCTTCACCAAAATCGCCGGCCATGCTGAGGAGTATGGCGCCGAGACCCTGGAAAGGATGTTCACCACCTACCCCCCAACCAAGACCTACTTCCCCCACTTCGATCTGTCACACGGCTCCGCTCAGATCAAGGGGCACGGCAAGAAGGTAGTGGCTGCCTTGATCGAGGCTGCCAACCACATTGATGACATCGCCGGCACCCTCTCCAAGCTCAGCGACCTCCATGCCCACAAGCTCCGCGTGGACCCTGTCAACTTCAAACTCCTGGGCCAATGCTTCCTGGTGGTGGTGGCCATCCACCACCCTGCTGCCCTGACCCCGGAGGTCCATGCTTCCCTGGACAAGTTCTTGTGCGCCGTGGGCACTGTGCTGACCGCCAAGTACCGTTAAGACGGCACGGTGGCTAGAGCTGGGGCCAACCCATCGCCAGCCCTCCGACAGCGAGCAGCCAAATGAGATGAAATAAAATCTGTTGCATTTGTGCTCCAG'
    seq1 = 'CATAAACCCTGGCGCGCTCGCGGCCCGGCACTCTTCTGGTCCCCACAGACTCAGAGAGAACCCACCATGGTGCTGTCTCCTGCCGACAAGACCAACGTCAAGGCCGCCTGGGGTAAGGTCGGCGCGCACGCTGGCGAGTATGGTGCGGAGGCCCTGGAGAGGATGTTCCTGTCCTTCCCCACCACCAAGACCTACTTCCCGCACTTCGACCTGAGCCACGGCTCTGCCCAGGTTAAGGGCCACGGCAAGAAGGTGGCCGACGCGCTGACCAACGCCGTGGCGCACGTGGACGACATGCCCAACGCGCTGTCCGCCCTGAGCGACCTGCACGCGCACAAGCTTCGGGTGGACCCGGTCAACTTCAAGCTCCTAAGCCACTGCCTGCTGGTGACCCTGGCCGCCCACCTCCCCGCCGAGTTCACCCCTGCGGTGCACGCCTCCCTGGACAAGTTCCTGGCTTCTGTGAGCACCGTGCTGACCTCCAAATACCGTTAAGCTGGAGCCTCGGTGGCCATGCTTCTTGCCCCTTGGGCCTCCCCCCAGCCCCTCCTCCCCTTCCTGCACCCGTACCCCCGTGGTCTTTGAATAAAGTCTGAGTGGGCGGCAAAAAAAAAAAAAAAAAAAAAA'
    alignment, walkback = needlemanwunch( seq2, seq1 )
    print_alignment( alignment, walkback, seq2, seq1 )
if __name__ == "__main__":
    main()
