import sys
import re
import numpy as np
sys.setrecursionlimit(10**9)

def hash(s):
    cv = 0
    for c in s:
        cv += ord(c)
        cv = cv * 17
        cv = cv % 256
    return cv

inputs = [line.strip() for line in sys.stdin]

strings = inputs[0].split(',')
print(strings)
sum = 0
for s in strings:
    h = hash(s)
    print(s)
    sum += h
print(sum)
    
    



