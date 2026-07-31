from collections import defaultdict
from typing import List


def solve(limit: int, queries: List[List[int]]) -> List[int]:
    ball_colors = {}
    color_counts = defaultdict(int)
    answer = []

    for ball, color in queries:
        if ball in ball_colors:
            previous = ball_colors[ball]
            color_counts[previous] -= 1
            if color_counts[previous] == 0:
                del color_counts[previous]

        ball_colors[ball] = color
        color_counts[color] += 1
        answer.append(len(color_counts))

    return answer
