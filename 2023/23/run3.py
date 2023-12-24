import sys
import re
import numpy as np
import math
import copy
sys.setrecursionlimit(10**9)
# inputs = [line.strip() for line in sys.stdin]
# R, C = (len(inputs), len(inputs[0]))
maxy = 0
inputs = np.array([[*line.strip()] for line in sys.stdin])
R, C = inputs.shape
dirs = [(-1, 0), (1,0), (0,1), (0,-1)]
rdirs = [(1, 0), (-1,0), (0,-1), (0,1)]

def isIntersection(inputs, r, c):
    if r < 0 or c < 0 or r >= R or c >= C:
        return None
    if inputs[r][c] == '#':
        return None
    if inputs[r][c] == 'S':
        return True
    dCount = 0
    for d in dirs:
        nr = r + d[0]
        nc = c + d[1]
        if nr >= 0 and nr < R and nc >= 0 and nc < C and inputs[nr][nc] != '#':
            dCount += 1
    return dCount > 2

def findNextIntersection(inputs, r, c, length, di):
    if r < 0 or c < 0 or r >= R or c >= C:
        return None
    if isIntersection(inputs, r, c):
        return (r,c, length)
    for id, d in enumerate(dirs):
        if d != rdirs[di]:
            res = findNextIntersection(inputs, r+d[0], c+d[1], length+1, id)
            if res is not None:
                return res
    return None

def getIntersections(inputs, sr, sc, graph):
    t = (sr,sc)
    if isIntersection(inputs, sr, sc):
        if t not in graph:
            graph[t] = []
        queue = [(sr,sc,0)]
        visited = set([(sr,sc)])
        while len(queue) > 0:
            r, c, l = queue.pop()
            for id, d in enumerate(dirs):
                nr = r + d[0]
                nc = c + d[1]
                if nr < 0 or nr >= R or nc < 0 or nc >= C or inputs[nr][nc] == '#':
                    continue
                if (nr, nc) in visited:
                    continue
                if isIntersection(inputs, nr, nc):
                    graph[t].append((nr, nc, l+1))
                else:
                    visited.add((nr, nc))
                    queue.append((nr, nc, l+1))

def longest(graph, r, c, length, visited):
    global maxy
    if r == R-1 and c == C-2:
        if length > maxy:
            maxy = length
            print(length)
            return length
        return None
    fres = None
    visited.add((r,c))
    for v in graph[(r,c)]:
        nr, nc, l = v
        if (nr, nc) in visited:
            continue
        res = longest(graph, nr, nc, length+l, visited)
        if res is not None:
            if fres is None:
                fres = res
            else:
                fres = max(fres, res)
    visited.remove((r,c))
    return fres

    

print(R, C)
graph = {}
for r in range(R):
    for c in range(C):
        getIntersections(inputs, r, c, graph)
# print(graph)
# start = (0, 2)

print(longest(graph, 0,1, 0, set()))