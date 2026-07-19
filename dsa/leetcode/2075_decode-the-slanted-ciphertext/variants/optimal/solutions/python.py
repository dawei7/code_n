def solve(encodedText: str, rows: int) -> str:
    columns = len(encodedText) // rows
    decoded = []

    for start_column in range(columns):
        row = 0
        column = start_column
        while row < rows and column < columns:
            decoded.append(encodedText[row * columns + column])
            row += 1
            column += 1

    return "".join(decoded).rstrip()
