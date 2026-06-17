"""Solution for dp_06: Subset Sum.

Return True iff some subset of the input array sums to
the target. The setup always picks a reachable target,
so the canonical answer is always True.
Requirement: O(n * sum) where sum is the total of arr.
Source: https://www.geeksforgeeks.org/subset-sum-problem-dp-25/

Inputs passed to solve():
    arr: list of positive integers.
    target: the sum to check for (always reachable in tests).

Goal:
    True iff a subset of arr sums to target.

Samples:
Sample 1 input:  arr = [3, 34, 4, 12, 5, 2], target = 9
Sample 1 output: True (4+5)

Sample 2 input:  arr = [3, 34, 4, 12, 5, 2], target = 30
Sample 2 output: False

Sample 3 input:  arr = [1, 2, 3], target = 6
Sample 3 output: True (1+2+3)

"""

def solve(arr, target):
    # Write your code here.
    return None
