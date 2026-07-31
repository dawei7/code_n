class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        return min(n * n, maxWeight // w)


def solve(n: int, w: int, maxWeight: int) -> int:
    return Solution().maxContainers(n, w, maxWeight)
