import sys
import re
import numpy as np
sys.setrecursionlimit(10**9)

def solve(plot, nums, i):
    if i < len(plot):
        if plot[i] == '?':
            score = 0
            plot[i] = '.'
            score += solve(plot, nums, i+1)
            plot[i] = '#'
            score += solve(plot, nums, i+1)
            plot[i] = '?'
            return score
        else:
            return solve(plot, nums, i+1)
    else:
        return 1 if isValid(plot, nums) else 0

def isValid(plot, nums):
    s = "".join(plot)
    parts = [p for p in s.split('.') if len(p) > 0]
    # print(parts)
    if len(parts) != len(nums):
        return False
    for part, num in zip(parts, nums):
        if len(part) != num:
            return False
    return True
    # ni = 0
    # count = 0
    # for c in plot:
    #     if c == '#':
    #         count += 1
    #     elif count > 0:
    #         if ni == len(nums) or nums[ni] != count:
    #             return False
    #         else:
    #             ni += 1
    #             count = 0
        
    # if count > 0 and ni < len(nums) and nums[ni] == count:
    #     ni += 1
    #     count = 0
    # return ni == len(nums)
        
            



inputs =[line.strip() for line in sys.stdin]
sum = 0
for line in inputs:
    plot, nums = line.split()
    plot = [*plot]
    nums = [int(x) for x in nums.split(',')]
    s = solve(plot, nums, 0)
    print(s)
    sum += s

print(sum)
# print(isValid([*'#.#.###'], [1,1,3]))
    
        

# print(0)
