import sys
import re
import numpy as np

sys.setrecursionlimit(10**9)

def inrange(a, b, c):
    if a > b:
        return inrange(b, a, c)
    return (a <= c <= b)

def lowerFirst(a, b):
    if a <= b:
        return (a, b)
    return (b, a)

inputs = np.array([[*line.strip()] for line in sys.stdin])

R,C = inputs.shape
doubleRs = set()
doubleCs = set()
for i in range(R):
    if not '#' in inputs[i]:
        doubleRs.add(i)

for i in range(C):
    if not '#' in inputs[:, i]:
        doubleCs.add(i)

galaxyRows, galaxyCols = np.where(inputs == '#')
galaxies = [*zip(galaxyRows, galaxyCols)]

sum = 0
G = len(galaxies)
for i in range(G):
    for j in range(i+1, G):
        r1, c1 = galaxies[i]
        r2, c2 = galaxies[j]
        r1, r2 = lowerFirst(r1, r2)
        c1, c2 = lowerFirst(c1, c2)
        
        dr  = 0
        for k in range(r1, r2):
            if k in doubleRs:
                dr += 1000000 - 1
        rdist = r2 - r1 + dr
        
        dc  = 0
        for k in range(c1, c2):
            if k in doubleCs:
                dc += 1000000 - 1
        cdist = c2 - c1 + dc
        
        sum += rdist + cdist
        

        
        
        
print(sum)

# print(0)
