class Solution:
    def knightProbability(
        self,
        n: int,
        k: int,
        row: int,
        column: int,
    ) -> float:
        moves = (
            (-2, -1),
            (-2, 1),
            (-1, -2),
            (-1, 2),
            (1, -2),
            (1, 2),
            (2, -1),
            (2, 1),
        )
        current = [[0.0] * n for _ in range(n)]
        current[row][column] = 1.0

        for _ in range(k):
            following = [[0.0] * n for _ in range(n)]
            for current_row in range(n):
                for current_column in range(n):
                    if current[current_row][current_column] == 0.0:
                        continue
                    contribution = current[current_row][current_column] / 8.0
                    for row_delta, column_delta in moves:
                        next_row = current_row + row_delta
                        next_column = current_column + column_delta
                        if 0 <= next_row < n and 0 <= next_column < n:
                            following[next_row][next_column] += contribution
            current = following

        return sum(map(sum, current))

