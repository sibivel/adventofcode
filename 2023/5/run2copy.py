import sys
import re
def mapValue(x, map: dict):
    for k in map.keys():
        if k <= x and x < k + map[k][1]:
            return map[k][0] - k + x
    return x
inputs = [line.strip() for line in sys.stdin]
seedRanges = [int(seed) for seed in re.search(
    'seeds: ([\d\s]+)', inputs[0]).groups()[0].split()]
i = 0
ranges = []
while i < len(seedRanges):
    ranges.append((seedRanges[i], seedRanges[i] + seedRanges[i+1]))
    i += 2
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
count = 0
newRanges = []
for map in maps:
    for r in ranges:
        nextRanges = []
        start = r[0]
        for k in sorted(map.keys()):
            if k < start and k+r > start:
                nextRanges.append((mapValue(start, map), k+r))
                start = 
            if k >= start and k < r[1]:
                poi.append
                start = k
for r in ranges:
    print(count)
    for seed in range(r[0], r[1]):
        mapI = 0
        source = seed
        while mapI < 7:
            map = maps[mapI]
            done = False
            for k in map:
                if k <= source and source < k + map[k][1]:
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
            # print(seed, location)
            lowest = min(lowest, location)
    count += 1
print(lowest)
            
        
            
