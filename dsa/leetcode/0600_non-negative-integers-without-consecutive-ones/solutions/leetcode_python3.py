class Solution:
    def findIntegers(self, n: int) -> int:
        bit_count = max(1, n.bit_length())
        ways = [0] * (bit_count + 1)
        ways[0] = 1
        ways[1] = 2

        for length in range(2, bit_count + 1):
            ways[length] = (
                ways[length - 1] + ways[length - 2]
            )

        answer = 0
        previous_bit = 0

        for bit in range(bit_count - 1, -1, -1):
            if n & (1 << bit):
                answer += ways[bit]
                if previous_bit:
                    return answer
                previous_bit = 1
            else:
                previous_bit = 0

        return answer + 1

