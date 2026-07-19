class Solution:
    def sumBase(self, n: int, k: int) -> int:
        digit_sum = 0
        while n > 0:
            n, digit = divmod(n, k)
            digit_sum += digit
        return digit_sum
