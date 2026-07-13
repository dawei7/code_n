def solve(fruits: list[list[int]]) -> int:
    n = len(fruits)
    diagonal = sum(fruits[i][i] for i in range(n))

    def top_right_path() -> int:
        negative = -10**18
        previous = [negative] * n
        previous[n - 1] = fruits[0][n - 1]

        for row in range(1, n - 1):
            current = [negative] * n
            for col in range(row + 1, n):
                best = previous[col]
                if col > 0:
                    best = max(best, previous[col - 1])
                if col + 1 < n:
                    best = max(best, previous[col + 1])
                current[col] = best + fruits[row][col]
            previous = current

        return previous[n - 1]

    def bottom_left_path() -> int:
        negative = -10**18
        previous = [negative] * n
        previous[n - 1] = fruits[n - 1][0]

        for col in range(1, n - 1):
            current = [negative] * n
            for row in range(col + 1, n):
                best = previous[row]
                if row > 0:
                    best = max(best, previous[row - 1])
                if row + 1 < n:
                    best = max(best, previous[row + 1])
                current[row] = best + fruits[row][col]
            previous = current

        return previous[n - 1]

    return diagonal + top_right_path() + bottom_left_path()
