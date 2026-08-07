import heapq
from typing import List


class Solution:
    def maximumValueSum(self, board: List[List[int]]) -> int:
        row_count = len(board)
        column_count = len(board[0])

        def build_summaries(row_order):
            best_by_column = [-float("inf")] * column_count
            summaries = [None] * row_count
            for row in row_order:
                for column, value in enumerate(board[row]):
                    best_by_column[column] = max(best_by_column[column], value)
                summaries[row] = heapq.nlargest(
                    3,
                    ((value, column) for column, value in enumerate(best_by_column)),
                )
            return summaries

        prefix = build_summaries(range(row_count))
        suffix = build_summaries(range(row_count - 1, -1, -1))

        answer = -float("inf")
        for middle_row in range(1, row_count - 1):
            for middle_column, middle_value in enumerate(board[middle_row]):
                for upper_value, upper_column in prefix[middle_row - 1]:
                    if upper_column == middle_column:
                        continue
                    for lower_value, lower_column in suffix[middle_row + 1]:
                        if lower_column not in (middle_column, upper_column):
                            answer = max(
                                answer,
                                upper_value + middle_value + lower_value,
                            )

        return answer
