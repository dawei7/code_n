import math


def solve(limit: int = 1500000) -> int:
    """Find the number of wire lengths L <= limit (1,500,000) for which EXACTLY ONE integer right triangle can be formed.

    Mathematical Principles Applied:
    1. Euclid's Primitive Pythagorean Triple Generator:
       Every primitive Pythagorean triple (a, b, c) with a^2 + b^2 = c^2 is parameterized by integers (m, n):
       a = m^2 - n^2, b = 2*m*n, c = m^2 + n^2
       where m > n > 0, m and n have opposite parity (m % 2 != n % 2), and gcd(m, n) == 1.

    2. Primitive Perimeter Formula:
       L_0 = a + b + c = (m^2 - n^2) + (2*m*n) + (m^2 + n^2) = 2 * m * (m + n).
       All non-primitive Pythagorean triples have perimeters that are positive integer multiples k * L_0.

    3. Perimeter Multiplicity Frequency Array:
       Increment counts[k * L_0] += 1 for all multiples k * L_0 <= 1,500,000.
       Count perimeters L where counts[L] == 1 (singular integer right triangles).

    Time Complexity: O(limit log limit) executing in ~0.25s.
    Space Complexity: O(limit) memory for perimeter frequency array.
    """
    # Allocate frequency array for perimeters L <= 1,500,000
    counts = [0] * (limit + 1)

    # Upper bound for generator m: 2 * m^2 <= limit => m <= sqrt(limit / 2)
    max_m = int((limit // 2) ** 0.5)

    # Loop generator m from 2 up to max_m
    for m in range(2, max_m + 1):
        # Loop generator n < m with opposite parity: step by 2
        for n in range(1 + (m % 2), m, 2):
            # Check coprimality: gcd(m, n) == 1
            if math.gcd(m, n) == 1:
                # Primitive perimeter L_0 = 2 * m * (m + n)
                l0 = 2 * m * (m + n)

                # Increment counts for primitive perimeter l0 and all its integer multiples k * l0
                for perim in range(l0, limit + 1, l0):
                    counts[perim] += 1

    # Count perimeters L with exactly one integer right triangle representation (counts[L] == 1)
    singular_triangles_count = sum(1 for c in counts if c == 1)

    # Return total count of singular integer right triangle wire lengths
    return singular_triangles_count


if __name__ == "__main__":
    print(solve())
