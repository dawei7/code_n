from collections import Counter
from typing import List


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        counts = Counter(value % k for value in arr)

        for remainder, count in counts.items():
            complement = (-remainder) % k
            if remainder == complement:
                if count % 2 != 0:
                    return False
            elif count != counts[complement]:
                return False

        return True
