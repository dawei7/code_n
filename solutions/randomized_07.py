"""Solution for randomized_07: Freivald's Algorithm (Matrix Product Check).


            Given three square n x n matrices A, B, C,
            determine if C = A * B. Freivald's Monte Carlo
            algorithm: generate a random n x 1 vector r with
            entries 0 or 1. Compute p = A * (B * r) - C * r.
            If p is the zero vector, return True (but this may
            be a false positive with low probability). Otherwise
            return False. Repeat trials times and accept if
            ALL iterations return True (or accept if ANY
            iteration returns False). O(n^2) per iteration.
            Source: https://www.geeksforgeeks.org/dsa/freivalds-algorithm/
            

Inputs passed to solve():
    mat_a: n x n matrix of integers (originally 'A' in the GfG notation).
    mat_b: n x n matrix of integers (originally 'B').
    mat_c: n x n matrix of integers (originally 'C').
    size: size of the matrices (originally 'n').
    trials: number of Freivald iterations to run.
    seed_value: an integer seed for reproducibility.

Goal:
    True if the algorithm believes mat_c = mat_a * mat_b, False otherwise. (False positives are possible but unlikely.)

Samples:
Sample 1 input:  A = [[1,1],[1,1]], B = [[1,1],[1,1]], C = [[2,2],[2,2]], n = 2, trials = 5, seed_value = 42
Sample 1 output: True

Sample 2 input:  A = [[1,1],[1,1]], B = [[1,1],[1,1]], C = [[2,2],[2,3]], n = 2, trials = 5, seed_value = 42
Sample 2 output: False (C is not A*B)


"""

def solve(mat_a, mat_b, mat_c, size, trials, seed_value):
    # Write your code here.
    return None
