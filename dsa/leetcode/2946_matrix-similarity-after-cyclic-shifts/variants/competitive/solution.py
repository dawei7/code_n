from typing import List


class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        column_count = len(mat[0])
        shift = k % column_count

        for row in mat:
            for column, value in enumerate(row):
                if value != row[(column + shift) % column_count]:
                    return False

        return True
