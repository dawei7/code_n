from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> List[int]:
        def nearest_distance(value: int) -> int:
            length = value.bit_length()
            half_length = (length + 1) // 2
            prefix = value >> (length - half_length)

            def mirror(half: int) -> int:
                palindrome = half
                remaining = half >> 1 if length % 2 else half
                while remaining:
                    palindrome = (palindrome << 1) | (remaining & 1)
                    remaining >>= 1
                return palindrome

            candidates = {
                (1 << (length - 1)) - 1,
                (1 << length) + 1,
            }
            for half in (prefix - 1, prefix, prefix + 1):
                if half > 0:
                    candidates.add(mirror(half))

            return min(abs(value - candidate) for candidate in candidates)

        return [nearest_distance(value) for value in nums]
