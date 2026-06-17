"""Solution for search_08: Interpolation Search.

Like binary search, but the probe position is estimated from the target's value, not the midpoint. O(log log n) average on uniformly distributed data; degenerates to O(n) on pathological inputs.
Source: https://www.geeksforgeeks.org/interpolation-search/

Inputs passed to solve():
    data: sorted list-like of n random integers.
    target: value to find in data.
    n: length of data.

Goal:
    the index of target in data, or -1 if not found.

Samples:
Sample 1 input:  data = [10, 20, 30, 40, 50], target = 30
Sample 1 output: 2

Sample 2 input:  data = [10, 20, 30, 40, 50], target = 35
Sample 2 output: -1

Sample 3 input:  data = [10, 20, 30, 40, 50], target = 10
Sample 3 output: 0

"""

def solve(data, target, n):
    # Write your code here.
    return None
