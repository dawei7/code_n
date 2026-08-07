class Solution:
    def newInteger(self, n: int) -> int:
        result = 0
        decimal_place = 1
        while n > 0:
            n, digit = divmod(n, 9)
            result += digit * decimal_place
            decimal_place *= 10
        return result
