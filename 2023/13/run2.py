import sys
import re
import numpy as np
sys.setrecursionlimit(10**9)

def solve(pattern):
    R, C = pattern.shape
    for i in range(R-1):
        t = i
        b = i+1
        done = True
        diffs = 0
        while t >= 0 and b < R:
            d = np.sum(pattern[t] != pattern[b])
            diffs += d 
            t -= 1
            b += 1
        if diffs == 1:
            return (i+1) * 100

    for i in range(C-1):
        l = i
        r = i+1
        done = True
        diffs = 0
        while l >= 0 and r < C:
            d = np.sum(pattern[:,l] != pattern[:,r])
            diffs += d 
            l -= 1
            r += 1
        if diffs == 1:
            return i+1
    return 0
        
inputs =[line.strip() for line in sys.stdin]

patterns = []

pattern = []
for line in inputs:
    if len(line) == 0:
        patterns.append(np.array(pattern))
        pattern = []
    else:
        pattern.append([*line])
patterns.append(np.array(pattern))

sum = 0
for pattern in patterns:
    x = solve(pattern)
    print(x)
    sum += x
print(sum)
