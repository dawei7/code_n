import math


def solve(r: int = 15000, m_x: int = -2000, m_y: int = 1500, g_x: int = 8000, g_y: int = 1500) -> int:
    """Find the number of lattice points P for which the angle between the two tangents to the ellipse is > 45 degrees.
    
    Time Complexity: O(a * log(y_range))
    Space Complexity: O(1)
    """
    # Focal distance 2c = dist(M, G) = sqrt((g_x - m_x)^2 + (g_y - m_y)^2)
    # Sum of distances to foci 2a = r
    dx = g_x - m_x
    dy = g_y - m_y
    c2 = (dx * dx + dy * dy) // 4
    a = r // 2
    a2 = a * a
    b2 = a2 - c2

    a2_plus_b2 = a2 + b2
    a2_b2 = a2 * b2

    def is_valid(x: int, y: int) -> bool:
        x2 = x * x
        y2 = y * y
        lhs_outside = b2 * x2 + a2 * y2
        if lhs_outside <= a2_b2:
            return False

        denom = x2 + y2 - a2_plus_b2
        if denom <= 0:
            return True

        num = 4 * (lhs_outside - a2_b2)
        return num > denom * denom

    count_q1 = 0
    max_x = int(math.sqrt(4 * a2)) + 5000

    for x in range(1, max_x + 1):
        if x >= a:
            y_min = 1
        else:
            y_min_sq = (b2 * (a2 - x * x)) // a2 + 1
            y_min = int(math.isqrt(y_min_sq))
            if y_min * y_min < y_min_sq:
                y_min += 1
            if y_min == 0:
                y_min = 1

        if not is_valid(x, y_min):
            continue

        low = y_min
        high = y_min + 20000
        ans_y = low
        while low <= high:
            mid = (low + high) // 2
            if is_valid(x, mid):
                ans_y = mid
                low = mid + 1
            else:
                high = mid - 1

        count_q1 += (ans_y - y_min + 1)

    count_x = sum(1 for x in range(1, max_x + 1) if is_valid(x, 0))
    count_y = sum(1 for y in range(1, max_x + 1) if is_valid(0, y))
    count_origin = 1 if is_valid(0, 0) else 0

    return 4 * count_q1 + 2 * count_x + 2 * count_y + count_origin

