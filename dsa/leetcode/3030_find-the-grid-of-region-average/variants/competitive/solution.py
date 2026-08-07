from typing import List


class Solution:
    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        totals = [[0] * cols for _ in range(rows)]
        counts = [[0] * cols for _ in range(rows)]

        for top in range(rows - 2):
            for left in range(cols - 2):
                valid = True

                for row in range(top, top + 3):
                    for col in range(left, left + 2):
                        if abs(image[row][col] - image[row][col + 1]) > threshold:
                            valid = False

                for row in range(top, top + 2):
                    for col in range(left, left + 3):
                        if abs(image[row][col] - image[row + 1][col]) > threshold:
                            valid = False

                if not valid:
                    continue

                average = sum(image[row][col] for row in range(top, top + 3) for col in range(left, left + 3)) // 9

                for row in range(top, top + 3):
                    for col in range(left, left + 3):
                        totals[row][col] += average
                        counts[row][col] += 1

        return [
            [totals[row][col] // counts[row][col] if counts[row][col] else image[row][col] for col in range(cols)]
            for row in range(rows)
        ]
