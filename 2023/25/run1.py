import sys
import re
import numpy as np
import math
sys.setrecursionlimit(10**9)

def addToGraph(graph, v, e):
    if not v in graph:
        graph[v] = []
    graph[v].append(e)

def removeEdge(graph, v, e):
    graph[v].remove(e)
    graph[e].remove(v)

def getPaths(graph, start):
    queue = [start]
    paths = {}
    paths[start] = []
    visited = set(start)
    while len(queue) > 0:
        next= queue.pop(0)
        path = paths[next]
        for e in graph[next]:
            if e in visited:
                continue
            edge = [next, e]
            edge.sort()
            queue.append(e)
            paths[e] = [*path, ' '.join(edge)]
            visited.add(e)
    return paths

def getSets(graph, nodes):
    sets = []
    for n in nodes:
        done = False
        for s in sets:
            if n in s:
                done = True
                break
        if not done:
            neighbors = set()
            getConnected(graph, n, neighbors)
            sets.append(neighbors)
    return sets

def getConnected(graph, n, visited):
    if n in visited:
        return
    visited.add(n)
    for c in graph[n]:
        getConnected(graph, c, visited)





inputs = [line.strip() for line in sys.stdin]
R, C = (len(inputs), len(inputs[0]))
# inputs = np.array([[*line.strip()] for line in sys.stdin])
# R, C = inputs.shape
# print(R, C)

graph = {}
for input in inputs:
    v, ends = input.split(':')
    ends = ends.split()
    # print(ends)
    for e in ends:
        addToGraph(graph, v, e)
        addToGraph(graph, e, v)
nodes = [*graph.keys()]
N = len(nodes)
edgeCounts = {}
paths = {}
for i in range(N):
    a = nodes[i]
    paths[a] = getPaths(graph, a)
    for target, path in paths[a].items():
        for edge in path:
            if edge not in edgeCounts:
                edgeCounts[edge] = 0
            edgeCounts[edge] += 1
sortededges = [*edgeCounts.keys()]
sortededges.sort(key= lambda e: edgeCounts[e])
# for se in sortededges:
#     print(se, edgeCounts[se])
edgesToRemove = sortededges[-3:]
print(edgesToRemove)

for e in edgesToRemove:
    a,b = e.split()
    removeEdge(graph, a, b)

groups = getSets(graph, nodes)
# print(groups)
product = 1
for g in groups:
    product *= len(g)
    print(product)





