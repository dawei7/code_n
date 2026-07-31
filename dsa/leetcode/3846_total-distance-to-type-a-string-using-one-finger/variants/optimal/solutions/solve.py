def solve(s: str) -> int:
    keyboard = (
        "qwertyuiop",
        "asdfghjkl",
        "zxcvbnm",
    )
    positions = {character: (row, column) for row, keys in enumerate(keyboard) for column, character in enumerate(keys)}

    row, column = positions["a"]
    total = 0

    for character in s:
        next_row, next_column = positions[character]
        total += abs(row - next_row) + abs(column - next_column)
        row, column = next_row, next_column

    return total
