class Solution:
    def splitNum(self, num: int) -> int:
        digits = sorted(str(num))
        first = second = 0

        for index, digit in enumerate(digits):
            if index % 2 == 0:
                first = first * 10 + int(digit)
            else:
                second = second * 10 + int(digit)

        return first + second
