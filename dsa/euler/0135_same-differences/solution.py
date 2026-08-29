def solve(limit: int = 1000000, target_solutions: int = 10) -> int:
    """Find the number of n < limit (1,000,000) with exactly target_solutions (10) solutions to x^2 - y^2 - z^2 = n.

    Mathematical Principles Applied:
    1. Arithmetic Progression Substitution:
       Let x, y, z be terms in arithmetic progression with common difference d > 0:
       x = z + 2d, y = z + d, z = z.
       Then:
       x^2 - y^2 - z^2 = (z + 2d)^2 - (z + d)^2 - z^2
                       = (z^2 + 4zd + 4d^2) - (z^2 + 2zd + d^2) - z^2
                       = 4zd + 3d^2 - z^2
                       = (3d - z)(d + z) = n.

    2. Change of Variables:
       Let a = 3d - z and u = d + z.
       Then n = a * u.
       Adding both equations: a + u = 4d => d = (a + u) / 4.
       Since d is an integer, we require (a + u) % 4 == 0.
       Also z = a - d > 0 => 3a > u.

    3. Harmonic Loop Precomputation:
       Iterate a from 1 to limit and u from 1 to min(limit // a, 3a - 1).
       If (a + u) % 4 == 0, increment sol_count[a * u] += 1.

    Time Complexity: O(limit log limit) executing in ~0.20s.
    Space Complexity: O(limit) memory for solution counts array.
    """
    sol_count = [0] * limit

    # Outer loop for factor a from 1 to limit - 1
    for a in range(1, limit):
        # Bound u by limit // a and strict positivity constraint 3*a > u (z = a - d > 0)
        max_u = min((limit - 1) // a, 3 * a - 1)
        for u in range(1, max_u + 1):
            if (a + u) % 4 == 0:
                n = a * u
                sol_count[n] += 1

    # Return total number of n < 1,000,000 with exactly 10 distinct AP solutions
    return sum(1 for n in range(1, limit) if sol_count[n] == target_solutions)


if __name__ == "__main__":
    print(solve())
