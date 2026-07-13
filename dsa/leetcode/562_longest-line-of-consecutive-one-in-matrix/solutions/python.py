"""Rolling directional dynamic programming for LeetCode 562."""


def solve(mat: list[list[int]]) -> int:
    if not mat or not mat[0]:
        return 0

    columns = len(mat[0])
    vertical = [0] * columns
    diagonal = [0] * columns
    anti_diagonal = [0] * columns
    longest = 0

    for row in mat:
        horizontal = 0
        next_diagonal = [0] * columns
        next_anti_diagonal = [0] * columns

        for column, value in enumerate(row):
            if value == 0:
                horizontal = 0
                vertical[column] = 0
                continue

            horizontal += 1
            vertical[column] += 1
            next_diagonal[column] = 1 + (
                diagonal[column - 1] if column > 0 else 0
            )
            next_anti_diagonal[column] = 1 + (
                anti_diagonal[column + 1]
                if column + 1 < columns
                else 0
            )
            longest = max(
                longest,
                horizontal,
                vertical[column],
                next_diagonal[column],
                next_anti_diagonal[column],
            )

        diagonal = next_diagonal
        anti_diagonal = next_anti_diagonal

    return longest

