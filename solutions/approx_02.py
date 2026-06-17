"""Solution for approx_02: Set Cover (Greedy).

Find a set of indices that cover every element of
``universe``. Greedy: each step picks the set covering
the most uncovered elements. Standard O(log n) approx
ratio for the classical Set Cover problem.
Source: https://www.geeksforgeeks.org/set-cover-problem-set-1-greedy-approximate-algorithm/

Inputs passed to solve():
    universe: list of k unique element IDs (0..k-1).
    sets: list of m sets, each a list of element IDs.
    m: number of sets.
    k: size of universe.

Goal:
    a sorted list of chosen set indices covering universe.

Samples:
Sample 1 input:  universe = [0, 1, 2, 3, 4], sets = [[0, 1], [1, 2, 3], [2, 3, 4], [0, 4]], m = 4, k = 5
Sample 1 output: [0, 1, 2] (or 1 + 2)


"""

def solve(universe, sets, m, k):
    # Write your code here.
    return None
