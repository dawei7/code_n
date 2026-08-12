def solve(max_tiles: int = 1000000, max_n: int = 10) -> int:
    """Find sum of N(n) for 1 <= n <= max_n where t <= max_tiles is type L(n).
    
    Time Complexity: O(M log M) where M = max_tiles / 4
    Space Complexity: O(M)
    """
    LIMIT = max_tiles // 4

    div_count = [0] * (LIMIT + 1)
    for i in range(1, LIMIT + 1):
        for j in range(i, LIMIT + 1, i):
            div_count[j] += 1

    N_counts = [0] * (max_n + 1)
    for m in range(1, LIMIT + 1):
        d = div_count[m]
        sq = int(m**0.5)
        if sq * sq == m:
            c = (d - 1) // 2
        else:
            c = d // 2

        if 1 <= c <= max_n:
            N_counts[c] += 1

    return sum(N_counts)
