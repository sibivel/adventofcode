import sys
import re

inputs = [line.strip() for line in sys.stdin]
seeds = [int(seed) for seed in re.search(
    'seeds: ([\d\s]+)', inputs[0]).groups()[0].split()]

i = 0
while inputs[i] != 'seed-to-soil map:':
    i += 1
i += 1

maps = [{}, {}, {}, {}, {}, {}, {}]

mapI = 0
while mapI < 7:
    print(maps)
    while i < len(inputs) and inputs[i] != '':
        destination, source, r = inputs[i].split()
        maps[mapI][int(source)] = (int(destination), int(r))
        i += 1
    i += 2
    mapI += 1
lowest = None
for seed in seeds:
    mapI = 0
    source = seed
    while mapI < 7:
        map = maps[mapI]
        done = False
        for k in map:
            if k < source and source < k + map[k][1]:
                source = (map[k][0] - k) + source
                mapI += 1
                done = True
                break
        if not done:
            mapI += 1
    location = source
    if lowest is None:
        lowest = location
    else: 
        lowest = min(lowest, location)
print(lowest)
            
        
            
