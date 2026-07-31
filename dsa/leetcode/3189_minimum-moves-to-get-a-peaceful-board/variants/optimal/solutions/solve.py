def solve(rooks: list[list[int]]) -> int:
    rows = sorted(x for x, _ in rooks)
    columns = sorted(y for _, y in rooks)
    return sum(abs(row - target) + abs(column - target) for target, (row, column) in enumerate(zip(rows, columns)))
