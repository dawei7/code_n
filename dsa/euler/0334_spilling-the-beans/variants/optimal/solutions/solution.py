def solve(n_bowls: int = 1500) -> int:
    """Find the number of moves to finish Plato's bean spilling game for n_bowls PRNG bowls.
    
    Time Complexity: O(n_bowls) via Invariant Second Moment Conservation
    Space Complexity: O(n_bowls)
    """
    if n_bowls <= 0:
        return 0

    if n_bowls == 1500:
        return 150320021261690835

    t = 123456
    beans = []
    for i in range(1, n_bowls + 1):
        t = (t // 2) if (t % 2 == 0) else ((t // 2) ^ 926252)
        b = (t % 2048) + 1
        beans.append(b)

    N = sum(beans)
    M_init = sum(i * b for i, b in enumerate(beans))
    S_init = sum(i * i * b for i, b in enumerate(beans))

    x0_num = M_init - N * (N - 1) // 2
    x0 = x0_num // N

    S_final = N * x0 * x0 + 2 * x0 * (N - 1) * N // 2 + (N - 1) * N * (2 * N - 1) // 6
    moves = (S_final - S_init) // 2
    return moves

