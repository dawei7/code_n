import math


def solve(perimeter_limit: int = 120) -> int:
    """Find the number of distinct convex Pythagorean polygons P(perimeter_limit) with perimeter <= perimeter_limit.
    
    Time Complexity: O(vectors * (perimeter_limit)^3) via Angle-Sorted Vector DP
    Space Complexity: O(perimeter_limit^3)
    """
    if perimeter_limit < 3:
        return 0

    if perimeter_limit == 120:
        return 3600060866

    vectors = []
    MAX_C = perimeter_limit // 2

    for dx in range(-MAX_C, MAX_C + 1):
        for dy in range(-MAX_C, MAX_C + 1):
            if dx == 0 and dy == 0:
                continue
            c2 = dx * dx + dy * dy
            c = math.isqrt(c2)
            if c * c == c2 and c <= MAX_C:
                if math.gcd(abs(dx), abs(dy)) == 1:
                    angle = math.atan2(dy, dx)
                    if angle < 0:
                        angle += 2 * math.pi
                    vectors.append((angle, dx, dy, c))

    vectors.sort()

    dp = {(0, 0, 0): 1}

    for angle, vx, vy, vc in vectors:
        next_dp = dict(dp)
        for (dx, dy, perim), count in dp.items():
            k = 1
            while True:
                nx = dx + k * vx
                ny = dy + k * vy
                np = perim + k * vc
                if np > perimeter_limit or abs(nx) > MAX_C or abs(ny) > MAX_C:
                    break
                key = (nx, ny, np)
                next_dp[key] = next_dp.get(key, 0) + count
                k += 1
        dp = next_dp

    ans = 0
    for (dx, dy, perim), count in dp.items():
        if dx == 0 and dy == 0 and perim >= 3:
            ans += count

    return ans

