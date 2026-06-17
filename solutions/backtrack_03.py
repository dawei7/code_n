"""Solution for backtrack_03: Combination Sum.

Given a list of positive integers (sorted) and a target, return
every unique combination of values that sums to target. Each
value may be used any number of times. Recurse forward only
(i >= start) to avoid duplicate combinations. Output is a
list of combinations; each combination is sorted.
Requirement: O(2^target) worst case.
Source: https://www.geeksforgeeks.org/combinational-sum/

Inputs passed to solve():
    candidates: list of n sorted positive integers (uniques).
    target: target sum (always reachable in the setup).
    n: length of candidates.

Goal:
    a list of unique combinations (each a list) that sum to target.

Samples:
Sample 1 input:  candidates = [2, 3, 6, 7], target = 7, n = 4
Sample 1 output: [[2, 2, 3], [7]]

Sample 2 input:  candidates = [2, 3, 5], target = 8, n = 3
Sample 2 output: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]


"""

def solve(candidates, target, n):
    # Write your code here.
    return None
