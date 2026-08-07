class Solution:
    def minAbsDiff(self, grid: list[list[int]], k: int) -> list[list[int]]:
        rows = len(grid)
        columns = len(grid[0])
        answer: list[list[int]] = []
        for top in range(rows - k + 1):
            answer_row: list[int] = []
            for left in range(columns - k + 1):
                values = sorted({grid[row][column] for row in range(top, top + k) for column in range(left, left + k)})
                minimum_gap = min((right - left_value for left_value, right in zip(values, values[1:])), default=0)
                answer_row.append(minimum_gap)
            answer.append(answer_row)
        return answer
