class Solution:
    def maxDiff(self, num: int) -> int:
        digits = str(num)

        maximum = digits
        for digit in digits:
            if digit != "9":
                maximum = digits.replace(digit, "9")
                break

        minimum = digits
        if digits[0] != "1":
            minimum = digits.replace(digits[0], "1")
        else:
            for digit in digits[1:]:
                if digit not in {"0", "1"}:
                    minimum = digits.replace(digit, "0")
                    break

        return int(maximum) - int(minimum)
