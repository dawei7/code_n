class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        remaining = num2.bit_count()
        answer = 0

        for bit in range(29, -1, -1):
            mask = 1 << bit
            if remaining > 0 and num1 & mask:
                answer |= mask
                remaining -= 1

        bit = 0
        while remaining > 0:
            mask = 1 << bit
            if answer & mask == 0:
                answer |= mask
                remaining -= 1
            bit += 1

        return answer
