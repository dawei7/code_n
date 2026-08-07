from collections import Counter
from functools import cache


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        initial = tuple(Counter(tiles).values())

        @cache
        def count_sequences(remaining: tuple[int, ...]) -> int:
            total = 0
            for index, count in enumerate(remaining):
                if count == 0:
                    continue
                next_remaining = list(remaining)
                next_remaining[index] -= 1
                total += 1 + count_sequences(tuple(next_remaining))
            return total

        return count_sequences(initial)
