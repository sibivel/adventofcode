import sys
import re

# races = [(7, 9), (15,40), (30,200)]
races = [(55, 401), (99, 1485), (97, 2274), (93, 1405)]
result = 1
for race in races:
    T, D = race
    count = 0
    for time in range(T):
        speed = T - time
        dist = speed * time
        if dist > D:
            count += 1
    print(count)
    result = result * count

print(result)
