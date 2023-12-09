import sys
import re

inputs = [line.strip() for line in sys.stdin]

instructions = inputs[0]

map = {}
for line in inputs[2:]:
    k = line[0:3]
    l = line[7:10]
    r = line[12:15]
    print(k, l, r)
    map[k] = (l, r)

cur = 'AAA'
count = 0
si = 0
while (cur != 'ZZZ'):
    if instructions[si] == 'L':
        cur = map[cur][0]
    else:
        cur = map[cur][1]
    si += 1
    if si == len(instructions):
        si = 0
    count += 1
print(count)
