"""Solution for math_03: Modular Exponentiation.

Compute (base^exp) mod mod without overflowing. Use
repeated squaring: for each bit of exp, square the base
(and reduce mod) and conditionally multiply the result.
Requirement: O(log exp) multiplications.
Source: https://www.geeksforgeeks.org/modular-exponentiation-power-in-modular-arithmetic/

Inputs passed to solve():
    base: the base (non-negative).
    exp: the exponent (non-negative).
    mod: the modulus (>= 1).

Goal:
    (base ** exp) % mod.

Samples:
Sample 1 input:  base = 2, exp = 10, mod = 1000
Sample 1 output: 24

Sample 2 input:  base = 3, exp = 5, mod = 100
Sample 2 output: 43

Sample 3 input:  base = 5, exp = 0, mod = 7
Sample 3 output: 1

"""

def solve(base, exp, mod):
    # Write your code here.
    return None
