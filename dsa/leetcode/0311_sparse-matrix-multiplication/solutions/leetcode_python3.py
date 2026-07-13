def _multiply(mat1: list[list[int]], mat2: list[list[int]]) -> list[list[int]]:
    rows = len(mat1)
    inner = len(mat2)
    columns = len(mat2[0])
    right_nonzero = [
        [(column, value) for column, value in enumerate(row) if value]
        for row in mat2
    ]
    result = [[0] * columns for _ in range(rows)]
    for row in range(rows):
        for shared in range(inner):
            left_value = mat1[row][shared]
            if left_value == 0:
                continue
            for column, right_value in right_nonzero[shared]:
                result[row][column] += left_value * right_value
    return result


class Solution:
    def multiply(
        self, mat1: list[list[int]], mat2: list[list[int]]
    ) -> list[list[int]]:
        return _multiply(mat1, mat2)
