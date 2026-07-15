from math import acos, atan2, hypot, pi


def solve(darts, r):
    best = 1
    diameter = 2.0 * r
    tolerance = 1e-10

    for anchor_index, (anchor_x, anchor_y) in enumerate(darts):
        events = []

        for point_index, (x, y) in enumerate(darts):
            if point_index == anchor_index:
                continue

            dx = x - anchor_x
            dy = y - anchor_y
            distance = hypot(dx, dy)
            if distance > diameter + tolerance:
                continue

            direction = atan2(dy, dx)
            half_width = acos(min(1.0, distance / diameter))
            start = direction - half_width
            end = direction + half_width

            for shift in (0.0, 2.0 * pi):
                events.append((start + shift, 1))
                events.append((end + shift, -1))

        events.sort(key=lambda event: (event[0], -event[1]))

        active = 1
        for _, delta in events:
            if delta == 1:
                active += 1
                best = max(best, active)
            else:
                active -= 1

    return best
