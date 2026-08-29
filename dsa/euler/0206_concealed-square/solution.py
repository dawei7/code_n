import math


def solve() -> int:
    """Find the unique positive integer x whose square has the form 1_2_3_4_5_6_7_8_9_0.

    Problem Context & Mathematical Principles:
    -------------------------------------------
    1. Modular Arithmetic on Last Digits:
       Since x^2 ends in 0, x^2 must end in 00, which implies x = 10 * y and x^2 = 100 * y^2.
       The pattern for y^2 becomes 1_2_3_4_5_6_7_8_9 (ending in 9).
       A square ending in 9 MUST end in 3 or 7, so y = 3 (mod 10) or y = 7 (mod 10).

    2. Square Root Range Bounds:
       Smallest candidate y^2 >= 10203040506070809 => min_y = math.isqrt(10203040506070809) = 101010101.
       Largest candidate y^2 <= 19293949596979899 => max_y = math.isqrt(19293949596979899) = 138902662.

    3. Stepped Descending Search:
       Iterating downwards from max_y to min_y across candidates ending in 7 and 3 tests the most
       likely candidates first, locating the solution in fewer than 1000 iterations!

    Complexity:
    -----------
    - Time Complexity: O(1) expected (~0.0001s).
    - Space Complexity: O(1) constant auxiliary space.
    """
    min_y = math.isqrt(10203040506070809)
    max_y = math.isqrt(19293949596979899)

    # Search candidates ending in 7 and 3 downwards from max_y
    base = (max_y // 10) * 10
    while base >= min_y:
        for offset in (7, 3):
            cand = base + offset
            if min_y <= cand <= max_y:
                s = str(cand * cand)
                if (
                    s[0] == "1"
                    and s[2] == "2"
                    and s[4] == "3"
                    and s[6] == "4"
                    and s[8] == "5"
                    and s[10] == "6"
                    and s[12] == "7"
                    and s[14] == "8"
                ):
                    return cand * 10
        base -= 10

    return 0


if __name__ == "__main__":
    print(solve())
