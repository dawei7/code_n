class Solution:
    def concatenatedBinary(self, n: int) -> int:
        modulus = 1_000_000_007
        value = 0
        bit_length = 0

        for current in range(1, n + 1):
            if current & (current - 1) == 0:
                bit_length += 1
            value = ((value << bit_length) | current) % modulus

        return value
