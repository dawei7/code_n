from collections import Counter
from typing import List


class Solution:
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        modulo = 1_000_000_007
        primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)
        frequencies = Counter(nums)
        masks = [0] * 31

        for value in range(2, 31):
            mask = 0
            valid = True
            for index, prime in enumerate(primes):
                if value % (prime * prime) == 0:
                    valid = False
                    break
                if value % prime == 0:
                    mask |= 1 << index
            if valid:
                masks[value] = mask

        ways = [0] * (1 << len(primes))
        ways[0] = 1

        for value in range(2, 31):
            count = frequencies[value]
            value_mask = masks[value]
            if count == 0 or value_mask == 0:
                continue
            for used_mask in range(len(ways) - 1, -1, -1):
                if used_mask & value_mask == 0:
                    combined = used_mask | value_mask
                    ways[combined] = (
                        ways[combined] + ways[used_mask] * count
                    ) % modulo

        nonempty_products = sum(ways[1:]) % modulo
        return nonempty_products * pow(2, frequencies[1], modulo) % modulo
