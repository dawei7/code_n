"""Optimal solution for LeetCode 363: Max Sum of Rectangle No Larger Than K."""

from bisect import bisect_left


def _best_subarray_at_most(values: list[int], limit: int) -> int | float:
    prefix_sums = [0]
    running = 0
    for value in values:
        running += value
        prefix_sums.append(running)

    coordinates = sorted(set(prefix_sums))
    tree = [0] * (len(coordinates) + 1)

    def add(coordinate_index: int) -> None:
        index = coordinate_index + 1
        while index < len(tree):
            tree[index] += 1
            index += index & -index

    def prefix_count(end: int) -> int:
        total = 0
        index = end
        while index:
            total += tree[index]
            index -= index & -index
        return total

    def coordinate_by_order(order: int) -> int:
        index = 0
        step = 1 << (len(tree).bit_length() - 1)
        while step:
            candidate = index + step
            if candidate < len(tree) and tree[candidate] < order:
                index = candidate
                order -= tree[candidate]
            step >>= 1
        return index

    add(bisect_left(coordinates, 0))
    inserted = 1
    best = float("-inf")

    for current in prefix_sums[1:]:
        threshold_index = bisect_left(coordinates, current - limit)
        below_threshold = prefix_count(threshold_index)
        if below_threshold < inserted:
            successor_index = coordinate_by_order(below_threshold + 1)
            best = max(best, current - coordinates[successor_index])
        add(bisect_left(coordinates, current))
        inserted += 1

    return best


def solve(matrix: list[list[int]], k: int) -> int:
    if not matrix or not matrix[0]:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])
    best = float("-inf")

    if rows <= cols:
        for top in range(rows):
            compressed = [0] * cols
            for bottom in range(top, rows):
                for col in range(cols):
                    compressed[col] += matrix[bottom][col]
                best = max(best, _best_subarray_at_most(compressed, k))
    else:
        for left in range(cols):
            compressed = [0] * rows
            for right in range(left, cols):
                for row in range(rows):
                    compressed[row] += matrix[row][right]
                best = max(best, _best_subarray_at_most(compressed, k))

    return int(best)
