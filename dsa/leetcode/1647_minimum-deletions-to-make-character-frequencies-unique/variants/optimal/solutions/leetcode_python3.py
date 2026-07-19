from collections import Counter


class Solution:
    def minDeletions(self, s: str) -> int:
        used = set()
        deletions = 0
        for frequency in Counter(s).values():
            while frequency > 0 and frequency in used:
                frequency -= 1
                deletions += 1
            if frequency > 0:
                used.add(frequency)
        return deletions
