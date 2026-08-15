import math


def solve() -> str:
    """Find the area under the blancmange curve enclosed by the circle C, rounded to 8 decimal places.

    Problem Context & Mathematical Principles:
    -------------------------------------------
    1. The Blancmange (Takagi) Fractal Curve:
       Defined for 0 <= x <= 1 as:
           B(x) = sum_{n=0}^infty s(2^n x) / 2^n
       where s(x) is the distance from x to the nearest integer: s(x) = min(x - floor(x), 1 - (x - floor(x))).

    2. The Enclosing Circle C:
       Circle with center (1/4, 1/2) and radius 1/4:
           (x - 1/4)^2 + (y - 1/2)^2 = (1/4)^2 = 1/16.
       The lower boundary of the circle is:
           y_bot(x) = 1/2 - sqrt(1/16 - (x - 1/4)^2) = 1/2 - sqrt(x/2 - x^2).

    3. Intersection Point & Area Region:
       The circle intersects the blancmange curve at x = 1/2 (where B(1/2) = 1/2 and y_bot(1/2) = 1/2)
       and at an intersection point x1 in [0.05, 0.10].
       Using binary search (bisection) on B(x) - y_bot(x) = 0 yields x1 to machine precision (~100 iterations).

    4. Analytical Integration:
       The enclosed area between x1 and 1/2 is:
           Area = int_{x1}^{1/2} (B(x) - y_bot(x)) dx = [I_B(1/2) - I_B(x1)] - int_{x1}^{1/2} y_bot(x) dx.
       - The antiderivative of s(t) is S(t) = (k/4) + int_0^{rem} s(u) du.
         By term-by-term integration: I_B(x) = sum_{n=0}^infty S(2^n x) / 4^n.
       - The circle integral is evaluated via substitution u = 4(x - 1/4) with standard antiderivative:
         int sqrt(1 - u^2) du = (1/2)(u sqrt(1 - u^2) + arcsin(u)).

    Complexity:
    -----------
    - Time Complexity: O(log(1/eps) * depth) operations (~0.001s).
    - Space Complexity: O(1) constant memory.
    """

    def s(x: float) -> float:
        x = x - math.floor(x)
        return min(x, 1.0 - x)

    def B(x: float) -> float:
        total = 0.0
        term = 1.0
        p = x
        for _ in range(60):
            val = s(p) / term
            total += val
            if val < 1e-18:
                break
            p *= 2.0
            term *= 2.0
        return total

    def S_val(t: float) -> float:
        k = math.floor(t)
        rem = t - k
        int_full = k * 0.25
        if rem <= 0.5:
            int_rem = rem * rem / 2.0
        else:
            int_rem = rem - rem * rem / 2.0 - 0.25
        return int_full + int_rem

    def I_blancmange(x: float) -> float:
        total = 0.0
        term = 1.0
        p = x
        for _ in range(60):
            val = S_val(p) / term
            total += val
            if val < 1e-18:
                break
            p *= 2.0
            term *= 4.0
        return total

    def y_circle_bot(x: float) -> float:
        return 0.5 - math.sqrt(x / 2.0 - x * x)

    # Binary search (bisection) for intersection point x1 in [0.05, 0.10]
    lo, hi = 0.05, 0.10
    for _ in range(100):
        mid = (lo + hi) / 2.0
        if B(mid) < y_circle_bot(mid):
            lo = mid
        else:
            hi = mid
    x1 = (lo + hi) / 2.0

    # Integral of Blancmange curve B(x) from x1 to 0.5
    int_B = I_blancmange(0.5) - I_blancmange(x1)

    # Integral of lower circle arc y_bot(x) from x1 to 0.5
    part1 = 0.5 * (0.5 - x1)
    u1 = 4.0 * (x1 - 0.25)
    u2 = 1.0

    def F_sqrt(u: float) -> float:
        return 0.5 * (u * math.sqrt(1.0 - u * u) + math.asin(u))

    int_sqrt = (1.0 / 16.0) * (F_sqrt(u2) - F_sqrt(u1))
    int_bot = part1 - int_sqrt

    ans_area = int_B - int_bot
    return f"{ans_area:.8f}"


if __name__ == "__main__":
    print(solve())
