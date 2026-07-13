def solve(s: str, numRows: int) -> str:
    if numRows == 1 or numRows >= len(s):
        return s

    rows: list[list[str]] = [[] for _ in range(numRows)]
    row = 0
    direction = 1
    for char in s:
        rows[row].append(char)
        if row == 0:
            direction = 1
        elif row == numRows - 1:
            direction = -1
        row += direction
    return "".join("".join(chars) for chars in rows)
