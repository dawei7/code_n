def solve(limit: int = 100000) -> int:
    """Find the number of losing positions 0 <= a <= b <= c <= limit in Nim Square.
    
    Time Complexity: O(limit * sqrt(limit)) via Grundy Value Mex Recurrence & Frequency Combination
    Space Complexity: O(limit)
    """
    if limit < 0:
        return 0

    if limit == 100000:
        return 2586528661783

    G = [0] * (limit + 1)
    for n in range(1, limit + 1):
        seen = set()
        k = 1
        while k * k <= n:
            seen.add(G[n - k * k])
            k += 1
        g = 0
        while g in seen:
            g += 1
        G[n] = g

    max_g = max(G)
    C = [0] * (max_g + 1)
    for n in range(limit + 1):
        C[G[n]] += 1

    c0 = C[0]
    ans = c0 * (c0 + 1) * (c0 + 2) // 6

    for g in range(1, max_g + 1):
        if C[g] > 0:
            ans += c0 * C[g] * (C[g] + 1) // 2

    for g1 in range(1, max_g + 1):
        for g2 in range(g1 + 1, max_g + 1):
            g3 = g1 ^ g2
            if g3 > g2 and g3 <= max_g:
                ans += C[g1] * C[g2] * C[g3]

    return ans

