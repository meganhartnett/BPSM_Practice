#!/usr/local/bin/python3

seq = 'ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT'

print("The complement sequence is", seq.replace('A', 't').replace('T','a').replace('G','c').replace('C','g').upper())
