class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        small_count = min(n, k // 2)
        remaining = n - small_count

        small_sum = small_count * (small_count + 1) // 2
        large_sum = remaining * (2 * k + remaining - 1) // 2
        return small_sum + large_sum
