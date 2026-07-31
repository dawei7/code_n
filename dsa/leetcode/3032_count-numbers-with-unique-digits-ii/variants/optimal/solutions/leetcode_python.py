class Solution:
    def numberCount(self, a: int, b: int) -> int:
        answer = 0

        for value in range(a, b + 1):
            digits = str(value)
            if len(set(digits)) == len(digits):
                answer += 1

        return answer
