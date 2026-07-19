from collections.abc import Iterable


def solve(board: list[list[str]], word: str) -> bool:
    def matches(segment: list[str]) -> bool:
        if len(segment) != len(word):
            return False
        forward = all(
            cell == " " or cell == letter
            for cell, letter in zip(segment, word)
        )
        backward = all(
            cell == " " or cell == letter
            for cell, letter in zip(segment, reversed(word))
        )
        return forward or backward

    def line_matches(line: Iterable[str]) -> bool:
        segment: list[str] = []
        for cell in line:
            if cell == "#":
                if matches(segment):
                    return True
                segment = []
            else:
                segment.append(cell)
        return matches(segment)

    for row in board:
        if line_matches(row):
            return True

    for column in range(len(board[0])):
        if line_matches(board[row][column] for row in range(len(board))):
            return True

    return False
