def solve(damage: list[int], armor: int) -> int:
    return sum(damage) - min(max(damage), armor) + 1
