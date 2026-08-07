from typing import List


class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        def weighted_sum(values: List[NestedInteger], depth: int) -> int:
            total = 0
            for value in values:
                if value.isInteger():
                    total += value.getInteger() * depth
                else:
                    total += weighted_sum(value.getList(), depth + 1)
            return total

        return weighted_sum(nestedList, 1)
