"""App-local reference solution for LeetCode 1817."""

from collections import defaultdict


def solve(logs: list[list[int]], k: int) -> list[int]:
    minutes_by_user: dict[int, set[int]] = defaultdict(set)
    for user_id, minute in logs:
        minutes_by_user[user_id].add(minute)

    answer = [0] * k
    for minutes in minutes_by_user.values():
        answer[len(minutes) - 1] += 1
    return answer
