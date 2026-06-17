"""Solution for bit_01: Count Set Bits.

Count the number of 1-bits in the binary
representation of the input integer n. Also known
as the Hamming weight or population count.
Walk through the bits: while n, count += n & 1;
n >>= 1. O(log n) bit-walks, comfortably within O(n).
Source: https://www.geeksforgeeks.org/count-set-bits-in-an-integer/

Inputs passed to solve():
    n: non-negative integer.

Goal:
    the number of 1-bits in n's binary representation.

Samples:
Sample 1 input:  n = 7
Sample 1 output: 3 (binary 111)

Sample 2 input:  n = 8
Sample 2 output: 1 (binary 1000)

Sample 3 input:  n = 0
Sample 3 output: 0

"""

def solve(n):
    # Write your code here.
    return None
