class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        if num == 0:
            return 0

        for count in range(1, 11):
            minimum_sum = count * k
            if minimum_sum <= num and minimum_sum % 10 == num % 10:
                return count
        return -1
