"""Solution for search_07: Exponential Search.

For unbounded / infinite sorted arrays: double the index until the upper bound is past the target, then binary-search inside it. O(log n) time, no need to know n up front.
Source: https://www.geeksforgeeks.org/exponential-search/

Inputs passed to solve():
    data: sorted list-like of n random integers.
    target: value to find in data.
    n: length of data.

Goal:
    the index of target in data, or -1 if not found.

Samples:
Sample 1 input:  data = [2, 4, 6, 8, 10, 12, 14], target = 10
Sample 1 output: 4

Sample 2 input:  data = [2, 4, 6, 8, 10, 12, 14], target = 1
Sample 2 output: -1

Sample 3 input:  data = [2, 4, 6, 8, 10, 12, 14], target = 14
Sample 3 output: 6

"""

def solve(data, target, n):
    # Write your code here.
    return None
