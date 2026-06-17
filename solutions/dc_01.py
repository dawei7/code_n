"""Solution for dc_01: Power (x to the n).

Compute x^n for a real x and a non-negative integer n.
Use divide-and-conquer: x^n = (x^(n//2))^2, with an extra
x when n is odd. O(log n) multiplications.
Source: https://www.geeksforgeeks.org/write-a-program-to-calculate-powxn/

Inputs passed to solve():
    x: base (real number, integer or float).
    n: exponent (non-negative integer).

Goal:
    x ** n (float).

Samples:
Sample 1 input:  x = 2, n = 10
Sample 1 output: 1024

Sample 2 input:  x = 2.0, n = -2
Sample 2 output: 0.25  (setup always uses n >= 0; this sample is illustrative)

Sample 3 input:  x = 3, n = 0
Sample 3 output: 1

"""

def solve(x, n):
    # Write your code here.
    return None
