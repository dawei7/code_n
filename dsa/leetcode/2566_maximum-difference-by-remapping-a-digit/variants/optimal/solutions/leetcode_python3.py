class Solution:
    def minMaxDifference(self, num: int) -> int:
        digits = str(num)
        maximize_digit = next((digit for digit in digits if digit != "9"), "9")

        maximum = int(digits.replace(maximize_digit, "9"))
        minimum = int(digits.replace(digits[0], "0"))

        return maximum - minimum
