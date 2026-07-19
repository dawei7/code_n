class Solution:
    def getLucky(self, s: str, k: int) -> int:
        value = 0
        for character in s:
            position = ord(character) - ord("a") + 1
            value += position // 10 + position % 10

        for _ in range(k - 1):
            digit_sum = 0
            while value:
                digit_sum += value % 10
                value //= 10
            value = digit_sum

        return value
