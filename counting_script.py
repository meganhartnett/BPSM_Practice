#!/usr/local/bin/python3

seq = 'ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT'

num_A = seq.count("A")

print(num_A)

num_T = seq.count("T")

print(num_T)

seq_T = num_A + num_T

print(seq_T)

len_seq = len(seq)

print(len_seq)

seq_n = seq_T/len_seq

print(seq_n)

