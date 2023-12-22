import sys
import re
import numpy as np
sys.setrecursionlimit(10**9)

# inputs = [line.strip() for line in sys.stdin]
# R, C = (len(inputs), len(inputs[0]))
inputs = np.array([[*line.strip()] for line in sys.stdin])
R, C = inputs.shape
print(R, C)

STEPS = 64
start = (0,0)
for r in range(R):
    for c in range(C):
        if inputs[r,c] == 'S':
            start = (r,c)

steps = 0
queue = [start]
nextQ = set()
while steps < STEPS:
    r, c = queue.pop()
    for dr,dc in [(-1,0), (1,0), (0,1), (0,-1)]:
        nr = r + dr
        nc = c + dc
        if nr < 0 or nr >= R or nc < 0 or nc >= C or inputs[nr, nc] == '#':
            continue
        nextQ.add((nr,nc))
    if len(queue) == 0:
        queue = [*nextQ]
        nextQ = set()
        steps += 1
print(len(queue))


