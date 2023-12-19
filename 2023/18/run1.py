import sys
import re
import numpy as np
sys.setrecursionlimit(10**9)

def getNewCoords(x, y, dir, dist):
    if dir == 'D':
        return [(x, y-i-1) for i in range(dist)]
    if dir == 'U':
        return [(x, y+i+1) for i in range(dist)]
    if dir == 'R':
        return [(x+i+1, y) for i in range(dist)]
    if dir == 'L':
        return [(x-1-i, y) for i in range(dist)]
    
def getChilds(x, y):
    return [(x +1, y), (x-1, y), (x, y+1), (x, y-1)]

def bfs(minX, minY, maxX, maxY,  startX, startY, inside, outside):
    t = (startX, startY)
    if t in inside:
        return
    if t in outside:
        return
    visited = set()
    queue = []
    queue.append((startX, startY))
    isInside = True
    while len(queue) > 0:
        t = queue.pop()
        x,y = t
        if t in outside:
            isInside = False
            break
        if x < minX or x > maxX or y < minY or y > maxY:
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

cur = (0,0)
minX = 0
minY = 0
maxX = 0
maxY = 0
inside = set()
inside.add(cur)
for input in inputs:
    dir, dist, hex = input.split()
    dist = int(dist)
    for coord in getNewCoords(cur[0], cur[1], dir, dist):
        cur = coord
        inside.add(cur)
        minX = min(minX, cur[0])
        minY = min(minY, cur[1])
        maxX = max(maxX, cur[0])
        maxY = max(maxY, cur[1])

outside = set()
for x in range(minX, maxX+1):
    for y in range(minY, maxY+1):
        t  = (x, y)
        if t in inside or t in outside:
            continue
        bfs(minX, minY, maxX, maxY, x, y, inside, outside)
print(len(inside))




