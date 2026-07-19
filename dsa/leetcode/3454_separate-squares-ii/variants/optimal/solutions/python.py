def solve(squares):
    x_values = sorted({x for x, _, length in squares for x in (x, x + length)})
    x_index = {value: index for index, value in enumerate(x_values)}
    events = []
    for x, y, length in squares:
        left = x_index[x]
        right = x_index[x + length]
        events.append((y, 1, left, right))
        events.append((y + length, -1, left, right))
    events.sort()

    count = [0] * (4 * len(x_values))
    covered = [0] * (4 * len(x_values))

    def pull(node: int, left: int, right: int) -> None:
        if count[node] > 0:
            covered[node] = x_values[right] - x_values[left]
        elif right - left == 1:
            covered[node] = 0
        else:
            covered[node] = covered[node * 2] + covered[node * 2 + 1]

    def update(node: int, left: int, right: int, query_left: int, query_right: int, delta: int) -> None:
        if query_left <= left and right <= query_right:
            count[node] += delta
            pull(node, left, right)
            return
        mid = (left + right) // 2
        if query_left < mid:
            update(node * 2, left, mid, query_left, query_right, delta)
        if mid < query_right:
            update(node * 2 + 1, mid, right, query_left, query_right, delta)
        pull(node, left, right)

    bands = []
    area = 0
    previous_y = events[0][0]
    index = 0
    while index < len(events):
        y = events[index][0]
        width = covered[1]
        if y > previous_y and width:
            delta_area = width * (y - previous_y)
            bands.append((previous_y, y, width, area))
            area += delta_area
        while index < len(events) and events[index][0] == y:
            _, delta, left, right = events[index]
            update(1, 0, len(x_values) - 1, left, right, delta)
            index += 1
        previous_y = y

    target = area / 2
    for bottom, top, width, area_before in bands:
        segment_area = width * (top - bottom)
        if area_before + segment_area >= target:
            return bottom + (target - area_before) / width
    return float(events[-1][0])
