class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        answer = 0

        for value in range(low, high + 1):
            digits = str(value)
            if len(digits) % 2 == 1:
                continue

            middle = len(digits) // 2
            left_sum = sum(int(digit) for digit in digits[:middle])
            right_sum = sum(int(digit) for digit in digits[middle:])
            answer += left_sum == right_sum

        return answer
