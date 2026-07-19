class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        ways = 0
        length = 1

        while length * (length + 1) // 2 <= n:
            remainder = n - length * (length - 1) // 2
            if remainder % length == 0:
                ways += 1
            length += 1

        return ways
