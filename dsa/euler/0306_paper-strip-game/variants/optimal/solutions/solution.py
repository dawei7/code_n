def solve(limit: int = 1000000) -> int:
    """Find the number of 1 <= n <= 1000000 for which the first player can force a win in the paper-strip game.
    
    Time Complexity: O(limit) via Sprague-Grundy Periodic Dawson's Chess Game Theory
    Space Complexity: O(1)
    """

    def mex(s):
        m = 0
        while m in s:
            m += 1
        return m

    G = [0] * 200
    for n in range(2, 200):
        reachable = set()
        for i in range(0, n - 1):
            left = i
            right = n - 2 - i
            reachable.add(G[left] ^ G[right])
        G[n] = mex(reachable)

    offset = 53
    period = 34

    def get_G(n):
        if n < offset:
            return G[n]
        return G[offset + (n - offset) % period]

    return sum(1 for n in range(1, limit + 1) if get_G(n) != 0)
