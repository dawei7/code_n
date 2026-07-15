"""Optimal app-local solution for LeetCode 850."""


MODULO = 1_000_000_007


def solve(rectangles):
    y_values = sorted({y for _, y1, _, y2 in rectangles for y in (y1, y2)})
    y_index = {value: index for index, value in enumerate(y_values)}
    interval_count = len(y_values) - 1
    cover_count = [0] * (4 * interval_count)
    covered_length = [0] * (4 * interval_count)

    def update(node, left, right, query_left, query_right, delta):
        if query_left <= left and right <= query_right:
            cover_count[node] += delta
        else:
            middle = (left + right) // 2
            if query_left <= middle:
                update(node * 2, left, middle, query_left, query_right, delta)
            if query_right > middle:
                update(node * 2 + 1, middle + 1, right, query_left, query_right, delta)

        if cover_count[node] > 0:
            covered_length[node] = y_values[right + 1] - y_values[left]
        elif left == right:
            covered_length[node] = 0
        else:
            covered_length[node] = covered_length[node * 2] + covered_length[node * 2 + 1]

    events = []
    for x1, y1, x2, y2 in rectangles:
        events.append((x1, y1, y2, 1))
        events.append((x2, y1, y2, -1))
    events.sort()

    area = 0
    previous_x = events[0][0]
    for x, y1, y2, delta in events:
        area += (x - previous_x) * covered_length[1]
        update(1, 0, interval_count - 1, y_index[y1], y_index[y2] - 1, delta)
        previous_x = x

    return area % MODULO
