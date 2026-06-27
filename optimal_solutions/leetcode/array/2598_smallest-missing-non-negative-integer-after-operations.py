from collections import Counter

def solve(nums: list[int], value: int) -> int:
    # Calculate the remainder of each number modulo 'value'.
    # Since we can add/subtract 'value' infinitely, any number x
    # can be transformed into any number y such that y % value == x % value.
    # We use (n % value) to handle negative numbers correctly in Python.
    counts = Counter(n % value for n in nums)
    
    # We want to find the smallest non-negative integer 'mex'
    # such that we cannot form 'mex'.
    # We can form 'mex' if we have at least one number with remainder (mex % value).
    # Specifically, if we have 'k' numbers with remainder 'r', we can form
    # the values r, r + value, r + 2*value, ..., r + (k-1)*value.
    
    mex = 0
    while True:
        remainder = mex % value
        if counts[remainder] > 0:
            counts[remainder] -= 1
            mex += 1
        else:
            return mex
