def solve(mat: list[list[int]]) -> int:
    frequencies = [0] * 10001
    required = len(mat)

    for row in mat:
        for value in row:
            frequencies[value] += 1
            if frequencies[value] == required:
                return value
    return -1
