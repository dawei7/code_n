import math


def solve(limit: int = 10**5) -> str:
    """Find the expected value of Albert's total score over 10^5 turns, rounded to 5 decimal places.
    
    Time Complexity: O(limit) via Closed-Form Circular Segment Integral
    Space Complexity: O(1)
    """

    def area_circle_corner(r):
        if r <= 1.0:
            return 0.0
        x_max = math.sqrt(r * r - 1.0)

        def I(x):
            return 0.5 * (
                x * math.sqrt(r * r - x * x)
                + r * r * math.atan2(x, math.sqrt(r * r - x * x))
            )

        return (I(x_max) - I(1.0)) - (x_max - 1.0)

    total_expected = 0.0
    for k in range(1, limit + 1):
        R1 = k - 0.5
        R2 = k + 0.5
        a1 = area_circle_corner(R1)
        a2 = area_circle_corner(R2)
        p_k = (a2 - a1) / (k * k)
        total_expected += k * p_k

    return f"{total_expected:.5f}"
