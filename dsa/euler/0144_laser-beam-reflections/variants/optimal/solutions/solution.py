import math


def solve() -> int:
    """Find number of laser beam reflections inside the ellipse 4x^2 + y^2 = 100 before exiting.
    
    Time Complexity: O(Bounces)
    Space Complexity: O(1)
    """
    x0, y0 = 0.0, 10.1
    x1, y1 = 1.4, -9.6
    bounces = 0

    while True:
        bounces += 1
        # Gradient normal vector to 4x^2 + y^2 = 100 at (x1, y1)
        nx, ny = 4 * x1, y1
        n_len = math.hypot(nx, ny)
        nx, ny = nx / n_len, ny / n_len

        # Incident direction vector
        vx, vy = x1 - x0, y1 - y0
        v_len = math.hypot(vx, vy)
        vx, vy = vx / v_len, vy / v_len

        # Vector reflection: R = V - 2 * (V . N) * N
        dot = vx * nx + vy * ny
        rx = vx - 2 * dot * nx
        ry = vy - 2 * dot * ny

        # Ray-ellipse intersection parameter t
        t = -2 * (4 * x1 * rx + y1 * ry) / (4 * rx * rx + ry * ry)

        x2 = x1 + t * rx
        y2 = y1 + t * ry

        # Update position
        x0, y0 = x1, y1
        x1, y1 = x2, y2

        # Check exit hole condition: -0.01 <= x1 <= 0.01 and y1 > 0
        if -0.01 <= x1 <= 0.01 and y1 > 0:
            return bounces
