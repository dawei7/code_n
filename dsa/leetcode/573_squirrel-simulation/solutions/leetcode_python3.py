from typing import List


class Solution:
    def minDistance(
        self,
        height: int,
        width: int,
        tree: List[int],
        squirrel: List[int],
        nuts: List[List[int]],
    ) -> int:
        del height, width

        def distance(first: List[int], second: List[int]) -> int:
            return (
                abs(first[0] - second[0])
                + abs(first[1] - second[1])
            )

        baseline = 0
        best_saving = float("-inf")

        for nut in nuts:
            tree_distance = distance(tree, nut)
            baseline += 2 * tree_distance
            best_saving = max(
                best_saving,
                tree_distance - distance(squirrel, nut),
            )

        return int(baseline - best_saving)

