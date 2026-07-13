from collections import Counter
from typing import List


class Solution:
    def findBlackPixel(self, picture: List[List[str]], target: int) -> int:
        cols = len(picture[0])
        col_counts = [0] * cols
        patterns = Counter()
        for row in picture:
            pattern = tuple(row)
            black_count = 0
            for col, pixel in enumerate(row):
                if pixel == "B":
                    black_count += 1
                    col_counts[col] += 1
            if black_count == target:
                patterns[pattern] += 1

        answer = 0
        for pattern, frequency in patterns.items():
            if frequency == target:
                answer += target * sum(
                    pixel == "B" and col_counts[col] == target
                    for col, pixel in enumerate(pattern)
                )
        return answer
