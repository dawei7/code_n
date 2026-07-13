from collections import Counter
from functools import lru_cache


class Solution:
    def minStickers(self, stickers: list[str], target: str) -> int:
        sticker_counts = [Counter(sticker) for sticker in stickers]
        impossible = len(target) + 1

        @lru_cache(maxsize=None)
        def minimum(remaining: str) -> int:
            if not remaining:
                return 0

            needed = Counter(remaining)
            required_letter = remaining[0]
            best = impossible

            for sticker in sticker_counts:
                if sticker[required_letter] == 0:
                    continue

                next_remaining = []
                for letter, count in needed.items():
                    next_remaining.extend(
                        letter * max(0, count - sticker[letter])
                    )
                canonical = "".join(sorted(next_remaining))
                residual = minimum(canonical)
                if residual != impossible:
                    best = min(best, residual + 1)

            return best

        answer = minimum("".join(sorted(target)))
        return -1 if answer == impossible else answer

