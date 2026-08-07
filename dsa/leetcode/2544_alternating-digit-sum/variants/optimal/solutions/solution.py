class Solution:
    def alternateDigitSum(self, n: int) -> int:
        answer = 0

        while n:
            answer = n % 10 - answer
            n //= 10

        return answer
