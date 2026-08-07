class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n = len(fruits)
        answer = sum(fruits[index][index] for index in range(n))
        negative = -(10**18)

        previous = [negative] * n
        previous[n - 1] = fruits[0][n - 1]

        for row in range(1, n - 1):
            current = [negative] * n
            for column in range(row + 1, n):
                best = previous[column]
                if column > 0:
                    best = max(best, previous[column - 1])
                if column + 1 < n:
                    best = max(best, previous[column + 1])
                current[column] = best + fruits[row][column]
            previous = current

        answer += previous[n - 1]

        previous = [negative] * n
        previous[n - 1] = fruits[n - 1][0]

        for column in range(1, n - 1):
            current = [negative] * n
            for row in range(column + 1, n):
                best = previous[row]
                if row > 0:
                    best = max(best, previous[row - 1])
                if row + 1 < n:
                    best = max(best, previous[row + 1])
                current[row] = best + fruits[row][column]
            previous = current

        return answer + previous[n - 1]
