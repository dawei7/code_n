from typing import List


def solve(rolls: List[int], k: int) -> int:
    seen = set()
    answer = 1
    for roll in rolls:
        seen.add(roll)
        if len(seen) == k:
            answer += 1
            seen.clear()
    return answer
