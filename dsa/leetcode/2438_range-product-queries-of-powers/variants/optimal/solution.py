from typing import List


class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        exponent_prefix = [0]
        bit_index = 0

        while n:
            if n & 1:
                exponent_prefix.append(exponent_prefix[-1] + bit_index)
            n >>= 1
            bit_index += 1

        modulo = 1_000_000_007
        return [pow(2, exponent_prefix[right + 1] - exponent_prefix[left], modulo) for left, right in queries]
