import sys
import re
import numpy as np
sys.setrecursionlimit(10**9)

def getDirs(d, cell):
    if cell == '.':
        return [d]
    elif cell == '/':
        if d == 'L':
            return ['D']
        elif d == 'R':
            return ['U']
        elif d == 'U':
            return ['R']
        elif d == 'D':
            return ['L']
    elif cell == '\\':
        if d == 'L':
            return ['U']
        elif d == 'R':
            return ['D']
        elif d == 'U':
            return ['L']
        elif d == 'D':
            return ['R']
    elif cell == '|':
        return ['U', 'D']
    elif cell == '-':
        return ['L', 'R']
    
def getCoords(r, c, d):
    if d == 'L':
        return (r, c-1, d)
    elif d == 'R':
        return (r, c+1, d)
    elif d == 'U':
        return (r-1, c, d)
    elif d == 'D':
        return (r+1, c, d)


inputs = np.array([[*line.strip()] for line in sys.stdin])

R,C = inputs.shape


energized = []
for r in range(R):
    energized.append([])
    for c in range(C):
        energized[r].append(set())
count = 0
stack = []
stack.append((0, 0, 'R'))

while len(stack) > 0:
    r, c, d = stack.pop()
    if r < 0 or r >= R or c < 0 or c >= C or d in energized[r][c]:
        continue
    energized[r][c].add(d)
    if len(energized[r][c]) == 1:
        count += 1
    newDs = getDirs(d, inputs[r][c])
    newCoords = [getCoords(r, c, newD) for newD in newDs]
    stack.extend(newCoords)
    # print(stack)
print(np.array(energized))
print(count)
# R, L, D, U




