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

def cycle(inputs):
    R, C = inputs.shape
    for c in range(C):
        inputs[:,c] = tilt(inputs[:,c])
    for r in range(R):
        inputs[r] = tilt(inputs[r])
    for c in range(C):
        inputs[:,c] = np.flip(tilt(np.flip(inputs[:,c])))
    for r in range(R):
        inputs[r] = np.flip(tilt(np.flip(inputs[r])))
    return inputs
    

inputs = np.array([[*line.strip()] for line in sys.stdin])

R, C = inputs.shape

tilted = np.copy(inputs)
count = 0
history = [tilted]
# while count < (3 + (1000000000 - 3) % 7):
while count < (120 + (1000000000 - 120) % 42):
    old = tilted
    tilted = cycle(np.copy(old))
    done = False
    for i in range(len(history)):
        t = history[i]
        if np.array_equal(t, tilted):
            print(count, i)
            # done = True
            break
    history.append(tilted)
    if done:
        break
    count += 1

sum = 0
for r in range(R):
    s = np.sum(tilted[r] == 'O') * (R-r)
    print(s)
    sum += s
print(sum)

# Example cycle start at 9th = 3
# 3 - 1 + (1000000000 % 6)
# Cycle starts at 161th cycle == 120th cycle
# 120 - 1 + (1000000000 % 41)

print(0)
    
    



