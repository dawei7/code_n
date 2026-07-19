from collections import Counter
from typing import List


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counts = Counter(arr)
        for value in arr:
            if counts[value] == 1:
                k -= 1
                if k == 0:
                    return value
        return ""
