import math


def solve(k: int = 2000000) -> str:
    """Find d(k) rounded to 9 decimal places: shortest Euclidean distance among 2,000,000 points.

    Blum Blum Shub PRNG generation and O(k log k) sweep-line closest pair algorithm.

    Time Complexity: O(k log k)
    Space Complexity: O(k)
    """
    MOD = 50515093
    s = 290797
    coords = [0] * (2 * k)
    for i in range(2 * k):
        coords[i] = s
        s = (s * s) % MOD

    pts = [(coords[2 * i], coords[2 * i + 1]) for i in range(k)]
    pts.sort(key=lambda p: p[0])

    min_d2 = float("inf")
    left = 0

    for i in range(k):
        px, py = pts[i]
        limit_dx = math.isqrt(int(min_d2)) + 1 if min_d2 != float("inf") else MOD
        while pts[i][0] - pts[left][0] >= limit_dx:
            left += 1
        for j in range(left, i):
            dx = px - pts[j][0]
            dy = py - pts[j][1]
            d2 = dx * dx + dy * dy
            if d2 < min_d2:
                min_d2 = d2

    min_dist = math.sqrt(min_d2)
    return f"{min_dist:.9f}"


if __name__ == "__main__":
    print(solve())
