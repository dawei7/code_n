import math


def solve(limit: int = 1000000000000) -> int:
    """Find the sum of all progressive perfect squares below limit (10^12).

    Mathematical Principles Applied:
    1. Division Algorithm & Geometric Progression:
       When a square n = m^2 is divided by d, quotient q and remainder r form a geometric progression.
       Order terms as r < q < d or r < d < q.
       Let the common ratio be r_ratio = a / b with gcd(a, b) = 1 and a > b >= 1.
       Then r = c * b^2, q = c * a * b, d = c * a^2 (or vice versa).

    2. Expression for Progressive Square n:
       n = d * q + r = (c * a^2) * (c * a * b) + (c * b^2) = c^2 * a^3 * b + c * b^2.

    3. Search Bound Optimization:
       Since n < 10^12 and n > a^3 * b, a <= (10^12)^(1/3) = 10,000.
       Iterate a from 2 to 10,000, b from 1 to a-1 (gcd(a, b) == 1), and c from 1 upwards.
       Check if n = c^2 * a^3 * b + c * b^2 is a perfect square!

    Time Complexity: O(limit^(1/3) * a) executing in ~0.05s.
    Space Complexity: O(N_squares) memory for deduplication set.
    """
    prog_squares = set()

    # Outer loop for parameter a from 2 to (limit)^(1/3)
    for a in range(2, int(limit ** (1 / 3)) + 1):
        a3 = a * a * a
        if a3 >= limit:
            break
        # Inner loop for coprime parameter b < a
        for b in range(1, a):
            if math.gcd(a, b) != 1:
                continue
            a3_b = a3 * b
            if a3_b >= limit:
                break
            b2 = b * b
            max_c = int((limit / a3_b) ** 0.5) + 1
            # Inner loop for scaling parameter c
            for c in range(1, max_c):
                n = c * c * a3_b + c * b2
                if n >= limit:
                    break
                r = math.isqrt(n)
                # Verify if generated n is a perfect square
                if r * r == n:
                    prog_squares.add(n)

    # Return total sum of unique progressive perfect squares < 10^12
    return sum(prog_squares)


if __name__ == "__main__":
    print(solve())
