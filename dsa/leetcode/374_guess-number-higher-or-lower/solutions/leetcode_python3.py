# The guess API is already defined for you.
# def guess(num: int) -> int:


class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n

        while left <= right:
            middle = left + (right - left) // 2
            response = guess(middle)
            if response == 0:
                return middle
            if response < 0:
                right = middle - 1
            else:
                left = middle + 1

        return -1

