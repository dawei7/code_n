from typing import List


def solve(tasks: List[int], space: int) -> int:
    last_day: dict[int, int] = {}
    day = 0
    for task in tasks:
        day = max(day + 1, last_day.get(task, -space) + space + 1)
        last_day[task] = day
    return day
