import math


STEPS = 26501365
R = 131
filledMapE = 7652
filledMapO = 7699

# STEPS = 5000
# R = 11
# filledMapO = 40
# filledMapE = 42

start = int(R/2)

mapsInOneDir = (STEPS - start)/R
print(mapsInOneDir)
mapsInOneDir = int(mapsInOneDir)
totalMaps = 2 * mapsInOneDir + 1
# for i in range(1, mapsInOneDir + 1):
#     totalMaps += 1 + 2 * (mapsInOneDir-abs(i)+1)
totalMaps = filledMapE/4
for r in range(1, mapsInOneDir):
    if r % 2 == 0:
        totalMaps += filledMapE/2
    else:
        totalMaps += filledMapO/2
for r in range(1, mapsInOneDir):
    # totalMaps += (mapsInOneDir - r - 1) * (filledMapE + filledMapO) / 2
    # for c in range(1, mapsInOneDir-r):
    #     if (r+c) % 2 == 0:
    #         totalMaps += filledMapE
    #     else:
    #         totalMaps += filledMapO
    if (r+1 % 2) == (mapsInOneDir % 2):
        if (mapsInOneDir % 2) == 1:
            totalMaps += filledMapO
        else:
            totalMaps += filledMapE
    totalMaps += (mapsInOneDir - r - 1) * (filledMapE + filledMapO) / 2
print(totalMaps)
# totalMaps  = totalMaps * 2
print(4 * totalMaps)
print(4 * totalMaps)

