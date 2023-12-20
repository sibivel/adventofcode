import sys
import re
import numpy as np
sys.setrecursionlimit(10**9)

def eval(part, workflows):
    workflowName = 'in'
    while workflowName != 'R' and workflowName != 'A':
        workflowName = evalOne(part, workflows[workflowName])
    if workflowName == 'A':
        print(part.values())
        return sum([*part.values()])
    return 0


def evalOne(part, workflow):
    print(part)
    for phrase in workflow[0]:
        char, greaterThan, value, target = phrase
        if greaterThan:
            if part[char] > value:
                return target
        else:
            if part[char] < value:
                return target
    return workflow[1]
        

inputs = [line.strip() for line in sys.stdin]
R, C = (len(inputs), len(inputs[0]))
# inputs = np.array([[*line.strip()] for line in sys.stdin])
# R, C = inputs.shape
# print(R, C)

workflows = {}
partsStart = 0
for i in range(R):
    if inputs[i] == '':
        partsStart = i+1
        break
    name, rest = re.search("(\w+)\{(.+)\}", inputs[i]).groups()
    # print(name, rest)
    parts = rest.split(',')
    workflow = []
    for rule in parts[:-1]:
        exp, target = rule.split(':')
        char = exp[0]
        symbol = exp[1]
        greaterThan = symbol == '>'
        value = int(exp[2:])
        workflow.append((char, greaterThan, value, target))
    workflows[name] = (workflow, parts[-1])

print(workflows)
result = 0
for i in range(partsStart, R):
    x, m, a, s = re.search("\{x\=(\d+),m\=(\d+),a\=(\d+),s\=(\d+)\}", inputs[i]).groups()
    x = int(x)
    m = int(m)
    a = int(a)
    s = int(s)
    print((x,m,a,s))
    part = {
        'x':x,
        'm':m,
        'a':a,
        's':s
    }
    val = eval(part, workflows)
    print(val)
    result += val
print(result)

