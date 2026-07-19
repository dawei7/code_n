from typing import List


class Solution:
    def pourWater(self, heights: List[int], volume: int, k: int) -> List[int]:
        for _ in range(volume):
            destination = k

            for direction in (-1, 1):
                position = k
                while (
                    0 <= position + direction < len(heights)
                    and heights[position + direction] <= heights[position]
                ):
                    position += direction
                    if heights[position] < heights[destination]:
                        destination = position

                if destination != k:
                    break

            heights[destination] += 1

        return heights
