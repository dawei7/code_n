"""Solution for bit_07: Swap Odd and Even Bits.

Swap the odd and even bits of n. Bit 0 (LSB) goes
to bit 1, bit 1 goes to bit 0, and so on. Two mask
operations: isolate the even bits with 0x5555..., shift
right by 1; isolate the odd bits with 0xAAAA..., shift
left by 1; OR the two halves. O(1).
Source: https://www.geeksforgeeks.org/swap-all-odd-and-even-bits/

Inputs passed to solve():
    n: non-negative integer.

Goal:
    n with odd and even bits swapped.

Samples:
Sample 1 input:  n = 23 (binary 10111)
Sample 1 output: 43 (binary 101011)

Sample 2 input:  n = 10 (binary 1010)
Sample 2 output: 5 (binary 0101)

Sample 3 input:  n = 0
Sample 3 output: 0

"""

def solve(n):
    # Write your code here.
    return None
