"""Sequential row-major reshape for LeetCode 566."""


def solve(mat: list[list[int]], r: int, c: int) -> list[list[int]]:
    rows = len(mat)
    columns = len(mat[0])

    if rows * columns != r * c:
        return mat

    reshaped = [[] for _ in range(r)]
    flat_index = 0

    for row in mat:
        for value in row:
            reshaped[flat_index // c].append(value)
            flat_index += 1

    return reshaped

