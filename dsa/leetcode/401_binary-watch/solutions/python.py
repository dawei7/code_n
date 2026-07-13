"""Optimal app-local solution for LeetCode 401: Binary Watch."""


def solve(turned_on: int) -> list[str]:
    return [
        f"{hour}:{minute:02d}"
        for hour in range(12)
        for minute in range(60)
        if hour.bit_count() + minute.bit_count() == turned_on
    ]
