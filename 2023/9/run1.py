import sys
import re

inputs = [line.strip() for line in sys.stdin]

def func(seq: []):
    next = []
    for i in range(1, len(seq)):
        next.append(seq[i] - seq[i-1])
    if len([x for x in next if x != 0]) > 0:
        d = func(next)
        return seq[-1] + d
    else:
        return seq[-1]

sum = 0
for input in inputs:
    seq = [int(x) for x in input.split()]
    sum += func(seq)
    
print(sum)
    