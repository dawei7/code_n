def solve(mat: list[list[int]]) -> int:
    size = len(mat)
    total = 0

    for index in range(size):
        total += mat[index][index]
        total += mat[index][size - 1 - index]

    if size % 2 == 1:
        total -= mat[size // 2][size // 2]

    return total
