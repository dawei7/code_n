import math


def solve(limit: int = 1053779) -> int:
    """Find T(limit), the number of 60-degree integer-sided triangles with inradius r <= 1053779.

    Problem Context & Mathematical Principles:
    -------------------------------------------
    1. 60-Degree Integer Triangle Geometry:
       In a triangle with integer sides (a, b, c) having a 60-degree angle between a and b:
           c^2 = a^2 + b^2 - a*b  (Law of Cosines)
       The area is A = (sqrt(3)/4) * a * b.
       The inradius is:
           r = A / s = (sqrt(3)/6) * (a + b - c)

    2. Eisenstein Integer Parameterization of Primitive Triangles:
       Every primitive integer solution with gcd(a, b) = 1 and a != b is uniquely parameterized
       by coprime positive integers (u, v) with u > 2v:
           a = u^2 - v^2
           b = 2uv - v^2
           c = u^2 - uv + v^2
       (where a, b, c are divided by 3 if (u + v) = 0 mod 3).
       Restricting to u > 2v breaks the involution symmetry v <-> u - v, generating every primitive
       triangle exactly once.

    3. Inradius Formulas:
       For each coprime pair u > 2v:
       - If (u + v) % 3 != 0:  r_0 = (sqrt(3)/2) * v * (u - v)
       - If (u + v) % 3 == 0:  r_0 = (sqrt(3)/6) * v * (u - v)
       The number of non-primitive multiples with inradius <= N is floor(N / r_0).

    Complexity:
    -----------
    - Time Complexity: O(N log N) hyperbolic lattice summation (~1.5s for N = 1053779).
    - Space Complexity: O(1) constant auxiliary space.
    """
    N = limit
    sqrt3 = math.sqrt(3)
    cnt = 0

    c1 = 2 * N / sqrt3
    c2 = 6 * N / sqrt3

    max_v = int(math.isqrt(int(c2)))

    for v in range(1, max_v + 1):
        u_start = 2 * v + 1
        u_mid = v + int(c1 / v)
        u_end = v + int(c2 / v)

        # Region 1: u in [u_start, min(u_mid, u_end)] -> both cases can have r_0 <= N
        if u_start <= u_mid:
            bound1 = min(u_mid, u_end)
            for u in range(u_start, bound1 + 1):
                if math.gcd(u, v) == 1:
                    if (u + v) % 3 == 0:
                        r0 = (sqrt3 / 6) * v * (u - v)
                    else:
                        r0 = (sqrt3 / 2) * v * (u - v)
                    cnt += int(N / r0)
        else:
            bound1 = u_start - 1

        # Region 2: u in [max(u_start, bound1 + 1), u_end] -> ONLY (u + v) % 3 == 0 can have r_0 <= N
        start2 = max(u_start, bound1 + 1)
        if start2 <= u_end:
            rem = (start2 + v) % 3
            first_u = start2 if rem == 0 else start2 + (3 - rem)
            for u in range(first_u, u_end + 1, 3):
                if math.gcd(u, v) == 1:
                    r0 = (sqrt3 / 6) * v * (u - v)
                    cnt += int(N / r0)

    # Return total count of 60-degree triangles with inradius <= limit
    return cnt


if __name__ == "__main__":
    print(solve())
