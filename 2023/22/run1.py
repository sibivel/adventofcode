import sys
import re
import numpy as np
import math
import copy
sys.setrecursionlimit(10**9)

def getAllCubes(c1, c2):
    if c1[0] != c2[0]:
        l = min(c1[0], c2[0])
        r = max(c1[0], c2[0])
        return np.array([[i, c1[1], c1[2]] for i in range(l, r+1)])
    if c1[1] != c2[1]:
        l = min(c1[1], c2[1])
        r = max(c1[1], c2[1])
        return np.array([[c1[0], i, c1[2]] for i in range(l, r+1)])
    else:
        l = min(c1[2], c2[2])
        r = max(c1[2], c2[2])
        return np.array([[c1[0], c1[1], i] for i in range(l, r+1)])
    
def isVertical(c1, c2):
    return c1[2] != c2[2]

inputs = [line.strip() for line in sys.stdin]
R, C = (len(inputs), len(inputs[0]))
# inputs = np.array([[*line.strip()] for line in sys.stdin])
# R, C = inputs.shape
# print(R, C)

bricks = []
# maxX = 0
# maxY = 0
# maxZ = 0
for input in inputs:
    w1, w2 = input.split('~')
    e1 = tuple([int(i) for i in w1.split(',')])
    e2 = tuple([int(i) for i in w2.split(',')])

    if e1[2] > e2[2]:
        bricks.append((e2, e1))
    else:
        bricks.append((e1, e2))
bricks.sort(key=lambda cube: cube[0][2])

lowestHeight = {}
lowestHeightIds = {}
restingOn = {}
for id, brick in enumerate(bricks):
    # print(id)
    # print(lowestHeight)
    # print(lowestHeightIds)
    c1, c2 = brick
    allCubes = getAllCubes(c1, c2)
    # print(brick, allCubes)
    restingOn[id] = set()
    if isVertical(c1, c2):
        floor = lowestHeight.get((c1[0], c1[1]), 0)
        floorId = lowestHeightIds.get((c1[0], c1[1]), None)
        if floorId is not None:
            restingOn[id].add(floorId)
        moveDown = c1[2] - (floor + 1)
        lowestHeight[(c1[0], c1[1])] = c2[2]-moveDown
        lowestHeightIds[(c1[0], c1[1])] = id
    else:
        floor = 0
        for c in allCubes:
            floor = max(floor, lowestHeight.get((c[0], c[1]), 0))

        for c in allCubes:
            floorId = lowestHeightIds.get((c[0], c[1]), None)
            if floorId is not None and lowestHeight[(c[0], c[1])] == floor:
                restingOn[id].add(floorId)
            lowestHeight[(c[0], c[1])] = floor+1
            lowestHeightIds[(c[0], c[1])] = id

cantBePulled = set()
for k, v in restingOn.items():
    if len(v) == 1:
        cantBePulled.update(v)
result = []
for i in range(len(bricks)):
    if i not in cantBePulled:
        result.append(i)
print(bricks)
print(restingOn) 
# print(bricks)
# print(result)        
print(len(result))

totalRemoved = 0
for i in range(len(bricks)):
    rcopy = copy.deepcopy(restingOn)
    toRemove = [i]
    removed = set()
    while len(toRemove) > 0:
        r = toRemove.pop(0)
        if r in removed:
            continue
        for j in range(len(bricks)):
            if r in rcopy[j]:
                rcopy[j].remove(r)
                if len(rcopy[j]) == 0:
                    toRemove.append(j)
        removed.add(r)
    print(len(removed))
    totalRemoved += len(removed)-1
print(totalRemoved)

