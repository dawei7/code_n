class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        score = 0
        while n:
            digit = n % 10
            score += digit * digit - digit
            n //= 10
        return score >= 50
