class Solution:
    def getPermutationIndex(self, perm: List[int]) -> int:
        mod = 1_000_000_007
        n = len(perm)
        tree = [0] * (n + 1)

        def prefix_sum(index: int) -> int:
            total = 0
            while index > 0:
                total += tree[index]
                index -= index & -index
            return total

        def add(index: int) -> None:
            while index <= n:
                tree[index] += 1
                index += index & -index

        rank = 0
        factorial = 1
        for index in range(n - 1, -1, -1):
            value = perm[index]
            rank = (rank + prefix_sum(value - 1) * factorial) % mod
            add(value)
            factorial = factorial * (n - index) % mod

        return rank
