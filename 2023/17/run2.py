import sys
import re
import numpy as np
import heapq
sys.setrecursionlimit(10**9)

def getDirs(d, dcount):
    result = []
    if dcount < 4:
        return [d]
    if dcount < 10:
        result.append(d)
    if d == 'R' or d == 'L':
        result.append('U')
        result.append('D')
    elif d == 'U' or d == 'D':
        result.append('L')
        result.append('R')
    return result

def getCoords(r, c, d):
    if d == 'L':
        return (r, c-1, d)
    elif d == 'R':
        return (r, c+1, d)
    elif d == 'U':
        return (r-1, c, d)
    elif d == 'D':
        return (r+1, c, d)

# inputs = np.array([line.strip() for line in sys.stdin])
inputs = np.array([[*line.strip()] for line in sys.stdin])

R,C = inputs.shape
print(inputs.shape)
visited = {}

queue = []
# cost to get here, r, c, dir, spaces traveled in that dir already, 
heapq.heappush(queue, (0, 0, 0, 'R', 0))
heapq.heappush(queue, (0, 0, 0, 'D', 0))

results = []
x = 0
while len(queue) > 0:
    print(x, end='\r')
    x += 1
    cost, r, c, d, dcount = heapq.heappop(queue)
    if r == R-1 and c == C-1 and dcount >= 4:
        results.append(cost)
        print(min(results))

    dirs = getDirs(d, dcount)
    childCells = [getCoords(r, c, dir) for dir in dirs]
    for child in childCells:
        nr, nc, nd = child
        if nr < 0 or nr >= R or nc < 0 or nc >= C:
            continue
        ndcount = 1
        ncost = cost + int(inputs[nr][nc])
        if nd == d:
            ndcount = dcount + 1
        t = (nr, nc, nd, ndcount)
        if t in visited and visited[t] <= ncost:
            continue
        visited[t] = ncost
        heapq.heappush(queue, (ncost, nr, nc, nd, ndcount))
    # queue.sort(key=lambda x: x[4], reverse=True)
        # print(queue[0])

print(results)
print(min(results))


        
    
    



