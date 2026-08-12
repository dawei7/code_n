def solve(target_score: int = 100) -> str:
    """Find the probability that Player 2 wins The Race to `target_score` points, rounded to 8 decimal places.
    
    Time Complexity: O(N^2 * log_2(N)) for N = 100
    Space Complexity: O(N^2)
    """
    N = target_score

    V = [[0.0] * (N + 1) for _ in range(N + 1)]
    W = [[0.0] * (N + 1) for _ in range(N + 1)]

    def get_V(i, j):
        if j >= N:
            return 1.0
        if i >= N:
            return 0.0
        return V[i][j]

    for i in range(N - 1, -1, -1):
        for j in range(N - 1, -1, -1):
            best_w = 0.0
            for T in range(1, 9):
                gain = 1 << (T - 1)
                prob_success = 1.0 / (1 << T)
                val = prob_success * get_V(i + 1, j + gain) + (1.0 - prob_success) * get_V(i + 1, j)
                if val > best_w:
                    best_w = val
            W[i + 1][j] = best_w

            best_v = 0.0
            for T in range(1, 9):
                gain = 1 << (T - 1)
                p2_pow = 1 << T
                val = (p2_pow * W[i + 1][j] + get_V(i, j + gain)) / (p2_pow + 1.0)
                if val > best_v:
                    best_v = val
            V[i][j] = best_v

    ans = V[0][0]
    return f"{ans:.8f}"
