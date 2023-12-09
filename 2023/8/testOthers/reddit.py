ll = [x for x in open("input").read().strip().split('\n\n')]
import math
inst = list(ll[0])
conn = {}
def solvesteps(start):
	pos = start
	idx = 0
	while not pos.endswith('Z'):
		d = inst[idx%len(inst)]
		pos = conn[pos][0 if d=='L' else 1]
		idx += 1
	return idx
ret = 1
for start in conn:
	if start.endswith('A'):
		ret = math.lcm(ret, solvesteps(start))
print("p2", ret)