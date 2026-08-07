from typing import List


class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        offset = 0
        minimum_offset = 0
        maximum_offset = 0

        for difference in differences:
            offset += difference
            minimum_offset = min(minimum_offset, offset)
            maximum_offset = max(maximum_offset, offset)

        return max(
            0,
            upper - lower - (maximum_offset - minimum_offset) + 1,
        )
