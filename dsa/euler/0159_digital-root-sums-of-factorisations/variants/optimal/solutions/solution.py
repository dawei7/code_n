def solve(limit: int = 1000000) -> int:
    """Find sum of mdrs(n) for 1 < n < limit.
    
    Time Complexity: O(limit * log(limit))
    Space Complexity: O(limit)
    """
    mdrs = [0] * limit
    for n in range(2, limit):
        mdrs[n] = 1 + (n - 1) % 9

    for i in range(2, limit):
        val_i = mdrs[i]
        max_j = (limit - 1) // i
        for j in range(2, max_j + 1):
            ij = i * j
            cand = val_i + mdrs[j]
            if cand > mdrs[ij]:
                mdrs[ij] = cand

    return sum(mdrs[2:limit])
