"""Solution for search_06: Jump Search.

Sorted array; jump ahead by a fixed block size m = sqrt(n) until the block could contain the target, then linear-scan inside it.
O(sqrt(n)) time, O(1) extra space. Useful when 'jump back' is expensive (e.g. rotating media).
Source: https://www.geeksforgeeks.org/jump-search/

Inputs passed to solve():
    data: sorted list-like of n random integers.
    target: value to find in data.
    n: length of data.

Goal:
    the index of target in data, or -1 if not found.

Samples:
Sample 1 input:  data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], target = 7
Sample 1 output: 7

Sample 2 input:  data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], target = 10
Sample 2 output: -1

Sample 3 input:  data = [5, 10, 15, 20, 25], target = 20
Sample 3 output: 3

"""

def solve(data, target, n):
    # Write your code here.
    return None
