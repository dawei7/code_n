"""Optimal solution for LeetCode 1074: Number of Submatrices That Sum to Target."""

from collections import Counter


def solve(matrix: list[list[int]], target: int) -> int:
    rows = len(matrix)
    columns = len(matrix[0])
    pair_rows = rows <= columns
    smaller = rows if pair_rows else columns
    larger = columns if pair_rows else rows
    answer = 0

    for first_boundary in range(smaller):
        compressed = [0] * larger
        for second_boundary in range(first_boundary, smaller):
            for index in range(larger):
                value = (
                    matrix[second_boundary][index]
                    if pair_rows
                    else matrix[index][second_boundary]
                )
                compressed[index] += value

            prefix_counts = Counter({0: 1})
            prefix = 0
            for value in compressed:
                prefix += value
                answer += prefix_counts[prefix - target]
                prefix_counts[prefix] += 1

    return answer
