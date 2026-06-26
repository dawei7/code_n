"""
Description
-----------
Multiply two 2x2 matrices using Strassen's algorithm
            (7 recursive products instead of the schoolbook 8).
            O(n^log2(7)) ~ O(n^2.807) time, which beats O(n^3)
            for large n. For the small n in the test gauntlet
            the constant factor dominates, so this is a teaching
            challenge, not a speedup.
            Source: https://www.geeksforgeeks.org/strassens-matrix-multiplication/

Examples
--------
Example 1:
Input:  a_mat = [[1, 2], [3, 4]], b_mat = [[5, 6], [7, 8]], n = 2
Output: [[19, 22], [43, 50]]

Example 2:
Input:  a_mat = [[0, 1], [1, 0]], b_mat = [[0, 1], [1, 0]], n = 2
Output: [[1, 0], [0, 1]]
"""

def solve(a_mat, b_mat, n):
    # Write your code here.
    return None
