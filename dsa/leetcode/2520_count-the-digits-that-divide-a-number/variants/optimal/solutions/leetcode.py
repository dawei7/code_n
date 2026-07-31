class Solution:
    def countDigits(self, num: int) -> int:
        original = num
        answer = 0

        while num:
            digit = num % 10
            if original % digit == 0:
                answer += 1
            num //= 10

        return answer
