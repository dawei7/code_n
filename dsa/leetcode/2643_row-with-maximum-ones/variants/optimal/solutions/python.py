def solve(mat: list[list[int]]) -> list[int]:
    best_row = 0
    best_count = -1

    for row_index, row in enumerate(mat):
        ones = sum(row)
        if ones > best_count:
            best_row = row_index
            best_count = ones

    return [best_row, best_count]
