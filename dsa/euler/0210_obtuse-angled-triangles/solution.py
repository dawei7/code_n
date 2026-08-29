import math


def solve(r: int = 10**9) -> int:
    """Find N(r), the number of points B in S(r) such that triangle OBC is obtuse for r = 10^9.

    Problem Context & Mathematical Principles:
    -------------------------------------------
    1. Obtuse Angle Partition & Disjoint Regions:
       For S(r) = {(x, y) in Z^2 : |x| + |y| <= r}, O = (0, 0), and C = (r/4, r/4) = (2k, 2k)
       where r = 8k, triangle OBC is obtuse iff point B(x, y) in S(r) satisfies one of 3 mutually
       disjoint geometric conditions:
       - Region 1 (Angle at O > 90 deg): x + y < 0. Count c1 = 64 * k^2 + 4 * k.
       - Region 2 (Angle at C > 90 deg): x + y > 4k. Count c2 = 32 * k^2 + 2 * k.
       - Region 3 (Angle at B > 90 deg): (x - k)^2 + (y - k)^2 < 2 * k^2 (Thales' circle interior).

    2. Gauss Circle Interior Lattice Count (Region 3):
       Shift origin to (k, k). Region 3 corresponds to integer points (u, v) strictly inside u^2 + v^2 < 2*k^2.
       By 8-fold symmetry of the circle:
       c3 = 1 + 4 * isqrt(2k^2 - 1) + 4*(k - 1) + 8 * (k*(k - 1)//2 + sum_{u=k+1}^{isqrt(2k^2 - 1)} isqrt(2k^2 - 1 - u^2)).

    3. Collinear Points Deduction:
       Points B on the line y = x passing through O(0, 0) and C(2k, 2k) are collinear with O and C,
       forming degenerate line segments rather than valid non-degenerate triangles.
       There are 4k collinear points in Region 1 (x < 0), 2k in Region 2 (x > 2k), and 2k - 1 in
       Region 3 (0 < x < 2k), totaling 8k - 1 collinear points that must be deducted.

    Complexity:
    -----------
    - Time Complexity: O((sqrt(2) - 1) * r / 8) operations (~3.4s for r = 10^9).
    - Space Complexity: O(1) constant auxiliary space.
    """
    k = r // 8
    R2 = 2 * k * k - 1

    # Region 1 + Region 2 closed form count
    c1_c2 = 96 * k * k + 6 * k

    # Region 3 (Gauss Circle Interior Count)
    ans_c3 = 1 + 4 * math.isqrt(R2) + 4 * (k - 1)

    # Swapped summation over the circular cap u in [k + 1, isqrt(R2)]
    sum_tri = k * (k - 1) // 2
    sum_d = 0
    isqrt = math.isqrt
    max_u = isqrt(R2)

    for u in range(k + 1, max_u + 1):
        sum_d += isqrt(R2 - u * u)

    ans_c3 += 8 * (sum_tri + sum_d)

    # Deduct 8k - 1 collinear points lying on line y = x
    collinear = 8 * k - 1

    # Total N(r)
    return c1_c2 + ans_c3 - collinear


if __name__ == "__main__":
    print(solve())
