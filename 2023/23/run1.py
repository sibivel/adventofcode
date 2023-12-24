import sys
import re
import numpy as np
import math
import copy
sys.setrecursionlimit(10**9)
# inputs = [line.strip() for line in sys.stdin]
# R, C = (len(inputs), len(inputs[0]))
maxy = 0
def longest(inputs, r, c, length, maxLengths, pdir, dir):
    global maxy
    R, C = inputs.shape
    end = (-1, -1)
    dirs = [(-1, 0), (1,0), (0,1), (0,-1)]
    if r < 0 or c < 0 or r >= R or c >= C:
        return None
    if inputs[r][c] == '#':
        return None
    if maxLengths[pdir][dir][r][c] is not None and maxLengths[pdir][dir][r][c] > length:
        return None
    if r == R-1 and c == C-2:
        maxLengths[pdir][dir][r][c] = length
        print(length)
        return length
    
    prevc = inputs[r][c]
    inputs[r][c] = '#'
    fres = None
    # if prevc == '^':
    #     fres = longest(inputs, r-1, c, length+1)
    # elif prevc == '>':
    #     fres = longest(inputs, r, c+1, length+1)
    # elif prevc == '<':
    #     fres = longest(inputs, r, c-1, length+1)
    # elif prevc == 'v':
    #     fres = longest(inputs, r+1, c, length+1)
    # else:
    for idx, d in enumerate(dirs):
        nr = r + d[0]
        nc = c + d[1]
        res = longest(inputs, nr, nc, length+1, maxLengths, dir, idx)
        if res is not None:
            if fres is None:
                fres = res
            else:
                fres = max(fres, res)
    inputs[r][c] = prevc
    if fres != None:
        maxLengths[pdir][dir][r][c] = length
    return fres
    

inputs = np.array([[*line.strip()] for line in sys.stdin])
R, C = inputs.shape
maxLengths = np.full((4, 4, R, C), None, dtype=object)
print(R, C)

start = (0, 2)

print(longest(inputs, 0,1, 0, maxLengths,0, 0))