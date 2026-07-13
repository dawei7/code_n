class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def subtree_size(prefix: int) -> int:
            first = prefix
            following = prefix + 1
            size = 0
            while first <= n:
                size += min(n + 1, following) - first
                first *= 10
                following *= 10
            return size

        prefix = 1
        remaining = k - 1
        while remaining:
            size = subtree_size(prefix)
            if size <= remaining:
                prefix += 1
                remaining -= size
            else:
                prefix *= 10
                remaining -= 1
        return prefix
