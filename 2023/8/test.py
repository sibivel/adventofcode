import sys
import re
import math

    

inputs = [line.strip() for line in sys.stdin]
v = []
instructions = inputs[0]

map = {}
starts = []
for line in inputs[2:]:
    k = line[0:3]
    l = line[7:10]
    r = line[12:15]
    if k[2] == 'A':
        starts.append(k)
    # print(k, l, r)
    map[k] = (l, r)

curs = set(starts)
seen = set()
count = 0
si = 0
for start in starts:
    cur = start
    count = 0
    si = 0
    while cur[2] != 'Z':
        if instructions[si] == 'L':
            cur = map[cur][0]
        else:
            cur = map[cur][1]
        si += 1
        if si == len(instructions):
            si = 0
        count += 1
    print(count)
    v.append(count)
print(v)
print(math.lcm(*v))
