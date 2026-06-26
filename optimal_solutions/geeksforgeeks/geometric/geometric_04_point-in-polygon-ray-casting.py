"""Optimal solution for geometric_04: Point in Polygon (Ray Casting).

Given a simple polygon (as a list of (x, y) vertices
"""


def solve(polygon, point, m):
    """Ray-casting point-in-polygon test."""
    if m < 3:
        return False
    x, y = point
    inside = False
    j = m - 1
    for i in range(m):
        xi, yi = polygon[i]
        xj, yj = polygon[j]
        # Edge (xj, yj) -> (xi, yi). Check if the horizontal
        # ray at y=y from the point crosses this edge.
        if ((yi > y) != (yj > y)):
            # The edge straddles the ray. Compute the x
            # intersection and check it's to the right of the
            # point.
            x_int = (xj * (yi - y) + xi * (y - yj)) / (yi - yj)
            if x < x_int:
                inside = not inside
        # Also: if the point lies on this edge, count as inside.
        # We can detect collinearity by checking the cross product
        # and bounding box.
        def _on_seg(a, b, c):
            return (min(a[0], b[0]) <= c[0] <= max(a[0], b[0])
                    and min(a[1], b[1]) <= c[1] <= max(a[1], b[1])
                    and (b[0] - a[0]) * (c[1] - a[1])
                        == (b[1] - a[1]) * (c[0] - a[0]))
        if _on_seg(polygon[i], polygon[j], point):
            return True
        j = i
    return inside
