import math


def is_pentagonal(p: int) -> bool:
    """Check if p is pentagonal P_n = n(3n-1)/2 via quadratic discriminant test."""
    val = 1 + 24 * p
    root = math.isqrt(val)
    return root * root == val and root % 6 == 5


def solve(start_h: int = 144) -> int:
    """Find the next triangle number after T_285 = P_165 = H_143 = 40755 that is also pentagonal and hexagonal.

    Mathematical Principles Applied:
    1. Hexagonal-Triangular Identity:
       Every hexagonal number H_m = m*(2m - 1) is automatically a triangle number:
       H_m = m*(2m - 1) = (2m - 1)*(2m) / 2 = T_{2m - 1}.
       Therefore, we DO NOT need to check triangularity; every hexagonal number is triangular!

    2. Single Test Search:
       Iterate hexagonal index m starting at 144 (since H_143 = 40755), and test if H_m is pentagonal.

    Time Complexity: O(m) for m ≈ 27,693 (executes in ~0.007s).
    Space Complexity: O(1) constant auxiliary space.
    """
    # Start search at hexagonal index m = 144
    m = start_h

    while True:
        # Compute m-th hexagonal number: H_m = m * (2m - 1)
        h = m * (2 * m - 1)

        # Test if H_m is also a pentagonal number
        if is_pentagonal(h):
            # Return matching number
            return h

        # Advance to next hexagonal index
        m += 1


if __name__ == "__main__":
    print(solve())
