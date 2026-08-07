class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        score = 0

        while n:
            n, digit = divmod(n, 10)
            score += digit

        return score
