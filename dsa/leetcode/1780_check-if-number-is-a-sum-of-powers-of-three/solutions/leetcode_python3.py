class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n:
            n, digit = divmod(n, 3)
            if digit == 2:
                return False
        return True
