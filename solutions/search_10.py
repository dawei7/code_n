"""Solution for search_10: Sublist Search.

Find the first index where ``sub`` appears as a contiguous run
in ``data``, or -1 if it never does. Sliding window of length m
scanned across an n-length list.
Source: https://www.geeksforgeeks.org/search-an-element-in-a-list/

Inputs passed to solve():
    data: list-like of n random integers.
    sub: list-like of m integers to find inside data.
    n: length of data.
    m: length of sub (m <= n).

Goal:
    the first index i where data[i:i+m] == sub, or -1 if not present.

Samples:
Sample 1 input:  data = [1, 2, 3, 4, 5, 6], sub = [3, 4, 5], n = 6, m = 3
Sample 1 output: 2

Sample 2 input:  data = [1, 2, 3, 4, 5], sub = [4, 5, 6], n = 5, m = 3
Sample 2 output: -1

Sample 3 input:  data = [1, 2, 3], sub = [1, 2, 3], n = 3, m = 3
Sample 3 output: 0

"""

def solve(data, sub, n, m):
    # Write your code here.
    return None
