"""Solution for math_08: Modular Multiplicative Inverse.


            Given a and m (with gcd(a, m) = 1), find x such
            that a*x = 1 (mod m). The inverse exists iff a and
            m are coprime. Use the extended Euclidean algorithm:
            the coefficient of a in a*x + m*y = gcd(a, m) = 1
            is the inverse (mod m). If gcd != 1, return 0 as a
            sentinel for 'no inverse'. O(log min(a, m)) time.
            Source: https://www.geeksforgeeks.org/multiplicative-inverse-under-modulo-m/
            

Inputs passed to solve():
    a: the integer whose inverse we want.
    m: the modulus.

Goal:
    x in [0, m) such that a*x = 1 (mod m), or 0 if no inverse exists.

Samples:
Sample 1 input:  a = 3, m = 11
Sample 1 output: 4 since 3*4 = 12 = 1 (mod 11)

Sample 2 input:  a = 10, m = 17
Sample 2 output: 12 since 10*12 = 120 = 1 (mod 17) (10^-1 = 12)


"""

def solve(a, m):
    # Write your code here.
    return None
