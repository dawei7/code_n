"""Solution for bit_02: Power of Two Check.

Return True iff the input n is a power of two.
A single bitwise trick covers the whole problem:
n is a power of two iff n > 0 and (n & (n - 1)) == 0.
Why? Powers of two have exactly one bit set, so
n - 1 clears that bit and only that bit, and the
AND with n is 0. O(1).
Source: https://www.geeksforgeeks.org/program-to-find-whether-a-no-is-power-of-two/

Inputs passed to solve():
    n: non-negative integer.

Goal:
    True iff n is a power of two (1, 2, 4, 8, ...).

Samples:
Sample 1 input:  n = 1
Sample 1 output: True

Sample 2 input:  n = 16
Sample 2 output: True

Sample 3 input:  n = 6
Sample 3 output: False

"""

def solve(n):
    # Write your code here.
    return None
