"""Row and column black-pixel counts for LeetCode 531."""


def solve(picture: list[list[str]]) -> int:
    rows, cols = len(picture), len(picture[0])
    row_counts = [0] * rows
    col_counts = [0] * cols
    for row in range(rows):
        for col in range(cols):
            if picture[row][col] == "B":
                row_counts[row] += 1
                col_counts[col] += 1
    return sum(
        picture[row][col] == "B" and row_counts[row] == 1 and col_counts[col] == 1
        for row in range(rows)
        for col in range(cols)
    )
