class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True

        left = 1
        right = num // 2
        while left <= right:
            middle = (left + right) // 2
            square = middle * middle
            if square == num:
                return True
            if square < num:
                left = middle + 1
            else:
                right = middle - 1
        return False

