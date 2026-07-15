DIRECTIONS = ((1, 0), (-1, 0), (0, 1), (0, -1))


def solve(grid: list[list[int]]) -> int:
    side = len(grid)
    labels = [[0] * side for _ in range(side)]
    component_sizes: dict[int, int] = {}
    next_label = 2

    for row in range(side):
        for column in range(side):
            if grid[row][column] != 1 or labels[row][column] != 0:
                continue

            labels[row][column] = next_label
            stack = [(row, column)]
            area = 0
            while stack:
                current_row, current_column = stack.pop()
                area += 1
                for row_delta, column_delta in DIRECTIONS:
                    neighbor_row = current_row + row_delta
                    neighbor_column = current_column + column_delta
                    if not (0 <= neighbor_row < side and 0 <= neighbor_column < side):
                        continue
                    if grid[neighbor_row][neighbor_column] != 1:
                        continue
                    if labels[neighbor_row][neighbor_column] != 0:
                        continue
                    labels[neighbor_row][neighbor_column] = next_label
                    stack.append((neighbor_row, neighbor_column))

            component_sizes[next_label] = area
            next_label += 1

    largest = max(component_sizes.values(), default=0)
    for row in range(side):
        for column in range(side):
            if grid[row][column] != 0:
                continue

            neighboring_labels: set[int] = set()
            for row_delta, column_delta in DIRECTIONS:
                neighbor_row = row + row_delta
                neighbor_column = column + column_delta
                if 0 <= neighbor_row < side and 0 <= neighbor_column < side:
                    label = labels[neighbor_row][neighbor_column]
                    if label != 0:
                        neighboring_labels.add(label)

            candidate = 1 + sum(component_sizes[label] for label in neighboring_labels)
            largest = max(largest, candidate)

    return largest
