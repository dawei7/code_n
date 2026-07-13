"""Integer state-capacity solution for LeetCode 458."""


def solve(buckets: int, minutesToDie: int, minutesToTest: int) -> int:
    states = minutesToTest // minutesToDie + 1
    pigs = 0
    capacity = 1
    while capacity < buckets:
        capacity *= states
        pigs += 1
    return pigs
