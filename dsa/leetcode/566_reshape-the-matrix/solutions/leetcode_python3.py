from typing import List


class Solution:
    def matrixReshape(
        self,
        mat: List[List[int]],
        r: int,
        c: int,
    ) -> List[List[int]]:
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

