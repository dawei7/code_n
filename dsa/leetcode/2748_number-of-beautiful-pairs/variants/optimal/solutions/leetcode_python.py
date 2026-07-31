from math import gcd


class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        first_digit_counts = [0] * 10
        pairs = 0

        for value in nums:
            last_digit = value % 10
            for first_digit in range(1, 10):
                if gcd(first_digit, last_digit) == 1:
                    pairs += first_digit_counts[first_digit]

            first_digit = value
            while first_digit >= 10:
                first_digit //= 10
            first_digit_counts[first_digit] += 1

        return pairs
