"""
Description
-----------
Given three square n x n matrices A, B, C,
            determine if C = A * B. Freivald's Monte Carlo
            algorithm: generate a random n x 1 vector r with
            entries 0 or 1. Compute p = A * (B * r) - C * r.
            If p is the zero vector, return True (but this may
            be a false positive with low probability). Otherwise
            return False. Repeat trials times and accept if
            ALL iterations return True (or accept if ANY
            iteration returns False). O(n^2) per iteration.
            Source: https://www.geeksforgeeks.org/dsa/freivalds-algorithm/

Examples
--------
Example 1:
Input:  A = [[1, 1], [1, 1]], B = [[1, 1], [1, 1]], C = [[2, 2], [2, 2]], n = 2, trials = 5, seed_value = 42
Output: True

Example 2:
Input:  A = [[1, 1], [1, 1]], B = [[1, 1], [1, 1]], C = [[2, 2], [2, 3]], n = 2, trials = 5, seed_value = 42
Output: False (C is not A*B)
"""

def solve(mat_a, mat_b, mat_c, size, trials, seed_value):
    # Write your code here.
    return None
