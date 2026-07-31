class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        if n == 0:
            return False

        found = False
        leading_digit = 0

        while n > 0:
            digit = n % 10
            if digit == x:
                found = True
            leading_digit = digit
            n //= 10

        return found and leading_digit != x
