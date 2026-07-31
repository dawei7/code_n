from typing import List


class Solution:
    def prefixConnected(self, words: List[str], k: int) -> int:
        prefix_counts: dict[str, int] = {}

        for word in words:
            if len(word) < k:
                continue
            prefix = word[:k]
            prefix_counts[prefix] = prefix_counts.get(prefix, 0) + 1

        return sum(count >= 2 for count in prefix_counts.values())
