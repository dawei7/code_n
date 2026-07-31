from collections import Counter


class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        width = len(s) // k
        source = Counter(s[i:i + width] for i in range(0, len(s), width))
        target = Counter(t[i:i + width] for i in range(0, len(t), width))
        return source == target
