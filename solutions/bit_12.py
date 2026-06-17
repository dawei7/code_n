"""Solution for bit_12: Reverse Bits.

Reverse the bits of a 32-bit unsigned integer n.
For each of the 32 bit positions, take bit i of n
and place it at bit (31 - i) of the result.
O(1) (a fixed number of bitwise ops).
Source: https://www.geeksforgeeks.org/reverse-bits-of-an-integer/

Inputs passed to solve():
    n: non-negative integer (treated as 32-bit unsigned).

Goal:
    n with its 32 bits reversed (LSB goes to MSB).

Samples:
Sample 1 input:  n = 0b00000010100101000001111010011100 (43261596)
Sample 1 output: 964176192 (binary 00111001011110000010100101000000)

Sample 2 input:  n = 0
Sample 2 output: 0

Sample 3 input:  n = 1 (binary 1, only the LSB set)
Sample 3 output: 2^31 = 2147483648

"""

def solve(n):
    # Write your code here.
    return None
