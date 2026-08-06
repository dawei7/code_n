"""Bitmask progress DP for LeetCode 473."""


def solve(matchsticks: list[int]) -> bool:
    total = sum(matchsticks)
    if total == 0 or total % 4:
        return False
    target = total // 4
    if max(matchsticks) > target:
        return False

    progress = [-1] * (1 << len(matchsticks))
    progress[0] = 0
    for mask, current in enumerate(progress):
        if current < 0:
            continue
        for i, stick in enumerate(matchsticks):
            bit = 1 << i
            if mask & bit:
                continue
            next_progress = current + stick
            if next_progress > target:
                continue
            progress[mask | bit] = next_progress % target
    return progress[-1] == 0
