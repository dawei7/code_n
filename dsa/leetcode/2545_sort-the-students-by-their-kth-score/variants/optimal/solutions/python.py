from typing import List


def solve(score: List[List[int]], k: int) -> List[List[int]]:
    return sorted(score, key=lambda row: row[k], reverse=True)
