from typing import List


class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        depth_sums = []
        maximum_integer_depth = 0

        def collect(values: List[NestedInteger], depth: int) -> None:
            nonlocal maximum_integer_depth
            for value in values:
                if value.isInteger():
                    while len(depth_sums) < depth:
                        depth_sums.append(0)
                    depth_sums[depth - 1] += value.getInteger()
                    maximum_integer_depth = max(maximum_integer_depth, depth)
                else:
                    collect(value.getList(), depth + 1)

        collect(nestedList, 1)
        return sum(
            depth_sum * (maximum_integer_depth - depth + 1)
            for depth, depth_sum in enumerate(depth_sums, start=1)
        )

