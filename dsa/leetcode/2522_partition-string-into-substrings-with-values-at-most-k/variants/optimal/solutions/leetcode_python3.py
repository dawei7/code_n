class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        parts = 0
        value = 0

        for character in s:
            digit = int(character)
            if digit > k:
                return -1

            extended = value * 10 + digit
            if extended > k:
                parts += 1
                value = digit
            else:
                value = extended

        return parts + 1
