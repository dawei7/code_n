from collections import deque
from typing import List


class Solution:
    def floodFill(
        self,
        image: List[List[int]],
        sr: int,
        sc: int,
        color: int,
    ) -> List[List[int]]:
        original = image[sr][sc]
        if original == color:
            return image

        rows = len(image)
        columns = len(image[0])
        image[sr][sc] = color
        queue = deque([(sr, sc)])

        while queue:
            row, column = queue.popleft()
            for next_row, next_column in (
                (row - 1, column),
                (row + 1, column),
                (row, column - 1),
                (row, column + 1),
            ):
                if (
                    0 <= next_row < rows
                    and 0 <= next_column < columns
                    and image[next_row][next_column] == original
                ):
                    image[next_row][next_column] = color
                    queue.append((next_row, next_column))

        return image
