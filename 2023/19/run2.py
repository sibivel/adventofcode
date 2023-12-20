import sys
import re
import numpy as np
sys.setrecursionlimit(10**9)

def eval(fakePart, workflows): # returns new list of fake parts OR a char 'A' or 'R' if it is evaluatable.
    workflowName = 'in'
    while workflowName != 'R' and workflowName != 'A':
        res = evalOne(fakePart, workflows[workflowName])
        if isinstance(res, str):
            workflowName = res
        else:
            return res
    if workflowName == 'A':
        return True
    return False


def evalOne(fakePart, workflow):
    for phrase in workflow[0]:
        char, greaterThan, value, target = phrase
        lower, upper = fakePart[char]
        if lower > upper:
            return []
        if greaterThan:
            if lower > value:
                return target
            elif upper <= value:
                continue
            else:
                a = dict(fakePart)
                a[char] = (lower, value)
                b = dict(fakePart)
                b[char] = (value+1, upper)
                return [a, b]
        else:
            if upper < value:
                return target
            elif lower >= value:
                continue
            else:
                a = dict(fakePart)
                a[char] = (lower, value-1)
                b = dict(fakePart)
                b[char] = (value, upper)
                return [a, b]
    return workflow[1]
        
def countFakePart(fakePart):
    print(fakePart)
    count = 1
    for c in 'xmas':
        count *= fakePart[c][1] - fakePart[c][0] + 1
    return count

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

queue = [{
    'x': (1, 4000),
    'm': (1, 4000),
    'a': (1, 4000),
    's': (1, 4000),
}]
result = 0
while len(queue) > 0:
    print(queue)
    fakePart = queue.pop()
    res = eval(fakePart, workflows)
    if isinstance(res, bool):
        if res:
            nv = countFakePart(fakePart)
            print(nv)
            result += nv
        else:
            continue
    else:
        for newFakePart in res:
            queue.append(newFakePart)
print(result)


# result = 0
# for i in range(partsStart, R):
#     x, m, a, s = re.search("\{x\=(\d+),m\=(\d+),a\=(\d+),s\=(\d+)\}", inputs[i]).groups()
#     x = int(x)
#     m = int(m)
#     a = int(a)
#     s = int(s)
#     print((x,m,a,s))
#     part = {
#         'x':x,
#         'm':m,
#         'a':a,
#         's':s
#     }
#     val = eval(part, workflows)
#     print(val)
#     result += val
# print(result)



