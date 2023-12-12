import sys
import re
import numpy as np
sys.setrecursionlimit(10**9)

inputs = np.array([[*line.strip()] for line in sys.stdin])

R = len(inputs)
C = len(inputs[0])
doubleRs = []
doubleCs = []
for i in range(R):
    if not '#' in inputs[i]:
        doubleRs.append(i)

for i in range(C):
    if not '#' in inputs[:, i]:
        doubleCs.append(i)

# print(doubleRs)
# print(doubleCs)

expanded = np.empty((R + len(doubleRs), C + len(doubleCs)))

expanded = []
for r in range(R):
    row = []
    for c in range(C):
        row.append(inputs[r][c])
        if c in doubleCs:
            row.append('.')
    expanded.append(row)
    if r in doubleRs:
        expanded.append(row)
expanded = np.array(expanded)
print(expanded)

galaxies = []
R = len(expanded)
C = len(expanded[0])
for r in range(R):
    for c in range(C):
        if expanded[r][c] == '#':
            galaxies.append((r,c))

sum = 0
G = len(galaxies)
for i in range(G):
    for j in range(i+1, G):
       sum += abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])
print(sum)



        

# print(0)
