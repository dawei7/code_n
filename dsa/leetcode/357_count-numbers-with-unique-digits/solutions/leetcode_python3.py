class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1

        total = 10
        exact_length = 9
        available = 9
        for _ in range(2, n + 1):
            exact_length *= available
            total += exact_length
            available -= 1
        return total
