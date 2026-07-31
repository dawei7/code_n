def solve(poured: int, query_row: int, query_glass: int) -> float:
    row = [float(poured)]
    for _ in range(query_row):
        next_row = [0.0] * (len(row) + 1)
        for glass, amount in enumerate(row):
            overflow = max(0.0, amount - 1.0) / 2.0
            next_row[glass] += overflow
            next_row[glass + 1] += overflow
        row = next_row
    return min(1.0, row[query_glass])
