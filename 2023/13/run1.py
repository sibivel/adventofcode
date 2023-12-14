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
        while t >= 0 and b < R:
            if not np.array_equal(pattern[t], pattern[b]):
                done = False
                break
            t -= 1
            b += 1
        if done:
            return (i+1) * 100

    for i in range(C-1):
        l = i
        r = i+1
        done = True
        while l >= 0 and r < C:
            print(l,r)
            print(pattern[:,l])
            print(pattern[:,r])
            if not np.array_equal(pattern[:,l],pattern[:,r]):
                done = False
                break
            l -= 1
            r += 1
        if done:
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
