def solve(target_score: int = 100) -> str:
    """Find probability Player 2 wins 'The Race' to target_score points, rounded to 8 decimal places.

    Problem Context & Mathematical Principles:
    -------------------------------------------
    1. Game Mechanics:
       - Player 1 tosses 1 coin per turn: Heads scores 1, Tails scores 0.
       - Player 2 chooses T >= 1 and tosses T coins: all Heads scores 2^(T-1), else 0.
       - Player 1 goes first. The first to reach >= target_score points wins immediately.
       - Player 2 plays optimally to maximize their winning probability.

    2. Backward Induction Markov Decision Process:
       Let P(i, j) = probability Player 2 wins when it is Player 2's turn to toss,
       and Q(i, j) = probability Player 2 wins when it is Player 1's turn to toss.

       On Player 1's turn at score (i, j):
           Q(i, j) = 0.5 * P(i, j) + 0.5 * P(i + 1, j)  (with P(i+1, j) = 0 if i+1 >= N).

       On Player 2's turn at score (i, j) with choice T:
           P_T(i, j) = 2^(-T) * S_T(i, j) + (1 - 2^(-T)) * Q(i, j)
       where S_T(i, j) = 1 if j + 2^(T-1) >= N else Q(i, j + 2^(T-1)).

       Substituting Q(i, j) = 0.5 * P(i, j) + 0.5 * P(i + 1, j) and solving for P(i, j):
           P(i, j) = max_{T >= 1} [ 2 * S_T(i, j) + (2^T - 1) * P(i + 1, j) ] / (2^T + 1).

    3. Starting State:
       Since Player 1 starts at score (0, 0), the game-winning probability is Q(0, 0).

    Complexity:
    -----------
    - Time Complexity: O(N^2 * log_2(N)) operations for N = 100 (< 0.01 seconds).
    - Space Complexity: O(N^2) DP table storage (~100 KB).
    """
    N = target_score
    P = [[0.0] * (N + 1) for _ in range(N + 1)]
    Q = [[0.0] * (N + 1) for _ in range(N + 1)]

    def get_P(i: int, j: int) -> float:
        if j >= N:
            return 1.0
        if i >= N:
            return 0.0
        return P[i][j]

    def get_Q(i: int, j: int) -> float:
        if j >= N:
            return 1.0
        if i >= N:
            return 0.0
        return Q[i][j]

    # Backward dynamic programming from score N-1 down to 0
    for i in range(N - 1, -1, -1):
        for j in range(N - 1, -1, -1):
            best_p = 0.0
            # Test all feasible coin toss counts T (T up to 8 covers gains up to 128 >= 100)
            for T in range(1, 9):
                gain = 1 << (T - 1)
                p2 = 1 << T

                if j + gain >= N:
                    S_T = 1.0
                else:
                    S_T = get_Q(i, j + gain)

                P_next_i = get_P(i + 1, j)
                val = (2.0 * S_T + (p2 - 1.0) * P_next_i) / (p2 + 1.0)
                if val > best_p:
                    best_p = val

            P[i][j] = best_p
            Q[i][j] = 0.5 * P[i][j] + 0.5 * get_P(i + 1, j)

    ans = Q[0][0]
    return f"{ans:.8f}"


if __name__ == "__main__":
    print(solve())
