"""Solution for bit_11: Bitwise AND of Range.

Given two non-negative integers left and right
with left <= right, return the bitwise AND of all
integers in the inclusive range [left, right].
The result is the common prefix (most significant
bits) of left and right, shifted into place. To
find it: keep clearing the lowest differing bit of
left while left > right; that's the common prefix.
Source: https://www.geeksforgeeks.org/bitwise-and-of-numbers-range/

Inputs passed to solve():
    left: left bound of the range (inclusive).
    right: right bound of the range (inclusive, >= left).

Goal:
    the bitwise AND of all integers in [left, right].

Samples:
Sample 1 input:  left = 5, right = 7
Sample 1 output: 4 (binary 101 AND 110 AND 111 = 100)

Sample 2 input:  left = 0, right = 0
Sample 2 output: 0

Sample 3 input:  left = 1, right = 1
Sample 3 output: 1
Sample 4 input:  left = 12, right = 15
Sample 4 output: 12 (all 1100..1111 share 1100)

"""

def solve(left, right):
    # Write your code here.
    return None
