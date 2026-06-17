"""Solution for math_09: Miller-Rabin Primality Test.


            Given a positive integer n, return True iff n is
            probably prime using the Miller-Rabin probabilistic
            test. Write n - 1 = 2^r * d with d odd. For each
            witness a (random in [2, n-1]), compute x = a^d
            mod n. If x == 1 or x == n - 1, the test passes for
            this witness. Otherwise, square x up to r - 1
            times; if any result is n - 1, the test passes.
            If none of the witnesses reveal n as composite,
            n is probably prime. With enough random witnesses
            the false-positive rate is negligible.
            O(k log^3 n) time for k witnesses.
            Source: https://www.geeksforgeeks.org/primality-test-set-3-miller-rabin/
            

Inputs passed to solve():
    n_val: the integer to test for primality.
    k: number of random witnesses.

Goal:
    True if n_val is probably prime; False if definitely composite.

Samples:
Sample 1 input:  n_val = 17, k = 5
Sample 1 output: True

Sample 2 input:  n_val = 18, k = 5
Sample 2 output: False

Sample 3 input:  n_val = 561, k = 10
Sample 3 output: True (Carmichael number passes Miller-Rabin)

"""

def solve(n_val, k):
    # Write your code here.
    return None
