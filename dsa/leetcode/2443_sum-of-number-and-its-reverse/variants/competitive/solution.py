class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        for value in range(num + 1):
            if value + int(str(value)[::-1]) == num:
                return True
        return False
