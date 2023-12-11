import sys
import re
sys.setrecursionlimit(10**9)


def run(inputs, startR, startC, bigInput):
    queue = [(startR, startC-1, 1), (startR+1, startC, 1)]
    m = 0
    while len(queue) > 0:
        r, c, d = queue.pop()
        char = inputs[r][c]
        if r < 0 or r >= len(inputs) or c < 0 or c >= len(inputs[0]):
            continue
        if isinstance(char, int):
            continue
        if char == '.':
            continue
        inputs[r][c] = d
        m = max(m, d)
        if char == '|':
            bigInput[r*3+1][c*3+1] = 'X'
            bigInput[r*3][c*3+1] = 'X'
            bigInput[r*3+2][c*3+1] = 'X'
            queue.insert(0, (r-1, c, d+1))
            queue.insert(0, (r+1, c, d+1))
        if char == '-':
            bigInput[r*3+1][c*3+1] = 'X'
            bigInput[r*3+1][c*3] = 'X'
            bigInput[r*3+1][c*3+2] = 'X'
            queue.insert(0, (r, c-1, d+1))
            queue.insert(0, (r, c+1, d+1))
        if char == 'L':
            bigInput[r*3+1][c*3+1] = 'X'
            bigInput[r*3][c*3+1] = 'X'
            bigInput[r*3+1][c*3+2] = 'X'
            queue.insert(0, (r-1, c, d+1))
            queue.insert(0, (r, c+1, d+1))
        if char == 'J':
            bigInput[r*3+1][c*3+1] = 'X'
            bigInput[r*3][c*3+1] = 'X'
            bigInput[r*3+1][c*3] = 'X'
            queue.insert(0, (r-1, c, d+1))
            queue.insert(0, (r, c-1, d+1))
        if char == '7':
            bigInput[r*3+1][c*3+1] = 'X'
            bigInput[r*3+1][c*3] = 'X'
            bigInput[r*3+2][c*3+1] = 'X'
            queue.insert(0, (r, c-1, d+1))
            queue.insert(0, (r+1, c, d+1))
        if char == 'F':
            bigInput[r*3+1][c*3+1] = 'X'
            bigInput[r*3+1][c*3+2] = 'X'
            bigInput[r*3+2][c*3+1] = 'X'
            queue.insert(0, (r, c+1, d+1))
            queue.insert(0, (r+1, c, d+1))
    return m


def countArea(bigInput):
    R = len(bigInput)
    C = len(bigInput[0])
    sum = 0
    for r in range(R):
        for c in range(C):
            visited = set()
            x = fillArea(bigInput, r, c, R, C, visited)
            for nr, nc in visited:
                bigInput[nr][nc] = '_' if x == -1 else 'O'
            if bigInput[r][c] == 'O' and (r-1) % 3 == 0 and (c-1) % 3 == 0:
                sum += 1
    print(sum)

def fillArea(bigInput, r, c, R, C, visited: set):
    if r < 0 or r >= R or c < 0 or c >= C:
        return -1
    if bigInput[r][c] == '_':
        return -1
    if bigInput[r][c] != '.':
        return 0
    if (r, c) in visited:
        return 0
    sum = 1
    # print(r, c)
    visited.add((r, c))
    for dr, dc in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        nr = r + dr
        nc = c + dc
        x = fillArea(bigInput, nr, nc, R, C, visited)
        if x == -1:
            return -1
        sum += x
    return sum


inputs = [[*line.strip()] for line in sys.stdin]
C = len(inputs[0])
bigInput = []
for r in range(len(inputs)*3):
    bigInput.append([])
    for c in range(C*3):
        bigInput[r].append('.')
for row in range(len(inputs)):
    for col in range(len(inputs[row])):
        if inputs[row][col] == 'S':
            inputs[row][col] = 0
            bigInput[row*3+1][col*3+1] = 'X'
            bigInput[row*3+1][col*3+0] = 'X'
            bigInput[row*3+2][col*3+1] = 'X'
            print(run(inputs, row, col, bigInput))
# for i in bigInput:
#     print(i)
countArea(bigInput)
# fillArea(bigInput, 9, 20, len(bigInput), len(bigInput[0]))
# for i in bigInput:
#     print(i)


# print(0)
