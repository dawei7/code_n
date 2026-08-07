class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0:
            return "0"

        digits = []
        while n != 0:
            remainder = n & 1
            digits.append(str(remainder))
            n = (n - remainder) // -2

        return "".join(reversed(digits))
