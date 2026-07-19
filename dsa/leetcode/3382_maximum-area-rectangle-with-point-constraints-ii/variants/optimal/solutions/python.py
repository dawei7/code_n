from collections import defaultdict


def solve(x: list[int], y: list[int]) -> int:
    points = list(zip(x, y))
    columns = defaultdict(list)
    for px, py in points:
        columns[px].append(py)

    segment_columns = defaultdict(list)
    for px, ys in columns.items():
        ys.sort()
        for lower, upper in zip(ys, ys[1:]):
            segment_columns[(lower, upper)].append(px)

    candidates = []
    for (lower, upper), xs in segment_columns.items():
        xs.sort()
        for left, right in zip(xs, xs[1:]):
            candidates.append((left, right, lower, upper))

    if not candidates:
        return -1

    compressed_y = {value: index + 1 for index, value in enumerate(sorted(set(y)))}
    size = len(compressed_y)
    tree = [0] * (size + 1)

    def add(index: int) -> None:
        while index <= size:
            tree[index] += 1
            index += index & -index

    def prefix(index: int) -> int:
        total = 0
        while index > 0:
            total += tree[index]
            index -= index & -index
        return total

    def range_sum(lower: int, upper: int) -> int:
        return prefix(compressed_y[upper]) - prefix(compressed_y[lower] - 1)

    events = []
    for query_index, (left, right, lower, upper) in enumerate(candidates):
        events.append((right, query_index, 1, lower, upper))
        events.append((left - 1, query_index, -1, lower, upper))
    events.sort(key=lambda event: event[0])

    sorted_points = sorted(points)
    point_index = 0
    counts = [0] * len(candidates)

    for limit, query_index, sign, lower, upper in events:
        while point_index < len(sorted_points) and sorted_points[point_index][0] <= limit:
            add(compressed_y[sorted_points[point_index][1]])
            point_index += 1
        counts[query_index] += sign * range_sum(lower, upper)

    best = -1
    for count, (left, right, lower, upper) in zip(counts, candidates):
        if count == 4:
            best = max(best, (right - left) * (upper - lower))

    return best
