def solve(squares: list[list[int]]) -> float:
    x_values = sorted({edge for x, _, side in squares for edge in (x, x + side)})
    x_index = {value: index for index, value in enumerate(x_values)}
    events = []
    for x, y, side in squares:
        left = x_index[x]
        right = x_index[x + side]
        events.append((y, 1, left, right))
        events.append((y + side, -1, left, right))
    events.sort()

    cover_count = [0] * (4 * len(x_values))
    covered_width = [0] * (4 * len(x_values))

    def pull(node: int, left: int, right: int) -> None:
        if cover_count[node] > 0:
            covered_width[node] = x_values[right] - x_values[left]
        elif right - left == 1:
            covered_width[node] = 0
        else:
            covered_width[node] = covered_width[node * 2] + covered_width[node * 2 + 1]

    def update(
        node: int,
        left: int,
        right: int,
        query_left: int,
        query_right: int,
        delta: int,
    ) -> None:
        if query_left <= left and right <= query_right:
            cover_count[node] += delta
            pull(node, left, right)
            return
        middle = (left + right) // 2
        if query_left < middle:
            update(node * 2, left, middle, query_left, query_right, delta)
        if middle < query_right:
            update(node * 2 + 1, middle, right, query_left, query_right, delta)
        pull(node, left, right)

    bands = []
    total_area = 0
    previous_y = events[0][0]
    event_index = 0
    while event_index < len(events):
        y = events[event_index][0]
        width = covered_width[1]
        if y > previous_y and width > 0:
            bands.append((previous_y, y, width, total_area))
            total_area += width * (y - previous_y)
        while event_index < len(events) and events[event_index][0] == y:
            _, delta, left, right = events[event_index]
            update(1, 0, len(x_values) - 1, left, right, delta)
            event_index += 1
        previous_y = y

    target = total_area / 2.0
    for bottom, top, width, area_before in bands:
        band_area = width * (top - bottom)
        if area_before + band_area >= target:
            return bottom + (target - area_before) / width
    return float(events[-1][0])
