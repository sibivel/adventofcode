import sys
import re
import numpy as np
sys.setrecursionlimit(10**9)

def tilt(array):
    L = array.shape[0]
    i = 0
    while i < L:
        if array[i] == 'O' and i > 0 and array[i-1] == '.':
            array[i-1] = 'O'
            array[i] = '.'
            i -= 1
        else:
            i += 1
    return array
            
    

inputs = np.array([[*line.strip()] for line in sys.stdin])

R, C = inputs.shape

tilted = np.empty((R,C), str)


# print(inputs[:,0].shape)
for c in range(C):
    tilted[:,c] = tilt(inputs[:,c])
sum = 0
for r in range(R):
    s = np.sum(tilted[r] == 'O') * (R-r)
    print(s)
    sum += s

print(sum)
    
    



