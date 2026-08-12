def solve(width: int = 32, height: int = 10) -> int:
    """Calculate W(width, height), number of crack-free walls using 2x1 and 3x1 bricks.
    
    Time Complexity: O(M^2 + H * E) where M is valid row count (~3329) and E is compatible edge count.
    Space Complexity: O(M^2)
    """
    rows = []

    def dfs(curr_sum, cracks):
        if curr_sum == width:
            rows.append(frozenset(cracks[:-1]))
            return
        if curr_sum + 2 <= width:
            dfs(curr_sum + 2, cracks + [curr_sum + 2])
        if curr_sum + 3 <= width:
            dfs(curr_sum + 3, cracks + [curr_sum + 3])

    dfs(0, [])
    M = len(rows)

    compat = [[] for _ in range(M)]
    for i in range(M):
        for j in range(i + 1, M):
            if rows[i].isdisjoint(rows[j]):
                compat[i].append(j)
                compat[j].append(i)

    counts = [1] * M
    for _ in range(1, height):
        next_counts = [0] * M
        for i in range(M):
            c = counts[i]
            if c > 0:
                for j in compat[i]:
                    next_counts[j] += c
        counts = next_counts

    return sum(counts)
