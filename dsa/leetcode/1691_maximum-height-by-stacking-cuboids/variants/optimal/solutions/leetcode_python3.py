from typing import List


class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        normalized = sorted(sorted(cuboid) for cuboid in cuboids)
        best = [cuboid[2] for cuboid in normalized]

        for bottom in range(len(normalized)):
            for top in range(bottom):
                if all(
                    normalized[top][dimension] <= normalized[bottom][dimension]
                    for dimension in range(3)
                ):
                    best[bottom] = max(
                        best[bottom], best[top] + normalized[bottom][2]
                    )

        return max(best)
