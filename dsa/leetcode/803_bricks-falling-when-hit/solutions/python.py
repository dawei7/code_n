def solve(grid: list[list[int]], hits: list[list[int]]) -> list[int]:
    rows, cols = len(grid), len(grid[0])
    roof = rows * cols
    parent = list(range(roof + 1))
    component_size = [1] * (roof + 1)

    def find(node: int) -> int:
        while node != parent[node]:
            parent[node] = parent[parent[node]]
            node = parent[node]
        return node

    def union(first: int, second: int) -> None:
        first_root, second_root = find(first), find(second)
        if first_root == second_root:
            return
        if component_size[first_root] < component_size[second_root]:
            first_root, second_root = second_root, first_root
        parent[second_root] = first_root
        component_size[first_root] += component_size[second_root]

    state = [row[:] for row in grid]
    removed = []
    for row, col in hits:
        removed.append(state[row][col] == 1)
        state[row][col] = 0

    for row in range(rows):
        for col in range(cols):
            if state[row][col] == 0:
                continue
            index = row * cols + col
            if row == 0:
                union(index, roof)
            if row and state[row - 1][col]:
                union(index, index - cols)
            if col and state[row][col - 1]:
                union(index, index - 1)

    answer = [0] * len(hits)
    for hit_index in range(len(hits) - 1, -1, -1):
        if not removed[hit_index]:
            continue
        row, col = hits[hit_index]
        before = component_size[find(roof)]
        state[row][col] = 1
        index = row * cols + col
        if row == 0:
            union(index, roof)
        for row_delta, col_delta in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            next_row, next_col = row + row_delta, col + col_delta
            if 0 <= next_row < rows and 0 <= next_col < cols and state[next_row][next_col]:
                union(index, next_row * cols + next_col)
        after = component_size[find(roof)]
        answer[hit_index] = max(0, after - before - 1)

    return answer
