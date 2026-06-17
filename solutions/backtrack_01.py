"""Solution for backtrack_01: Subset Sum (Decision).

Given a list of positive integers and a target, return True
iff some subset of the list sums exactly to target. The setup
always picks a reachable target (prefix-sum of a random
split), so the answer is True.
Requirement: O(2^n) time, O(n) recursion stack.
Source: https://www.geeksforgeeks.org/subset-sum-problem-dp-25/

Inputs passed to solve():
    arr: list of n positive integers.
    target: target sum (always reachable in the setup).
    n: length of arr.

Goal:
    True iff some subset of arr sums to target.

Samples:
Sample 1 input:  arr = [3, 34, 4, 12, 5, 2], target = 9, n = 6
Sample 1 output: True (4+5)

Sample 2 input:  arr = [1, 2, 3], target = 7, n = 3
Sample 2 output: False (reachable by 1+2+3=6, but target is 7)


"""

def solve(arr, target, n):
    # Write your code here.
    return None
