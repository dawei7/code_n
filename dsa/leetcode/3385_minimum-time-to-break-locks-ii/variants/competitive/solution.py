from typing import List


class Solution:
    def findMinimumTime(self, strength: List[int]) -> int:
        n = len(strength)
        row_potential = [0] * (n + 1)
        column_potential = [0] * (n + 1)
        matched_row = [0] * (n + 1)
        previous_column = [0] * (n + 1)

        for row in range(1, n + 1):
            matched_row[0] = row
            column = 0
            minimum_slack = [float("inf")] * (n + 1)
            used = [False] * (n + 1)

            while True:
                used[column] = True
                current_row = matched_row[column]
                delta = float("inf")
                next_column = 0

                for candidate in range(1, n + 1):
                    if used[candidate]:
                        continue
                    cost = (strength[current_row - 1] + candidate - 1) // candidate
                    slack = cost - row_potential[current_row] - column_potential[candidate]
                    if slack < minimum_slack[candidate]:
                        minimum_slack[candidate] = slack
                        previous_column[candidate] = column
                    if minimum_slack[candidate] < delta:
                        delta = minimum_slack[candidate]
                        next_column = candidate

                for candidate in range(n + 1):
                    if used[candidate]:
                        row_potential[matched_row[candidate]] += delta
                        column_potential[candidate] -= delta
                    elif candidate:
                        minimum_slack[candidate] -= delta

                column = next_column
                if matched_row[column] == 0:
                    break

            while column:
                prior = previous_column[column]
                matched_row[column] = matched_row[prior]
                column = prior

        return -column_potential[0]
