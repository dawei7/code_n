def solve(grid: list[list[int]]) -> bool:
    def can_discount_from_prefix(matrix: list[list[int]]) -> bool:
        total = sum(map(sum, matrix))
        prefix = 0
        seen: set[int] = set()
        width = len(matrix[0])

        for row_index in range(len(matrix) - 1):
            prefix += sum(matrix[row_index])
            seen.update(matrix[row_index])
            difference = 2 * prefix - total

            if difference == 0:
                return True
            if difference <= 0:
                continue

            if row_index == 0:
                if difference in (matrix[0][0], matrix[0][-1]):
                    return True
            elif width == 1:
                if difference in (matrix[0][0], matrix[row_index][0]):
                    return True
            elif difference in seen:
                return True

        return False

    transposed = [list(column) for column in zip(*grid)]
    return (
        can_discount_from_prefix(grid)
        or can_discount_from_prefix(grid[::-1])
        or can_discount_from_prefix(transposed)
        or can_discount_from_prefix(transposed[::-1])
    )
