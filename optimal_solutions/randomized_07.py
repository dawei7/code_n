"""Optimal solution for randomized_07: Freivald's Algorithm (Matrix Product Check).

Given three square n x n matrices A, B, C,
"""


def solve(mat_a, mat_b, mat_c, size, trials, seed_value):
    """Freivald's algorithm: k iterations of random
    vector r in {0, 1}^n; check if A*(B*r) == C*r.
    """
    import random
    rng = random.Random(seed_value)
    n = size
    A = mat_a
    B = mat_b
    C = mat_c
    for _ in range(max(1, trials)):
        r = [rng.randint(0, 1) for _ in range(n)]
        # Compute B * r.
        Br = [0] * n
        for i in range(n):
            s = 0
            for j in range(n):
                s += B[i][j] * r[j]
            Br[i] = s
        # Compute C * r.
        Cr = [0] * n
        for i in range(n):
            s = 0
            for j in range(n):
                s += C[i][j] * r[j]
            Cr[i] = s
        # Compute A * (B * r).
        ABr = [0] * n
        for i in range(n):
            s = 0
            for j in range(n):
                s += A[i][j] * Br[j]
            ABr[i] = s
        # Check A * (B * r) == C * r componentwise.
        if ABr != Cr:
            return False
    return True
