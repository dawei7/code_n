from collections import Counter


def solve(board: list[list[str]], word: str) -> bool:
    available = Counter(character for row in board for character in row)
    required = Counter(word)
    if any(available[character] < count for character, count in required.items()):
        return False
    if available[word[0]] > available[word[-1]]:
        word = word[::-1]

    rows, columns = len(board), len(board[0])

    def search(row: int, column: int, index: int) -> bool:
        if board[row][column] != word[index]:
            return False
        if index == len(word) - 1:
            return True

        character = board[row][column]
        board[row][column] = "#"
        found = False
        for row_step, column_step in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            next_row = row + row_step
            next_column = column + column_step
            if (
                0 <= next_row < rows
                and 0 <= next_column < columns
                and search(next_row, next_column, index + 1)
            ):
                found = True
                break
        board[row][column] = character
        return found

    return any(
        search(row, column, 0)
        for row in range(rows)
        for column in range(columns)
    )
