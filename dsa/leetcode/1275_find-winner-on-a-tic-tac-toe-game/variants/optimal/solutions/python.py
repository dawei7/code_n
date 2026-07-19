def solve(moves):
    rows = [0, 0, 0]
    columns = [0, 0, 0]
    diagonal = 0
    anti_diagonal = 0

    for turn, (row, column) in enumerate(moves):
        value = 1 if turn % 2 == 0 else -1
        rows[row] += value
        columns[column] += value
        if row == column:
            diagonal += value
        if row + column == 2:
            anti_diagonal += value

    lines = rows + columns + [diagonal, anti_diagonal]
    if 3 in lines:
        return "A"
    if -3 in lines:
        return "B"
    return "Draw" if len(moves) == 9 else "Pending"
