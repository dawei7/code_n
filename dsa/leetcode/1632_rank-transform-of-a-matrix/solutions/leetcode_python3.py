from collections import defaultdict
from typing import List


class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        columns = len(matrix[0])
        by_value = defaultdict(list)
        for row in range(rows):
            for column in range(columns):
                by_value[matrix[row][column]].append((row, column))

        row_rank = [0] * rows
        column_rank = [0] * columns
        answer = [[0] * columns for _ in range(rows)]

        for value in sorted(by_value):
            parent = {}

            def find(node):
                parent.setdefault(node, node)
                if parent[node] != node:
                    parent[node] = find(parent[node])
                return parent[node]

            def union(left, right):
                left_root = find(left)
                right_root = find(right)
                if left_root != right_root:
                    parent[right_root] = left_root

            for row, column in by_value[value]:
                union((0, row), (1, column))

            components = defaultdict(list)
            for row, column in by_value[value]:
                components[find((0, row))].append((row, column))

            assignments = []
            for cells in components.values():
                rank = 1 + max(
                    max(row_rank[row], column_rank[column])
                    for row, column in cells
                )
                assignments.append((cells, rank))

            for cells, rank in assignments:
                for row, column in cells:
                    answer[row][column] = rank
                    row_rank[row] = max(row_rank[row], rank)
                    column_rank[column] = max(column_rank[column], rank)
        return answer
