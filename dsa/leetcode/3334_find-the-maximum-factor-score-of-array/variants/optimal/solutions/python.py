import math
from functools import reduce

def get_gcd(a, b):
    return math.gcd(a, b)

def get_lcm(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // math.gcd(a, b)

def calculate_score(arr):
    if not arr:
        return 0
    g = reduce(math.gcd, arr)
    l = reduce(get_lcm, arr)
    return g * l

def solve(nums: list[int]) -> int:
    # Calculate score for the full array
    max_score = calculate_score(nums)
    
    # Try removing each element one by one
    for i in range(len(nums)):
        subset = nums[:i] + nums[i+1:]
        if not subset:
            continue
        max_score = max(max_score, calculate_score(subset))
        
    return max_score
