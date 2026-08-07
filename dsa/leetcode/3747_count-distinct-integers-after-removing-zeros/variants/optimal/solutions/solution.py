class Solution:
    def countDistinct(self, n: int) -> int:
        digits = str(n)
        total = sum(9**length for length in range(1, len(digits)))

        for index, character in enumerate(digits):
            digit = int(character)
            remaining = len(digits) - index - 1
            total += max(0, digit - 1) * 9**remaining
            if digit == 0:
                return total

        return total + 1
