class Solution:
    def numberOfWays(self, n: int) -> int:
        mod = 1_000_000_007

        def ways_without_four(total: int) -> int:
            if total < 0:
                return 0
            sixes = total // 6
            pairs = total // 2
            return (sixes + 1) * (pairs + 1) - 3 * sixes * (sixes + 1) // 2

        return sum(ways_without_four(n - 4 * fours) for fours in range(3)) % mod
