import sys
import re
import numpy as np
import math
sys.setrecursionlimit(10**9)


inputs = [line.strip() for line in sys.stdin]
R, C = (len(inputs), len(inputs[0]))
# inputs = np.array([[*line.strip()] for line in sys.stdin])
# R, C = inputs.shape
# print(R, C)

modules = {}
for input in inputs:
    if input.startswith('broadcaster'):
        outputs = [s.strip() for s in input.split('->')[1].strip().split(',')]
        modules['broadcaster'] = ['b', outputs, False, {}]
        continue
    mtype, name, outputString = re.search("(.)(\w+) \-\> (.*)", input).groups()
    outputs = [s.strip() for s in outputString.split(',')]
    # mtype, outputs, isHigh, inputsState
    modules[name] = [mtype, outputs, False, {}]

for name in modules:
    outputs = modules[name][1]
    for o in outputs:
        if o not in modules:
            continue
        modules[o][3][name] = False

# print(modules)
lowCount = 0
highCount = 0
sequences = {
    'bt': [0],
    'dl': [0],
    'fr': [0],
    'rv': [0],
}
dsequences = {
    'bt': [],
    'dl': [],
    'fr': [],
    'rv': [],
}
for press in range(10000):
    lowCount += 1
    pulses = [('broadcaster', False, o) for o in modules['broadcaster'][1]]
    while len(pulses) > 0:
        pulse = pulses.pop(0)
        # print(pulse)
        source, value, dest = pulse
        if value:
            highCount += 1
        else:
            lowCount += 1
        if dest not in modules:
            continue
        if modules[dest][0] == '%':
            if value == False:
                modules[dest][2] = not modules[dest][2]
                for o in modules[dest][1]:
                    pulses.append((dest, modules[dest][2], o))
        elif modules[dest][0] == '&':
            modules[dest][3][source] = value
            allHigh = all(modules[dest][3].values())
            for o in modules[dest][1]:
                pulses.append((dest, not allHigh, o))
        if (source in ['bt', 'dl', 'fr', 'rv'] and dest == 'rs' and value):
            print(press, modules['rs'][3])
            for k in modules['rs'][3]:
                if modules['rs'][3][k]:
                    sequences[k].append(press)
print(sequences)
# print(dsequences)

print(lowCount)
print(highCount)
print(lowCount * highCount)

print(math.lcm(*[sequences[k][1]+1 for k in sequences]))