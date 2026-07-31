class Solution:
    def isDigitorialPermutation(self, n: int) -> bool:
        factorial = (1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880)

        original_counts = [0] * 10
        factorial_sum = 0
        remaining = n

        while remaining > 0:
            digit = remaining % 10
            original_counts[digit] += 1
            factorial_sum += factorial[digit]
            remaining //= 10

        sum_counts = [0] * 10
        remaining = factorial_sum

        while remaining > 0:
            sum_counts[remaining % 10] += 1
            remaining //= 10

        return original_counts == sum_counts
