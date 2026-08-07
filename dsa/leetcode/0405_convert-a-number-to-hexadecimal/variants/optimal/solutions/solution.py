class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        digits = "0123456789abcdef"
        value = num & 0xFFFFFFFF
        result = []

        while value:
            result.append(digits[value & 0xF])
            value >>= 4

        return "".join(reversed(result))
