from typing import List


class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        cell_count = row * col
        top = cell_count
        bottom = cell_count + 1
        parent = list(range(cell_count + 2))
        size = [1] * (cell_count + 2)
        land = [False] * cell_count

        def find(node: int) -> int:
            while node != parent[node]:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node

        def union(left: int, right: int) -> None:
            left_root = find(left)
            right_root = find(right)
            if left_root == right_root:
                return
            if size[left_root] < size[right_root]:
                left_root, right_root = right_root, left_root
            parent[right_root] = left_root
            size[left_root] += size[right_root]

        for day in range(cell_count - 1, -1, -1):
            current_row = cells[day][0] - 1
            current_col = cells[day][1] - 1
            index = current_row * col + current_col
            land[index] = True

            if current_row == 0:
                union(index, top)
            if current_row == row - 1:
                union(index, bottom)

            for row_delta, col_delta in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                neighbor_row = current_row + row_delta
                neighbor_col = current_col + col_delta
                if 0 <= neighbor_row < row and 0 <= neighbor_col < col:
                    neighbor = neighbor_row * col + neighbor_col
                    if land[neighbor]:
                        union(index, neighbor)

            if find(top) == find(bottom):
                return day

        return 0
