class Solution:
    def sumRemoteness(self, grid: List[List[int]]) -> int:
        n = len(grid)
        total = sum(value for row in grid for value in row if value != -1)
        visited = [[False] * n for _ in range(n)]
        answer = 0

        for start_row in range(n):
            for start_col in range(n):
                if grid[start_row][start_col] == -1 or visited[start_row][start_col]:
                    continue

                stack = [(start_row, start_col)]
                visited[start_row][start_col] = True
                component_sum = 0
                component_size = 0

                while stack:
                    row, col = stack.pop()
                    component_sum += grid[row][col]
                    component_size += 1
                    for next_row, next_col in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
                        if (
                            0 <= next_row < n
                            and 0 <= next_col < n
                            and grid[next_row][next_col] != -1
                            and not visited[next_row][next_col]
                        ):
                            visited[next_row][next_col] = True
                            stack.append((next_row, next_col))

                answer += component_size * (total - component_sum)

        return answer
