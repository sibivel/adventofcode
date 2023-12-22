import sys
import re
import numpy as np
sys.setrecursionlimit(10**9)

# inputs = [line.strip() for line in sys.stdin]
# R, C = (len(inputs), len(inputs[0]))
inputs = np.array([[*line.strip()] for line in sys.stdin])
R, C = inputs.shape
print(R, C)

STEPS = 300
start = (0,0, 0,0)
for r in range(R):
    for c in range(C):
        if inputs[r,c] == 'S':
            start = (r,c, 0, 0)
print(start)
steps = 0
queue = [start]
nextQ = set()
visited = [set(), set()]
visited[0].add(start)
oldCount = 0
while steps < STEPS:
    r, c, mr, mc = queue.pop()
    for dr,dc in [(-1,0), (1,0), (0,1), (0,-1)]:
        nr = r + dr
        nc = c + dc
        nmr = mr
        nmc = mc
        if nr < 0:
            nmr -= 1
            nr = (nr + R) % R
        if nr >= R:
            nmr += 1
            nr = nr % R
        if nc < 0:
            nmc -= 1
            nc = (nc + C) % C
        if nc >= C:
            nmc += 1
            nc = nc % C
        # if nr < 0 or nr >= R or nc < 0 or nc >= C or inputs[nr, nc] == '#':
        if inputs[nr, nc] == '#':
            continue
        t = (nr, nc, nmr, nmc)
        if nmr == 0 and nmc == 0:
            visited[steps % 2].add(t)
        nextQ.add(t)
    if len(queue) == 0:
        queue = [*nextQ]
        nextQ = set()
        steps += 1
        if steps % 2 == 1 and oldCount == len(visited[1]):
            print("filled", len(visited[1]), steps)
            # quit()
        oldCount = len(visited[1])
        done = 0

# for r in range(R):
#     for c in range(C):
#         mt = (r,c,0,0)
#         if  inputs[r,c] != '#' and mt not in visited[1] and mt not in visited[0]:
#             print(r,c)
# print(len(visited[0]), len(visited[1]))

# 130 steps to cover all but 5 squares in first map. odd len 7699
# 261th steps cover all but 5 on map 1,0 reached at 66 odd len 7651
# 392th steps cover all but 5 on map 1,1 reached at 132 odd len 7699
# 392th steps cover all but 5 on map 2,0 reached at 197 odd len 7699

# 26501365 / 131 = 202300.4961832061

# 

