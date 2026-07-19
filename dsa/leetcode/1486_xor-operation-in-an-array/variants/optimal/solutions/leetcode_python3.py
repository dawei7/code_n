class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        def xor_prefix(value: int) -> int:
            if value < 0:
                return 0

            remainder = value & 3
            if remainder == 0:
                return value
            if remainder == 1:
                return 1
            if remainder == 2:
                return value + 1
            return 0

        first = start >> 1
        high_bits = xor_prefix(first - 1) ^ xor_prefix(first + n - 1)
        low_bit = (start & 1) if n & 1 else 0
        return (high_bits << 1) | low_bit
