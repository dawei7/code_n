"""Solution for math_07: Extended Euclidean Algorithm.


            Given two non-negative integers a and b (not both
            zero), find integers x and y such that a*x + b*y
            = gcd(a, b). Run Euclid's algorithm but keep the
            coefficients at each step: when (a, b) -> (b, a%b),
            the new x = old_y - (a//b) * old_x, and the new y
            = old_x. Return (gcd, x, y). O(log min(a, b)) time.
            Foundation for the modular inverse.
            Source: https://www.geeksforgeeks.org/euclidean-algorithms-basic-and-extended/
            

Inputs passed to solve():
    a: first non-negative integer.
    b: second non-negative integer.

Goal:
    a tuple (gcd, x, y) such that a*x + b*y = gcd.

Samples:
Sample 1 input:  a = 35, b = 15
Sample 1 output: (5, 1, -2) since 35*1 + 15*(-2) = 5 = gcd(35, 15)

Sample 2 input:  a = 30, b = 20
Sample 2 output: (10, 1, -1)


"""

def solve(a, b):
    # Write your code here.
    return None
