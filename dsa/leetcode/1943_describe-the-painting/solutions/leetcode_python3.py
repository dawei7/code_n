from collections import defaultdict
from typing import List


class Solution:
    def splitPainting(
        self,
        segments: List[List[int]],
    ) -> List[List[int]]:
        changes = defaultdict(int)
        for start, end, color in segments:
            changes[start] += color
            changes[end] -= color

        painting = []
        mixed_color = 0
        previous = None
        for coordinate in sorted(changes):
            if previous is not None and mixed_color:
                painting.append([previous, coordinate, mixed_color])
            mixed_color += changes[coordinate]
            previous = coordinate

        return painting
