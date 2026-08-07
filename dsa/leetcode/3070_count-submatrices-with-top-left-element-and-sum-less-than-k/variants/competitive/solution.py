class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        column_sums = [0] * len(grid[0])
        answer = 0

        for row in grid:
            rectangle_sum = 0
            for column, value in enumerate(row):
                column_sums[column] += value
                rectangle_sum += column_sums[column]
                answer += int(rectangle_sum <= k)

        return answer
