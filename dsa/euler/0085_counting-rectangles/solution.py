def solve(target: int = 2000000) -> int:
    """Find the area of the grid with the nearest number of contained sub-rectangles to target (2,000,000).

    Mathematical Principles Applied:
    1. Sub-Rectangle Counting Formula:
       In a grid of width w and height h, a sub-rectangle is formed by choosing 2 vertical lines from (w + 1) lines,
       and 2 horizontal lines from (h + 1) lines.
       Number of contained sub-rectangles = C(w + 1, 2) * C(h + 1, 2)
       = (w * (w + 1) / 2) * (h * (h + 1) / 2).

    2. Bounded Grid Search & Symmetry Breaking:
       Search width w from 1 up to 2000 and height h from 1 up to w.
       Minimize the absolute difference |rectangles - target| and track best_area = w * h.

    Time Complexity: O(sqrt(target)) executing in ~0.002s.
    Space Complexity: O(1) constant auxiliary space.
    """
    best_diff = float("inf")
    best_area = 0

    # Search width w
    for w in range(1, 2000):
        # Search height h <= w to break symmetry
        for h in range(1, w + 1):
            # Calculate total contained sub-rectangles in a w x h grid
            rects = (w * (w + 1) // 2) * (h * (h + 1) // 2)
            diff = abs(rects - target)

            # Update minimal absolute difference and corresponding grid area w * h
            if diff < best_diff:
                best_diff = diff
                best_area = w * h

            # Break inner height loop if total sub-rectangles exceed target
            if rects > target:
                break

    # Return grid area obtaining nearest number of sub-rectangles to 2,000,000
    return best_area


if __name__ == "__main__":
    print(solve())
