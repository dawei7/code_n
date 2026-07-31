from typing import List


class Solution:
    def maxDistance(self, words: List[str]) -> int:
        n = len(words)
        best = 0

        for right in range(n - 1, 0, -1):
            if words[right] != words[0]:
                best = right + 1
                break

        for left in range(1, n):
            if words[left] != words[-1]:
                best = max(best, n - left)
                break

        return best
