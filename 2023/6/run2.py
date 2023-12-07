import sys
import re

# race = (71530, 940200)
race = (55999793, 401148522741405)
result = 1
T, D = race
count = 0
for time in range(T):
    speed = T - time
    dist = speed * time
    if dist > D:
        count += 1
print(count)
