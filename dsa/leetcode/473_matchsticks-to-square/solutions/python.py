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
    for mask in range(len(progress)):
        if progress[mask] < 0:
            continue
        for index, stick in enumerate(matchsticks):
            bit = 1 << index
            if mask & bit or progress[mask] + stick > target:
                continue
            progress[mask | bit] = (progress[mask] + stick) % target
    return progress[-1] == 0
