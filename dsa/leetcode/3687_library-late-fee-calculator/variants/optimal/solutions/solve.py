def solve(daysLate: list[int]) -> int:
    return sum(1 if days == 1 else 2 * days if days <= 5 else 3 * days for days in daysLate)
