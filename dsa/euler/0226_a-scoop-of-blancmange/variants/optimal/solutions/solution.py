import math


def s(x: float) -> float:
    x = x - math.floor(x)
    return min(x, 1.0 - x)


def B(x: float) -> float:
    total = 0.0
    term = 1.0
    p = x
    for _ in range(50):
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
    total = x * x / 2.0
    term = 1.0 / 4.0
    p = x
    for _ in range(50):
        val = term * S_val(p)
        total += val
        if val < 1e-18:
            break
        p *= 2.0
        term /= 4.0
    return total


def y_circle_bot(x: float) -> float:
    return 0.5 - math.sqrt(x / 2.0 - x * x)


def solve() -> str:
    """Find area under blancmange curve enclosed by circle C, rounded to 8 decimal places.
    
    Time Complexity: O(log(1 / eps)) via binary root finding + exact Takagi series integration
    Space Complexity: O(1)
    """
    lo, hi = 0.05, 0.10
    for _ in range(100):
        mid = (lo + hi) / 2.0
        if B(mid) < y_circle_bot(mid):
            lo = mid
        else:
            hi = mid
    x1 = (lo + hi) / 2.0

    int_B = I_blancmange(0.5) - I_blancmange(x1)

    part1 = 0.5 * (0.5 - x1)
    u1 = 4.0 * (x1 - 0.25)
    u2 = 1.0

    def F_sqrt(u):
        return 0.5 * (u * math.sqrt(1.0 - u * u) + math.asin(u))

    int_sqrt = (1.0 / 16.0) * (F_sqrt(u2) - F_sqrt(u1))
    int_bot = part1 - int_sqrt

    ans_area = int_B - int_bot
    return f"{ans_area:.8f}"
