import sys
import re
import numpy as np
sys.setrecursionlimit(10**9)


def getNewCoord(x, y, dir, dist):
    if dir == 'U':
        return (x, y-dist)
    if dir == 'D':
        return (x, y+dist)
    if dir == 'R':
        return (x+dist, y)
    if dir == 'L':
        return (x-dist, y)


def getChilds(x, y):
    return [(x + 1, y), (x-1, y), (x, y+1), (x, y-1)]


def bfs(startX, startY, inside, outside, Xs, Ys):
    t = (startX, startY)
    if t in inside:
        return
    if t in outside:
        return
    visited = set()
    queue = []
    queue.append((startX, startY))
    visited.add((startX, startY))
    isInside = True
    while len(queue) > 0:
        t = queue.pop()
        x, y = t
        if t in outside:
            isInside = False
            break
        if x < 0 or x >= len(Xs) or y < 0 or y >= len(Ys):
            isInside = False
            break
        for child in getChilds(x, y):
            if child in visited or child in inside:
                continue
            visited.add(child)
            queue.append(child)
    for v in visited:
        if isInside:
            inside.add(v)
        else:
            outside.add(v)


inputs = np.array([line.strip() for line in sys.stdin])
R, C = (len(inputs), len(inputs[0]))
# inputs = np.array([[*line.strip()] for line in sys.stdin])
# R, C = inputs.shape
print(R, C)
dirmap = {
    0: 'R',
    1: 'D',
    2: 'L',
    3: 'U',
}
cur = [0, 0]
edges = []
edges.append(cur)
sum = 0
clockwise = True
for input in inputs:
    dir, dist, hex = input.split()
    hex = re.search('\(\#(.+)\)', hex).groups()[0]
    dist = int(hex[0:5], 16)
    dir = dirmap[int(hex[5])]
    # dist = int(dist)
    print(dir, dist)
    # if dir == 'D' or 'L':
    #     sum += dist
    newcur = getNewCoord(cur[0], cur[1], dir, dist)
    sum += dist
    cur = newcur
    edges.append(cur)

for i in range(len(edges)-1):
    x1, y1 = edges[i]
    x2, y2 = edges[i+1]
    sum += int(x1 * y2) - int(x2*y1)
print(edges)
print(sum/2+1)
