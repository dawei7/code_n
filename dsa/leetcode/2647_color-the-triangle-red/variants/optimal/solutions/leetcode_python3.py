from typing import List


class Solution:
    def colorRed(self, n: int) -> List[List[int]]:
        result = [[1, 1]]

        for row in range(2, n + 1):
            offset = (n - row) % 4
            start = offset % 3 + 1

            if offset % 2:
                result.append([row, start])
            else:
                for column in range(start, 2 * row, 2):
                    result.append([row, column])

        return result
