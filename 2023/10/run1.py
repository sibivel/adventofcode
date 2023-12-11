import sys
import re


def run(inputs, startR, startC):
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
            queue.insert(0, (r-1, c, d+1))
            queue.insert(0, (r+1, c, d+1))
        if char == '-':
            queue.insert(0, (r, c-1, d+1))
            queue.insert(0, (r, c+1, d+1))
        if char == 'L':
            queue.insert(0, (r-1, c, d+1))
            queue.insert(0, (r, c+1, d+1))
        if char == 'J':
            queue.insert(0, (r-1, c, d+1))
            queue.insert(0, (r, c-1, d+1))
        if char == '7':
            queue.insert(0, (r, c-1, d+1))
            queue.insert(0, (r+1, c, d+1))
        if char == 'F':
            queue.insert(0, (r, c+1, d+1))
            queue.insert(0, (r+1, c, d+1))    
    return m


inputs = [[*line.strip()] for line in sys.stdin]


for row in range(len(inputs)):
    for col in range(len(inputs[row])):
        if inputs[row][col] == 'S':
            inputs[row][col] = 0
            print(run(inputs, row, col))
            # print(inputs)
            


# print(0)
