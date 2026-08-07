from typing import List


class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        next_missing = 1
        total = 0

        for value in sorted(set(nums)):
            if value > next_missing:
                take = min(k, value - next_missing)
                end = next_missing + take - 1
                total += (next_missing + end) * take // 2
                k -= take
                if k == 0:
                    return total
            next_missing = value + 1

        end = next_missing + k - 1
        return total + (next_missing + end) * k // 2
