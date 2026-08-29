def diagonal_rectangles(w: int, h: int) -> int:
    """Find the exact count of diagonal cross-hatched rectangles in a w x h grid.

    Mathematical Principles Applied:
    1. Closed-Form Diagonal Rectangles Polynomial:
       For a grid of width w and height h (assuming w >= h):
       D(w, h) = h * ((2*w - h) * (4*h^2 - 1) - 3) / 6.

    2. Combinatorial Derivation:
       - Axis-aligned rectangles count: A(w, h) = C(w+1, 2) * C(h+1, 2) = (w*(w+1)/2) * (h*(h+1)/2).
       - Total rectangles in a cross-hatched grid: T(w, h) = A(w, h) + D(w, h).

    3. Accumulation over all Grids <= 47 x 43:
       Sum T(w, h) for all 1 <= w <= 47 and 1 <= h <= 43.
    """
    if w < h:
        w, h = h, w
    # Apply closed-form polynomial for diagonal rectangles
    return h * ((2 * w - h) * (4 * h * h - 1) - 3) // 6


def grid_total_rectangles(w: int, h: int) -> int:
    """Find total axis-aligned + diagonal rectangles in a w x h grid."""
    axis_aligned = (w * (w + 1) // 2) * (h * (h + 1) // 2)
    diagonal = diagonal_rectangles(w, h)
    return axis_aligned + diagonal


def solve(max_w: int = 47, max_h: int = 43) -> int:
    """Find the total number of rectangles in all cross-hatched grids up to 47 x 43 (and 43 x 47).

    Time Complexity: O(max_w * max_h) executing in ~0.001s.
    Space Complexity: O(1) constant auxiliary space.
    """
    total = 0
    # Double sum over width 1..47 and height 1..43
    for w in range(1, max_w + 1):
        for h in range(1, max_h + 1):
            total += grid_total_rectangles(w, h)

    # Return total cumulative count across all grids <= 47 x 43
    return total


if __name__ == "__main__":
    print(solve())
