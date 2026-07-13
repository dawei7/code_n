from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        size = len(matrix)
        low = matrix[0][0]
        high = matrix[-1][-1]

        def count_at_most(limit: int) -> int:
            row = size - 1
            col = 0
            count = 0
            while row >= 0 and col < size:
                if matrix[row][col] <= limit:
                    count += row + 1
                    col += 1
                else:
                    row -= 1
            return count

        while low < high:
            middle = low + (high - low) // 2
            if count_at_most(middle) >= k:
                high = middle
            else:
                low = middle + 1
        return low

