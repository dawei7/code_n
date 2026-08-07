from typing import List


class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        total = sum(milestones)
        largest = max(milestones)
        rest = total - largest

        if largest <= rest + 1:
            return total

        return 2 * rest + 1
