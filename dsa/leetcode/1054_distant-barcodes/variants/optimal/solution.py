from collections import Counter
from typing import List


class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        counts = Counter(barcodes)
        most_common = counts.most_common()
        n = len(barcodes)
        res = [0] * n
        idx = 0
        for val, count in most_common:
            for _ in range(count):
                res[idx] = val
                idx += 2
                if idx >= n:
                    idx = 1
        return res
