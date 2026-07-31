def solve(image: list[list[int]]) -> list[list[int]]:
    return [[value ^ 1 for value in reversed(row)] for row in image]
