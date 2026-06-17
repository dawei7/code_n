"""Solution for sort_13: Tim Sort (Simplified).

Tim Sort: divide into runs (already-sorted subsequences),
then merge with a stack-based merge policy. This simplified
version uses Python's built-in sorted() for each run
and merges them, demonstrating the O(n log n) average
case and O(n) on already-sorted data.
Source: https://www.geeksforgeeks.org/tim-sort/

Inputs passed to solve():
    data: list-like of n random integers. Mutate in place.
    n: length of data.

Goal:
    the same data object, sorted in place (in ascending order).

Samples:
Sample 1 input:  data = [3, 1, 2], n = 3
Sample 1 output: [1, 2, 3]

Sample 2 input:  data = [5, 5, 2, 9], n = 4
Sample 2 output: [2, 5, 5, 9]

Sample 3 input:  data = [8, 4, 7, 1, 3], n = 5
Sample 3 output: [1, 3, 4, 7, 8]

"""

def solve(data, n):
    # Write your code here.
    return None
