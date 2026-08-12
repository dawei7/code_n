def diagonal_rectangles(w: int, h: int) -> int:
    """Find number of diagonal cross-hatched rectangles in a w x h grid."""
    if w < h:
        w, h = h, w
    return h * ((2 * w - h) * (4 * h * h - 1) - 3) // 6


def grid_total_rectangles(w: int, h: int) -> int:
    """Find total axis-aligned + diagonal rectangles in a w x h grid."""
    axis_aligned = (w * (w + 1) // 2) * (h * (h + 1) // 2)
    diagonal = diagonal_rectangles(w, h)
    return axis_aligned + diagonal


def solve(max_w: int = 47, max_h: int = 43) -> int:
    """Find total number of rectangles in all cross-hatched grids up to max_w x max_h.
    
    Time Complexity: O(max_w * max_h)
    Space Complexity: O(1)
    """
    total = 0
    for w in range(1, max_w + 1):
        for h in range(1, max_h + 1):
            total += grid_total_rectangles(w, h)

    return total
