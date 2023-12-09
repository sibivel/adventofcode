import sys
import re

inputs = [line.strip() for line in sys.stdin]

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
done = False
print(curs)
while (not done):
    newcurs = set()
    for cur in curs:
        if instructions[si] == 'L':
            newcurs.add(map[cur][0])
        else:
            newcurs.add(map[cur][1])
    curs = newcurs
    print(curs)
    if (str(sorted(curs)) in seen):
        break
    seen.add(str(sorted(curs)))
    si += 1
    if si == len(instructions):
        si = 0
    count += 1
    done = True
    for c in curs:
        if c[2] != 'Z':
            done = False
            break
print(count)
