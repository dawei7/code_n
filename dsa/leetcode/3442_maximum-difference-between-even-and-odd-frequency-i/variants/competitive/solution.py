from collections import Counter


class Solution:
    def maxDifference(self, s: str) -> int:
        frequencies = Counter(s).values()
        largest_odd = max(count for count in frequencies if count % 2)
        smallest_even = min(count for count in frequencies if count % 2 == 0)
        return largest_odd - smallest_even
