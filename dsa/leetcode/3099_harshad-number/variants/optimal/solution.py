class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        original = x
        digit_sum = 0

        while x:
            digit_sum += x % 10
            x //= 10

        return digit_sum if original % digit_sum == 0 else -1
