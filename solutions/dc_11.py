"""Solution for dc_11: Modular Exponentiation.


            Compute (x ** n) % m for non-negative integers x, n
            and a positive modulus m. Naive multiplication of x
            by itself n times takes O(n) steps and overflows for
            big n. The D&C trick: square-and-reduce the base
            while halving the exponent. Reduces O(n) to O(log n).
            Source: https://www.geeksforgeeks.org/dsa/modular-exponentiation-power-in-modular-arithmetic/
            

Inputs passed to solve():
    x: base, non-negative integer (small in tests).
    n: exponent, non-negative integer (up to 2^20 in tests).
    m: modulus, positive integer.

Goal:
    (x ** n) % m as a non-negative int.

Samples:
Sample 1 input:  x = 3, n = 2, m = 4
Sample 1 output: 1

Sample 2 input:  x = 2, n = 6, m = 10
Sample 2 output: 4

Sample 3 input:  x = 7, n = 0, m = 13
Sample 3 output: 1
Sample 4 input:  x = 0, n = 5, m = 7
Sample 4 output: 0

"""

def solve(x, n, m):
    # Write your code here.
    return None
