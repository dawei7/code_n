class Solution:
    def confusingNumber(self, n: int) -> bool:
        rotated_digit = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}
        original = n
        rotated = 0

        while n:
            digit = n % 10
            if digit not in rotated_digit:
                return False
            rotated = rotated * 10 + rotated_digit[digit]
            n //= 10

        return rotated != original

