import sys
import re
import numpy as np
sys.setrecursionlimit(10**9)

memo = {}
def solve(plot, nums, curCount=0, pi=0, ni=0):
    key = (curCount, pi, ni)
    if key in memo:
        return memo[key]
    
    if pi == len(plot):
        if ni == len(nums) and curCount == 0:
            memo[key] = 1
        elif ni == len(nums)-1 and curCount == nums[ni]:
            memo[key] = 1
        else:
            memo[key] = 0
    elif ni == len(nums):
        memo[key] = 1 if '#' not in plot[pi:] else 0
    elif curCount > nums[ni]:
        memo[key] = 0
    elif plot[pi] == '.':
        if curCount > 0:
            if nums[ni] != curCount:
                memo[key] = 0
            else:
                memo[key] = solve(plot, nums, 0, pi + 1, ni + 1)
        else:
            memo[key] = solve(plot, nums, 0, pi+1, ni)
    elif plot[pi] == '#':
        memo[key] = solve(plot, nums, curCount + 1, pi+1, ni)
    else:
        r = 0
        if curCount > 0:
            if nums[ni] == curCount:
                r += solve(plot, nums, 0, pi + 1, ni + 1)
        else:
            r += solve(plot, nums, 0, pi + 1, ni)
        r += solve(plot, nums, curCount + 1, pi+1, ni)
        memo[key] = r
    return memo[key]


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


inputs = [line.strip() for line in sys.stdin]
sum = 0
for line in inputs:
    plot, nums = line.split()
    plot = '?'.join([plot] * 5)
    nums = [int(x) for x in nums.split(',')] * 5
    memo = {}
    s = solve(plot, nums)
    print(s)
    sum += s

print(sum)
# print(isValid([*'#.#.###'], [1,1,3]))


# print(0)
