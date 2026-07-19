from math import isqrt


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = isqrt(c)

        while left <= right:
            square_sum = left * left + right * right
            if square_sum == c:
                return True
            if square_sum < c:
                left += 1
            else:
                right -= 1
        return False
