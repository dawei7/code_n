def solve(squares):
    # Collect all unique x-coordinates for the segment tree
    x_coords = sorted(list(set([s[0] for s in squares] + [s[0] + s[2] for s in squares])))
    x_map = {x: i for i, x in enumerate(x_coords)}
    m = len(x_coords)
    
    # Segment tree to track the length of the union of intervals on the x-axis
    count = [0] * (4 * m)
    length = [0.0] * (4 * m)

    def update(node, start, end, l, r, val):
        if l <= start and end <= r:
            count[node] += val
        else:
            mid = (start + end) // 2
            if l < mid:
                update(2 * node, start, mid, l, r, val)
            if r > mid:
                update(2 * node + 1, mid, end, l, r, val)
        
        if count[node] > 0:
            length[node] = float(x_coords[end] - x_coords[start])
        else:
            if end - start == 1:
                length[node] = 0.0
            else:
                length[node] = length[2 * node] + length[2 * node + 1]

    def get_area_below(y_limit):
        events = []
        for x, y, l in squares:
            y_bottom = max(0, y)
            y_top = min(y_limit, y + l)
            if y_bottom < y_top:
                events.append((y_bottom, 1, x, x + l))
                events.append((y_top, -1, x, x + l))
        
        events.sort()
        
        total_area = 0.0
        prev_y = events[0][0] if events else 0
        
        for y, type, x1, x2 in events:
            total_area += length[1] * (y - prev_y)
            update(1, 0, m - 1, x_map[x1], x_map[x2], type)
            prev_y = y
        return total_area

    # Calculate total area
    total_area = get_area_below(float('inf'))
    target = total_area / 2.0
    
    # Binary search for the y-coordinate
    low = 0.0
    high = 2e9 # Sufficiently large range
    for _ in range(100):
        mid = (low + high) / 2
        if get_area_below(mid) < target:
            low = mid
        else:
            high = mid
            
    return high
