"""Solution for randomized_06: Estimating Pi via Monte Carlo.


            Estimate the value of pi using the Monte Carlo
            method: sample n uniformly random points in the
            unit square [0, 1] x [0, 1] and count how many fall
            inside the quarter unit circle (x^2 + y^2 <= 1).
            The fraction of points inside, multiplied by 4,
            estimates pi. As n grows, the estimate converges
            to pi. O(n) time. The result is a float.
            Source: https://en.wikipedia.org/wiki/Monte_Carlo_method (referenced in GfG DSA Random)
            

Inputs passed to solve():
    n: number of random points to sample.
    seed_value: an integer seed for reproducibility.

Goal:
    a float estimate of pi (the absolute error vs true pi should be small for large n).

Samples:
Sample 1 input:  n = 10000, seed_value = 42
Sample 1 output: ~3.14 (very close to true pi)


"""

def solve(n, seed_value):
    # Write your code here.
    return None
