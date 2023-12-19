import sys
import re
import numpy as np
sys.setrecursionlimit(10**9)


def getNewCoord(x, y, dir, dist):
    if dir == 'D':
        return (x, y-dist)
    if dir == 'U':
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
cur = (0, 0)
minX = 0
minY = 0
maxX = 0
maxY = 0
Xs = set()
Ys = set()
Xs.add(0)
Ys.add(0)
lines = []
edges = set()
edges.add(cur)
for input in inputs:
    _, _, hex = input.split()
    hex = re.search('\(\#(.+)\)', hex).groups()[0]
    dist = int(hex[0:5], 16)
    dir = dirmap[int(hex[5])]
    print(dist, dir)
    newcur = getNewCoord(cur[0], cur[1], dir, dist)
    lines.append([cur, newcur])
    cur = newcur
    Xs.add(cur[0])
    Ys.add(cur[1])
    # edges.add(cur)

Xs = sorted([*Xs])
Ys = sorted([*Ys])

inside = set()
for line in lines:
    startX, startY = line[0]
    endX, endY = line[1]
    i1 = Xs.index(startX)
    i2 = Xs.index(endX)

    j1 = Ys.index(startY)
    j2 = Ys.index(endY)
    s1 = 1
    s2 = 1
    if i1 > i2:
        s1 = -1
    if j1 > j2:
        s2 = -1
    for i in range(i1, i2+1, s1):
        for j in range(j1, j2+1, s2):
            inside.add((i,j))
print(Xs, Ys)
print(sorted(inside))

outside = set()
for x in range(len(Xs)):
    for y in range(len(Ys)):
        t = (x, y)
        if t in inside or t in outside:
            continue
        bfs(x, y, inside, outside, Xs, Ys)

sum = 0
for i in range(1, len(Xs)):
    x = Xs[i]
    for j in range(1, len(Ys)):
        y = Ys[j]
        if (i, j) in inside and (i-1, j-1) in inside and (i, j-1) in inside and (i-1, j) in inside:
            sum += abs(Xs[i] - Xs[i-1]) * abs(Ys[j] - Ys[j-1])
print(sorted(outside))
print(sum)
