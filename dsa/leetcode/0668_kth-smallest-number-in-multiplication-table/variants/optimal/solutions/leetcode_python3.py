class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        if m > n:
            m, n = n, m

        low = 1
        high = m * n
        while low < high:
            candidate = (low + high) // 2
            count = sum(min(n, candidate // row) for row in range(1, m + 1))
            if count >= k:
                high = candidate
            else:
                low = candidate + 1
        return low
