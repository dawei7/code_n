class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 1_162_261_467 % n == 0
