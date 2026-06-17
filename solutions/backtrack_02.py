"""Solution for backtrack_02: Permutations.

Return every ordering of ``arr`` as a list of lists. The
setup uses distinct elements so we don't have to dedupe.
Outer list is sorted so the verify can compare directly.
Requirement: O(n! * n) time.
Source: https://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/

Inputs passed to solve():
    arr: list of n distinct integers.
    n: length of arr (capped at 6 because n! grows fast).

Goal:
    a list of n! permutations (each a list), sorted.

Samples:
Sample 1 input:  arr = [1, 2, 3], n = 3
Sample 1 output: [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]

Sample 2 input:  arr = [1, 2], n = 2
Sample 2 output: [[1,2], [2,1]]


"""

def solve(arr, n):
    # Write your code here.
    return None
