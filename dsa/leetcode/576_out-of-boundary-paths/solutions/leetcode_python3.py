class Solution:
    def findPaths(
        self,
        m: int,
        n: int,
        maxMove: int,
        startRow: int,
        startColumn: int,
    ) -> int:
        mod = 1_000_000_007
        current = [[0] * n for _ in range(m)]
        current[startRow][startColumn] = 1
        escaped = 0

        for _ in range(maxMove):
            next_counts = [[0] * n for _ in range(m)]
            for row in range(m):
                for column in range(n):
                    ways = current[row][column]
                    if ways == 0:
                        continue
                    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        next_row = row + dr
                        next_column = column + dc
                        if 0 <= next_row < m and 0 <= next_column < n:
                            next_counts[next_row][next_column] = (
                                next_counts[next_row][next_column] + ways
                            ) % mod
                        else:
                            escaped = (escaped + ways) % mod
            current = next_counts

        return escaped

