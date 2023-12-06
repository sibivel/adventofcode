import sys
import re

def squashMaps(map1: dict, map2: dict):
    result = {}
    map1keys = sorted(map1.keys())
    
    # for k in map1keys:
    #     d = map1[k][0]
    #     r = map1[k][1]
    #     usedKeys = []
    #     map2keys = sorted(map2.keys())
    #     for k2 in map2keys:
    #         if k2 >= d and k2 < d + r:
    #             result[k] = (map2[k2] + k2 - d, k2-d)
    #             k = k + k2 - d + 1
    #             d = k2 + 1
    #             r = r - (k2 - d)
    #             usedKeys = k2
    #     for usedKey in usedKeys:
    #         map2keys.remove(usedKey)
    #     result[k] = (d, r)
    # for k2 in map2keys:
    #     result[k2] = map2[k2]
    # return result

def isInRanges(k, ranges):
    for range in ranges:
        if k >= range[0] and k < range[0] + range[1]:
            return True
    return False

inputs = [line.strip() for line in sys.stdin]
seedRanges = [int(seed) for seed in re.search(
    'seeds: ([\d\s]+)', inputs[0]).groups()[0].split()]
i = 0
ranges = []
while i < len(seedRanges):
    ranges.append((seedRanges[i], seedRanges[i+1]))
    i += 2
print(ranges)
i = 0
while inputs[i] != 'seed-to-soil map:':
    i += 1
i += 1

maps = [{}, {}, {}, {}, {}, {}, {}]

mapI = 0
while mapI < 7:
    # print(maps)
    while i < len(inputs) and inputs[i] != '':
        destination, source, r = inputs[i].split()
        maps[mapI][int(source)] = (int(destination), int(destination) + int(r))
        i += 1
    i += 2
    mapI += 1
squashedMap = maps[0]
for j in range(6):
    squashedMap = squashMaps(squashedMap, maps[j+1])
print(squashedMap)
lowest = None
for k in squashedMap.keys():
    if isInRanges(k, ranges):
        if lowest is None:
            lowest = squashedMap[k][0]
        else:
            lowest = min(lowest, squashedMap[k][0])
if isInRanges(0, ranges) and not 0 in squashedMap:
    if lowest is None:
        lowest = 0
    else:
        lowest = min(lowest, 0)
# for seed in seeds:
#     mapI = 0
#     source = seed
#     while mapI < 7:
#         map = maps[mapI]
#         done = False
#         for k in map:
#             if k < source and source < k + map[k][1]:
#                 source = (map[k][0] - k) + source
#                 mapI += 1
#                 done = True
#                 break
#         if not done:
#             mapI += 1
#     location = source
#     if lowest is None:
#         lowest = location
#     else: 
#         lowest = min(lowest, location)
print(lowest)



        
        
        
        
            
