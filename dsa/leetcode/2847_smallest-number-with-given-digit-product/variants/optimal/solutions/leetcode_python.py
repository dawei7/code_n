class Solution:
    def smallestNumber(self, n: int) -> str:
        if n < 10:
            return str(n)

        digits = []
        for digit in range(9, 1, -1):
            while n % digit == 0:
                digits.append(str(digit))
                n //= digit

        if n != 1:
            return "-1"
        return "".join(reversed(digits))
