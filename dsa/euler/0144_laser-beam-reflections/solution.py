import math


def solve() -> int:
    """Find the number of laser beam reflections inside the ellipse 4x^2 + y^2 = 100 before exiting through the top hole.

    Mathematical Principles Applied:
    1. Gradient Vector & Normal Line to Ellipse:
       The ellipse equation is f(x, y) = 4x^2 + y^2 - 100 = 0.
       The gradient vector grad f = (df/dx, df/dy) = (8x, 2y) is normal to the tangent at (x, y).
       Normal vector N = (4x, y) / sqrt(16x^2 + y^2).

    2. Law of Reflection (Vector Form):
       Let V be the unit incident direction vector from (x0, y0) to (x1, y1).
       The reflected unit direction vector R is:
       R = V - 2 * (V . N) * N.

    3. Ray-Ellipse Line Intersection:
       Substitute ray parametric equation (x, y) = (x1 + t*rx, y1 + t*ry) into 4x^2 + y^2 = 100:
       4(x1 + t*rx)^2 + (y1 + t*ry)^2 = 100.
       Using 4*x1^2 + y1^2 = 100, the quadratic simplifies to t*(t*(4*rx^2 + ry^2) + 2*(4*x1*rx + y1*ry)) = 0.
       The non-zero root is:
       t = -2 * (4*x1*rx + y1*ry) / (4*rx^2 + ry^2).
       Next reflection point: (x2, y2) = (x1 + t*rx, y1 + t*ry).

    4. Top Hole Exit Condition:
       The laser exits when -0.01 <= x <= 0.01 and y > 0.

    Time Complexity: O(Bounces) linear execution in ~0.001s.
    Space Complexity: O(1) constant auxiliary space.
    """
    x0, y0 = 0.0, 10.1
    x1, y1 = 1.4, -9.6
    bounces = 0

    while True:
        bounces += 1

        # Calculate unit normal vector N to ellipse 4x^2 + y^2 = 100 at (x1, y1)
        nx, ny = 4 * x1, y1
        n_len = math.hypot(nx, ny)
        nx, ny = nx / n_len, ny / n_len

        # Calculate unit incident direction vector V
        vx, vy = x1 - x0, y1 - y0
        v_len = math.hypot(vx, vy)
        vx, vy = vx / v_len, vy / v_len

        # Apply vector reflection formula R = V - 2 * (V . N) * N
        dot = vx * nx + vy * ny
        rx = vx - 2 * dot * nx
        ry = vy - 2 * dot * ny

        # Solve for ray-ellipse intersection parameter t
        t = -2 * (4 * x1 * rx + y1 * ry) / (4 * rx * rx + ry * ry)

        # Advance to next reflection point (x2, y2)
        x2 = x1 + t * rx
        y2 = y1 + t * ry

        # Update ray positions
        x0, y0 = x1, y1
        x1, y1 = x2, y2

        # Check top exit hole condition: -0.01 <= x1 <= 0.01 and y1 > 0
        if -0.01 <= x1 <= 0.01 and y1 > 0:
            return bounces


if __name__ == "__main__":
    print(solve())
