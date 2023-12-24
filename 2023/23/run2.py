import sys
import re
import numpy as np
import math
import copy
import heapq

sys.setrecursionlimit(10**9)
# inputs = [line.strip() for line in sys.stdin]
# R, C = (len(inputs), len(inputs[0]))
maxy = 0
def longest(inputs, sr, sc):
    global maxy
    R, C = inputs.shape
    queue = [(0, sr, sc, set())]
    solution = None
    while len(queue) > 0:
        length, r, c, visited = queue.pop()
        dirs = [(-1, 0), (1,0), (0,1), (0,-1)]
        if r < 0 or c < 0 or r >= R or c >= C:
            continue
        if inputs[r][c] == '#' or (r,c) in visited:
            continue
        if r == R-1 and c == C-2:
            maxy = max(maxy, length)
            print(length)
            continue

        visited.add((r,c))
        for idx, d in enumerate(dirs):
            nr = r + d[0]
            nc = c + d[1]
            queue.append((length+1, nr, nc, copy.deepcopy(visited)))
        queue.sort()
        # print([x[0] for x in queue])
    return 0
    

inputs = np.array([[*line.strip()] for line in sys.stdin])
R, C = inputs.shape
maxLengths = np.full((4, R, C), None, dtype=object)
print(R, C)

start = (0, 2)

print(longest(inputs, 0,1))
print(maxy)