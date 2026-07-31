class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        modulus = 1_000_000_007
        low_count = min(n, target // 2)
        high_count = n - low_count

        low_sum = low_count * (low_count + 1) // 2
        high_sum = high_count * (2 * target + high_count - 1) // 2

        return (low_sum + high_sum) % modulus
