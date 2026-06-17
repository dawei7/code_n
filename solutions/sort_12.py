"""Solution for sort_12: Pancake Sort.

Sort using only 'flip' operations: reverse the prefix
[0..k] for any k. Strategy: for each max value, flip it
to the front, then flip the whole unsorted prefix to
drop it into its sorted slot at the end.
Requirement: O(n^2) flips, O(1) extra space.
Source: https://www.geeksforgeeks.org/pancake-sorting/

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
