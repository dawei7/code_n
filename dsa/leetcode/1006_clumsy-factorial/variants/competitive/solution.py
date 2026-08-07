class Solution:
    def clumsy(self, n: int) -> int:
        if n <= 4:
            return (0, 1, 2, 6, 7)[n]

        remainder = n % 4
        if remainder == 0:
            return n + 1
        if remainder <= 2:
            return n + 2
        return n - 1
