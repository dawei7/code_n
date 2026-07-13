def _island_counts(m: int, n: int, positions: list[list[int]]) -> list[int]:
    parent: dict[int, int] = {}
    size: dict[int, int] = {}
    islands = 0
    result: list[int] = []

    def find(node: int) -> int:
        root = node
        while parent[root] != root:
            root = parent[root]
        while node != root:
            parent_node = parent[node]
            parent[node] = root
            node = parent_node
        return root

    for row, column in positions:
        node = row * n + column
        if node in parent:
            result.append(islands)
            continue
        parent[node] = node
        size[node] = 1
        islands += 1

        for row_delta, column_delta in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            neighbor_row = row + row_delta
            neighbor_column = column + column_delta
            if not (0 <= neighbor_row < m and 0 <= neighbor_column < n):
                continue
            neighbor = neighbor_row * n + neighbor_column
            if neighbor not in parent:
                continue
            root = find(node)
            neighbor_root = find(neighbor)
            if root == neighbor_root:
                continue
            if size[root] < size[neighbor_root]:
                root, neighbor_root = neighbor_root, root
            parent[neighbor_root] = root
            size[root] += size[neighbor_root]
            islands -= 1

        result.append(islands)
    return result


class Solution:
    def numIslands2(self, m: int, n: int, positions: list[list[int]]) -> list[int]:
        return _island_counts(m, n, positions)
