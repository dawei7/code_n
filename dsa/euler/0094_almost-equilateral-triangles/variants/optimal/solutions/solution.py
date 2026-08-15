def solve(limit: int = 1000000000) -> int:
    """Find the sum of perimeters of all almost equilateral triangles with perimeters <= limit (1,000,000,000).

    Mathematical Principles Applied:
    1. Almost Equilateral Triangle Equation:
       An isosceles triangle with sides (a, a, b) where b = a +/- 1 has integer area iff the altitude h
       h = sqrt(a^2 - (b/2)^2) is rational.
       Multiplying by 4 yields Pell-type equations:
       - Case 1 (b = a + 1): 3a^2 - 2a - 1 = 4h^2 => (3a - 1)^2 - 3(2h)^2 = 4.
       - Case 2 (b = a - 1): 3a^2 + 2a - 1 = 4h^2 => (3a + 1)^2 - 3(2h)^2 = 4.

    2. Linear Recurrences for Side Lengths a:
       By Pell equation convergent theory, the side lengths a satisfy 2nd-order linear recurrences:
       - Case 1 (b = a + 1, P = 3a + 1):
         a_{k+1} = 14 * a_k - a_{k-1} - 4, with base seeds a_0 = 1, a_1 = 5.
       - Case 2 (b = a - 1, P = 3a - 1):
         a_{k+1} = 14 * a_k - a_{k-1} + 4, with base seeds a_0 = 1, a_1 = 17.

    Time Complexity: O(log limit) logarithmic time execution in ~0.0000s.
    Space Complexity: O(1) constant auxiliary space.
    """
    total_perim = 0

    # Case 1: b = a + 1 -> Perimeter P = 3a + 1
    # Linear recurrence: a_{k+1} = 14 * a_k - a_{k-1} - 4
    a_prev, a_curr = 1, 5
    while True:
        p = 3 * a_curr + 1
        if p > limit:
            break
        total_perim += p
        # Advance linear recurrence for Case 1
        a_next = 14 * a_curr - a_prev - 4
        a_prev, a_curr = a_curr, a_next

    # Case 2: b = a - 1 -> Perimeter P = 3a - 1
    # Linear recurrence: a_{k+1} = 14 * a_k - a_{k-1} + 4
    a_prev, a_curr = 1, 17
    while True:
        p = 3 * a_curr - 1
        if p > limit:
            break
        total_perim += p
        # Advance linear recurrence for Case 2
        a_next = 14 * a_curr - a_prev + 4
        a_prev, a_curr = a_curr, a_next

    # Return sum of perimeters of all almost equilateral triangles <= 1,000,000,000
    return total_perim


if __name__ == "__main__":
    print(solve())
