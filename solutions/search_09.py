"""Solution for search_09: Fibonacci Search.

Sorted array; uses Fibonacci numbers to split the range. Always
shrinks by at least one Fibonacci number, so the loop runs in
O(log n) time. The split is by index, not value, so the only
operation is the standard '<=' comparison.
Source: https://www.geeksforgeeks.org/fibonacci-search/

Inputs passed to solve():
    data: sorted list-like of n random integers.
    target: value to find in data.
    n: length of data.

Goal:
    the index of target in data, or -1 if not found.

Samples:
Sample 1 input:  data = [1, 4, 7, 9, 12, 15, 18, 22, 25, 30], target = 22
Sample 1 output: 7

Sample 2 input:  data = [1, 4, 7, 9, 12, 15, 18, 22, 25, 30], target = 13
Sample 2 output: -1

Sample 3 input:  data = [1, 4, 7, 9, 12, 15, 18, 22, 25, 30], target = 1
Sample 3 output: 0

"""

def solve(data, target, n):
    # Write your code here.
    return None
