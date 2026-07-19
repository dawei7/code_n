def solve(coordinates: str) -> bool:
    column = ord(coordinates[0]) - ord("a")
    row = int(coordinates[1]) - 1
    return (column + row) % 2 == 1
