"""Solution for greedy_11: Egyptian Fraction.

Represent a rational number ``p/q`` (with p, q > 0) as a sum of
distinct unit fractions ``1/d_i``. The greedy algorithm picks
the smallest unit fraction ``>= p/q`` at each step, which is
``1 / ceil(q/p)``, and recurses on the remainder.
Requirement: O(q) iterations in the worst case.
Source: https://www.geeksforgeeks.org/greedy-algorithms-set-2-kruskals-minimum-spanning-tree-algorithm/

Inputs passed to solve():
    p: numerator of the fraction (positive).
    q: denominator of the fraction (positive).

Goal:
    a list of unit-fraction denominators summing to p/q.

Samples:
Sample 1 input:  p = 2, q = 3
Sample 1 output: [2, 6]  (2/3 = 1/2 + 1/6)

Sample 2 input:  p = 6, q = 14
Sample 2 output: [3, 11, 231]  (6/14 = 1/3 + 1/11 + 1/231)

Sample 3 input:  p = 1, q = 2
Sample 3 output: [2]

"""

def solve(p, q):
    # Write your code here.
    return None
