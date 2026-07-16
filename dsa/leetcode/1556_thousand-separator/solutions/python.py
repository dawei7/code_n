"""Optimal app-local solution for LeetCode 1556."""


def solve(n: int) -> str:
    """Render n with a dot between decimal groups of three digits."""
    digits = str(n)
    groups = []

    while digits:
        groups.append(digits[-3:])
        digits = digits[:-3]

    return ".".join(reversed(groups))
