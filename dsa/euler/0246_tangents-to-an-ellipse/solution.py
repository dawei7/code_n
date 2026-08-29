from math import isqrt


def solve(
    r: int = 15000,
    m_x: int = -2000,
    m_y: int = 1500,
    g_x: int = 8000,
    g_y: int = 1500,
) -> int:
    """Find the number of lattice points P for which the tangent angle to the ellipse is > 45 degrees.

    Problem Context & Mathematical Principles:
    -------------------------------------------
    1. Ellipse Geometric Construction:
       Given circle of radius r centred at M and internal point G, locus of equidistant points
       forms an ellipse whose foci are M and G with major axis 2a = r and focal distance 2c = dist(M, G).
       - Semi-major axis: a = r / 2 = 7500.
       - Semi-focal distance: c = dist(M, G) / 2 = 5000.
       - Semi-minor axis: b = sqrt(a^2 - c^2) = sqrt(56,250,000 - 25,000,000) = sqrt(31,250,000).

    2. Angle Between Tangents to an Ellipse:
       For a point P(x, y) outside the ellipse x^2/a^2 + y^2/b^2 = 1, the angle theta between
       the two tangents satisfies:
           tan^2(theta) = 4 * (b^2 x^2 + a^2 y^2 - a^2 b^2) / (x^2 + y^2 - (a^2 + b^2))^2.
       - Inside the orthoptic (director) circle x^2 + y^2 <= a^2 + b^2, theta >= 90 deg > 45 deg.
       - Outside the director circle, theta > 45 deg iff:
           4 * (b^2 x^2 + a^2 y^2 - a^2 b^2) > (x^2 + y^2 - (a^2 + b^2))^2.

    3. 4-Fold Symmetry & Binary Search:
       Exploiting quadrant reflection symmetry about the ellipse center (3000, 1500),
       we binary search the valid y-range for each horizontal coordinate x.

    Complexity:
    -----------
    - Time Complexity: O(x_max * log(y_max)) (~0.06 seconds).
    - Space Complexity: O(1) auxiliary space.
    """
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
    max_x = isqrt(4 * a2) + 5000

    for x in range(1, max_x + 1):
        if x >= a:
            y_min = 1
        else:
            y_min_sq = (b2 * (a2 - x * x)) // a2 + 1
            y_min = isqrt(y_min_sq)
            if y_min * y_min < y_min_sq:
                y_min += 1
            if y_min == 0:
                y_min = 1

        if not is_valid(x, y_min):
            continue

        low = y_min
        high = y_min + 2 * r
        ans_y = low
        while low <= high:
            mid = (low + high) // 2
            if is_valid(x, mid):
                ans_y = mid
                low = mid + 1
            else:
                high = mid - 1

        count_q1 += ans_y - y_min + 1

    count_x = sum(1 for x in range(1, max_x + 1) if is_valid(x, 0))
    count_y = sum(1 for y in range(1, max_x + 1) if is_valid(0, y))
    count_origin = 1 if is_valid(0, 0) else 0

    return 4 * count_q1 + 2 * count_x + 2 * count_y + count_origin


if __name__ == "__main__":
    print(solve())
