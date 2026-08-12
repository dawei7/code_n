def solve(num_players: int = 100) -> str:
    """Find expected number of turns for The Chase game with `num_players`, rounded to 10 significant digits.
    
    Time Complexity: O((N / 2)^3) Gaussian Elimination for N = 100
    Space Complexity: O((N / 2)^2)
    """
    N = num_players
    MAX_D = N // 2

    A = [[0.0] * (MAX_D + 1) for _ in range(MAX_D + 1)]
    B_vec = [0.0] * (MAX_D + 1)

    A[0][0] = 1.0
    B_vec[0] = 0.0

    def get_d(x):
        x = abs(x)
        if x > MAX_D:
            x = N - x
        return x

    for d in range(1, MAX_D + 1):
        A[d][d] += 18.0
        A[d][get_d(d - 1)] -= 8.0
        A[d][get_d(d - 2)] -= 1.0
        A[d][get_d(d + 1)] -= 8.0
        A[d][get_d(d + 2)] -= 1.0
        B_vec[d] = 36.0

    for i in range(MAX_D + 1):
        pivot = A[i][i]
        for j in range(i, MAX_D + 1):
            A[i][j] /= pivot
        B_vec[i] /= pivot
        for k in range(MAX_D + 1):
            if k != i:
                factor = A[k][i]
                for j in range(i, MAX_D + 1):
                    A[k][j] -= factor * A[i][j]
                B_vec[k] -= factor * B_vec[i]

    ans = B_vec[MAX_D]
    return f"{ans:.10g}"
