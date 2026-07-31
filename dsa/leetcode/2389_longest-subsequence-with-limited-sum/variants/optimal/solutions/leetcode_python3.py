from bisect import bisect_right
from itertools import accumulate
from typing import List


class Solution:
    def answerQueries(
        self,
        nums: List[int],
        queries: List[int],
    ) -> List[int]:
        nums.sort()
        prefix_sums = list(accumulate(nums))
        return [bisect_right(prefix_sums, query) for query in queries]
