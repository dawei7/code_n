class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        value = abs(x)
        limit = 2**31 if sign < 0 else 2**31 - 1
        reversed_value = 0

        while value:
            value, digit = divmod(value, 10)
            if reversed_value > (limit - digit) // 10:
                return 0
            reversed_value = reversed_value * 10 + digit
        return sign * reversed_value
