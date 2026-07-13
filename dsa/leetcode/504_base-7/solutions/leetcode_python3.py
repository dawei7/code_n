class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"

        negative = num < 0
        value = abs(num)
        digits = []
        while value:
            value, remainder = divmod(value, 7)
            digits.append(str(remainder))

        representation = "".join(reversed(digits))
        return f"-{representation}" if negative else representation
