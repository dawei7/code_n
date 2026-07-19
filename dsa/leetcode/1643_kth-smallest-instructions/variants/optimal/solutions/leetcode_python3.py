from math import comb
from typing import List


class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        vertical, horizontal = destination
        instructions: List[str] = []

        while horizontal and vertical:
            starting_with_horizontal = comb(horizontal + vertical - 1, vertical)
            if k <= starting_with_horizontal:
                instructions.append("H")
                horizontal -= 1
            else:
                instructions.append("V")
                vertical -= 1
                k -= starting_with_horizontal

        instructions.extend("H" * horizontal)
        instructions.extend("V" * vertical)
        return "".join(instructions)
