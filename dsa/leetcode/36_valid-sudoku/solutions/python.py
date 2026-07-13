def solve(board: list[list[str]]) -> bool:
    rows = [set() for _ in range(9)]
    columns = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    for row in range(9):
        for column in range(9):
            digit = board[row][column]
            if digit == ".":
                continue
            box = (row // 3) * 3 + column // 3
            if digit in rows[row] or digit in columns[column] or digit in boxes[box]:
                return False
            rows[row].add(digit)
            columns[column].add(digit)
            boxes[box].add(digit)
    return True
