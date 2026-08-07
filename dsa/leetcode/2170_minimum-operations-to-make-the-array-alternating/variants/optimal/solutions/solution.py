from collections import Counter
from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        even = Counter(nums[::2]).most_common(2)
        odd = Counter(nums[1::2]).most_common(2)
        even += [(None, 0)] * (2 - len(even))
        odd += [(None, 0)] * (2 - len(odd))

        if even[0][0] != odd[0][0]:
            unchanged = even[0][1] + odd[0][1]
        else:
            unchanged = max(
                even[0][1] + odd[1][1],
                even[1][1] + odd[0][1],
            )

        return len(nums) - unchanged
