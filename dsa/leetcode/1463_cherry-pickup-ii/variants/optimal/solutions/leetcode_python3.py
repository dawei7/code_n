class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        unreachable = -1

        previous = [[unreachable] * cols for _ in range(cols)]
        previous[0][cols - 1] = grid[0][0] + grid[0][cols - 1]

        for row in range(1, rows):
            current = [[unreachable] * cols for _ in range(cols)]

            for col1 in range(cols):
                for col2 in range(cols):
                    score = previous[col1][col2]
                    if score == unreachable:
                        continue

                    for next1 in range(max(0, col1 - 1), min(cols, col1 + 2)):
                        for next2 in range(max(0, col2 - 1), min(cols, col2 + 2)):
                            gain = grid[row][next1]
                            if next1 != next2:
                                gain += grid[row][next2]
                            candidate = score + gain
                            if candidate > current[next1][next2]:
                                current[next1][next2] = candidate

            previous = current

        return max(max(row) for row in previous)
