import sys
import re
import numpy as np
sys.setrecursionlimit(10**9)

def hash(s):
    cv = 0
    for c in s:
        cv += ord(c)
        cv = cv * 17
        cv = cv % 256
    return cv

def findLabel(box, label):
    for i in range(len(box)):
        if box[i][0] == label:
            return i
    return None

inputs = [line.strip() for line in sys.stdin]

strings = inputs[0].split(',')
print(strings)
sum = 0
boxes = []
for i in range(256):
    boxes.append([])
for s in strings:
    if s[-1].isdigit():
        label = s[0:-2]
        focal = int(s[-1])
        h = hash(label)
        i = findLabel(boxes[h], label)
        if i is None:
            boxes[h].append((label, focal))
        else:
            boxes[h][i] = (label, focal)
    else:
        label = s[0:-1]
        h = hash(label)
        i = findLabel(boxes[h], label)
        if not i is None:
            boxes[h].pop(i)
print(boxes)
for i in range(256):
    box = boxes[i]
    for j in range(len(box)):
        b = box[j]
        sum += (i+1) * (j+1) * b[1]
print(sum)
    
    



