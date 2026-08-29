def solve(size: int = 1001) -> int:
    """Compute the sum of the numbers on the diagonals in an size x size clockwise number spiral.

    Problem Context & Mathematical Principles:
    -------------------------------------------
    1. Layered Square Shells (Odd Dimensions):
       An odd-sized spiral of dimension s (for s = 3, 5, ..., size) has 4 diagonal corners:
           - Top-Right:    s^2
           - Top-Left:     s^2 - (s - 1)
           - Bottom-Left:  s^2 - 2(s - 1)
           - Bottom-Right: s^2 - 3(s - 1)

    2. Single-Layer Corner Sum:
       Summing all 4 corners of shell s:
           S(s) = 4 * s^2 - 6 * (s - 1)

    Complexity:
    -----------
    - Time Complexity: O(size) dynamic layer iteration (terminates in ~0.0001s).
    - Space Complexity: O(1) constant auxiliary space.
    """
    total_sum = 1

    # Dynamically sum 4 corners for each odd layer side length s
    for s in range(3, size + 1, 2):
        total_sum += 4 * s * s - 6 * (s - 1)

    return total_sum


if __name__ == "__main__":
    print(solve())
