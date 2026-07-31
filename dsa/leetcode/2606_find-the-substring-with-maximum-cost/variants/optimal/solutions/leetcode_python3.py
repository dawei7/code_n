from typing import List


class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        values = {character: value for character, value in zip(chars, vals)}
        best = 0
        current = 0

        for character in s:
            value = values.get(character, ord(character) - ord("a") + 1)
            current = max(0, current + value)
            best = max(best, current)

        return best
