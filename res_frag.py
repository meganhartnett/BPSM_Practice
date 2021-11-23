#!/usr/local/bin/python3

seq = 'ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT'

n = seq.find('GAATTC')

print(n)

res_f = seq[0:22]

res_f2 = seq[22:]

print(res_f)

print(res_f2) 

len_res_f2 = len(res_f2)

print(len_res_f2)
