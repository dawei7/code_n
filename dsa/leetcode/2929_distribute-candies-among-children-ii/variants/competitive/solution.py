class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        def unrestricted(total: int) -> int:
            if total < 0:
                return 0
            return (total + 1) * (total + 2) // 2

        step = limit + 1
        return (
            unrestricted(n) - 3 * unrestricted(n - step) + 3 * unrestricted(n - 2 * step) - unrestricted(n - 3 * step)
        )
