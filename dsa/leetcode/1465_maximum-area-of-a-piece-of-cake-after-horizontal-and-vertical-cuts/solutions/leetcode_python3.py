class Solution:
    def maxArea(
        self,
        h: int,
        w: int,
        horizontalCuts: List[int],
        verticalCuts: List[int],
    ) -> int:
        horizontal = [0, *sorted(horizontalCuts), h]
        vertical = [0, *sorted(verticalCuts), w]

        max_height = max(
            horizontal[index] - horizontal[index - 1]
            for index in range(1, len(horizontal))
        )
        max_width = max(
            vertical[index] - vertical[index - 1]
            for index in range(1, len(vertical))
        )

        return (max_height * max_width) % 1_000_000_007
