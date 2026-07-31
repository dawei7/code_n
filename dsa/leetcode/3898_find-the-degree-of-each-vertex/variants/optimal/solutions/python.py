def solve(matrix: list[list[int]]) -> list[int]:
    degrees: list[int] = []
    for row in matrix:
        degree = 0
        for connected in row:
            degree += connected
        degrees.append(degree)
    return degrees
