def solve(s: int = 1000) -> int:
    """Find the product a * b * c for the unique Pythagorean triplet where a + b + c = s.

    Mathematical Principles Applied:
    1. Single Variable Elimination:
       Given a^2 + b^2 = c^2 and a + b + c = s:
       Substitute c = s - a - b:
       a^2 + b^2 = (s - a - b)^2
                 = s^2 + a^2 + b^2 - 2sa - 2sb + 2ab
       0 = s^2 - 2sa - 2sb + 2ab
       2b*(s - a) = s^2 - 2sa
       b = (s^2 / 2 - sa) / (s - a) = (s*(s/2 - a)) / (s - a)

    2. Search Range Bounds:
       Since a < b < c and a + b + c = s, a must be strictly less than s / 3.
       For s = 1000, 1 <= a < 333.

    3. Integer Division Condition:
       b is a valid integer iff numerator (s*s/2 - s*a) is divisible by denominator (s - a).

    Time Complexity: O(s) reduced to ~333 steps.
    Space Complexity: O(1) constant auxiliary space.
    """
    # Half perimeter squared term: s^2 / 2 = 1000^2 / 2 = 500,000
    s_sq_half = s * s // 2

    # Loop 'a' from 1 up to s // 3 (since a < b < c and a + b + c = s)
    for a in range(1, s // 3):
        # Numerator: s^2 / 2 - s * a
        num = s_sq_half - s * a

        # Denominator: s - a
        den = s - a

        # Check if numerator is evenly divisible by denominator
        if num % den == 0:
            # Exact integer value for 'b'
            b = num // den

            # Compute 'c' from perimeter s = a + b + c
            c = s - a - b

            # Verify strictly ordered triplet condition a < b < c
            if a < b < c:
                # Return the product a * b * c
                return a * b * c

    # Return -1 if no triplet is found (guaranteed to exist for s = 1000)
    return -1


if __name__ == "__main__":
    print(solve())
