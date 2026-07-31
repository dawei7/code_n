def solve(grid: list[list[int]]) -> list[list[int]]:
    modulus = 12345
    rows = len(grid)
    columns = len(grid[0])
    product = [[1] * columns for _ in range(rows)]

    prefix = 1
    for row in range(rows):
        for column in range(columns):
            product[row][column] = prefix
            prefix = prefix * grid[row][column] % modulus

    suffix = 1
    for row in range(rows - 1, -1, -1):
        for column in range(columns - 1, -1, -1):
            product[row][column] = product[row][column] * suffix % modulus
            suffix = suffix * grid[row][column] % modulus

    return product
