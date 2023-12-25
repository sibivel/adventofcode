import sys
import re
import numpy as np
import math
sys.setrecursionlimit(10**9)

def findIntercept(vec1, vec2):
    p1, v1  = vec1
    p2, v2 = vec2
    
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    
    m1 = v1[1]/v1[0]
    m2 = v2[1]/v2[0]
    if (m2 == m1):
        return False
    x =( m2 * x2 - m1 * x1 + y1 - y2)/(m2-m1)
    y = m1 * (x-x1) + y1
    t1 = (x - x1)/v1[0]
    t2 = (x - x2)/v2[0]

    # lower = 7
    # upper = 27
    lower = 200000000000000
    upper = 400000000000000
    # print(x,y,t1,t2)
    if t1 > 0 and t2 > 0 and x >= lower and x <= upper and y >= lower and y <= upper:
        return True




inputs = [line.strip() for line in sys.stdin]
R, C = (len(inputs), len(inputs[0]))
# inputs = np.array([[*line.strip()] for line in sys.stdin])
# R, C = inputs.shape
# print(R, C)

vectors = []
for input in inputs:
    pstring, vstring = input.split('@')
    position = tuple([int(s.strip()) for s in pstring.split(',')])
    velocity = tuple([int(s.strip()) for s in vstring.split(',')])
    vectors.append((position, velocity))

count = 0
for i in range(R):
    for j in range(i+1, R):
        # print(vectors[i], vectors[j])
        if findIntercept(vectors[i], vectors[j]):
            count += 1
print(count)



