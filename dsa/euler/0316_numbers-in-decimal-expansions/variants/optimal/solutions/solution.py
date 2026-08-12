def solve(max_n: int = 999999, power: int = 16) -> int:
    """Find sum_{n=2..999999} g(floor(10^16 / n)) for expected string matching index g(k).
    
    Time Complexity: O(max_n * L) via Guibas-Odlyzko String Martingale Formula
    Space Complexity: O(L)
    """

    def g(val):
        s = str(val)
        L = len(s)
        tot = 0
        pow10 = 10
        for j in range(1, L + 1):
            if s[:j] == s[L - j :]:
                tot += pow10
            pow10 *= 10
        return tot - (L - 1)

    target_pow = 10**power
    return sum(g(target_pow // n) for n in range(2, max_n + 1))
