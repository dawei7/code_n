from collections import defaultdict


class Solution:
    def countPairs(self, nums: List[int]) -> int:
        seen = defaultdict(int)
        pairs = 0

        for value in sorted(nums):
            digits = list(str(value))
            reachable = {value}
            for left in range(len(digits)):
                for right in range(left + 1, len(digits)):
                    digits[left], digits[right] = digits[right], digits[left]
                    reachable.add(int("".join(digits)))
                    digits[left], digits[right] = digits[right], digits[left]

            pairs += sum(seen[candidate] for candidate in reachable)
            seen[value] += 1

        return pairs
