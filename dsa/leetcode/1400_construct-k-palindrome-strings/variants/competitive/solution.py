from collections import Counter


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s):
            return False
        odd_count = sum(frequency % 2 for frequency in Counter(s).values())
        return odd_count <= k
