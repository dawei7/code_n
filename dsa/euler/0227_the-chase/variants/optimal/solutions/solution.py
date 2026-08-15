def solve(num_players: int = 100) -> str:
    """Find the expected number of turns for The Chase game with 100 players, rounded to 10 significant digits.

    Problem Context & Mathematical Principles:
    -------------------------------------------
    1. Game State & Distance Representation:
       In a circle of N players (N = 100), two players hold dice.
       The state is the shortest circular distance d in [0, N//2] = [0, 50] between the two dice.
       - Game ends when d = 0 (both dice land on the same player), so E[0] = 0.
       - Starting state is d = 50 (diametrically opposite).

    2. Single Turn Markov Transition Probabilities:
       Each turn, both players roll a standard 6-sided die:
       - Rolling 1: pass die to the left (-1).
       - Rolling 6: pass die to the right (+1).
       - Rolling 2, 3, 4, 5: keep die (0).
       Relative change in distance delta in {-2, -1, 0, +1, +2}:
           P(delta = -2) = (1/6) * (1/6) = 1/36
           P(delta = -1) = 2 * (1/6) * (4/6) = 8/36
           P(delta =  0) = (4/6)^2 + 2 * (1/6)^2 = 18/36
           P(delta = +1) = 2 * (1/6) * (4/6) = 8/36
           P(delta = +2) = (1/6) * (1/6) = 1/36

    3. System of Linear Equations for Absorbing Markov Chain:
       For each distance d in [1, 50]:
           E[d] = 1 + (18/36) E[d] + (8/36)(E[|d-1|] + E[|d+1|]) + (1/36)(E[|d-2|] + E[|d+2|])
       where boundary distances wrap around: if x > 50, x = 100 - x.
       Multiplying by 36:
           18 E[d] - 8 E[dist(d-1)] - 8 E[dist(d+1)] - 1 E[dist(d-2)] - 1 E[dist(d+2)] = 36.

    4. Gaussian Elimination:
       The linear system A * E = B of size 51x51 is solved in O((N/2)^3) operations (~0.003s).

    Complexity:
    -----------
    - Time Complexity: O((N / 2)^3) operations (~0.003s for N = 100).
    - Space Complexity: O((N / 2)^2) auxiliary matrix space (< 10 KB).
    """
    N = num_players
    MAX_D = N // 2

    # Construct the linear system A * E = B_vec of size (MAX_D + 1)
    A = [[0.0] * (MAX_D + 1) for _ in range(MAX_D + 1)]
    B_vec = [0.0] * (MAX_D + 1)

    # Base absorbing state: E[0] = 0
    A[0][0] = 1.0
    B_vec[0] = 0.0

    def get_d(x: int) -> int:
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

    # Gaussian elimination with row pivoting
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

    # Return expected turns from starting distance d = 50 formatted to 10 significant digits
    ans = B_vec[MAX_D]
    return f"{ans:.10g}"


if __name__ == "__main__":
    print(solve())
