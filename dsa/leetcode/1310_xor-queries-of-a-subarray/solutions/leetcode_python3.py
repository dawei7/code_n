from typing import List


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix = [0]
        for value in arr:
            prefix.append(prefix[-1] ^ value)

        return [prefix[right + 1] ^ prefix[left] for left, right in queries]
