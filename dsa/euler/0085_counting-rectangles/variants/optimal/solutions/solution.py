def solve(target: int = 2000000) -> int:
    """Find area of grid with nearest number of contained sub-rectangles to target.
    
    Time Complexity: O(W * H)
    Space Complexity: O(1)
    """
    best_diff = float('inf')
    best_area = 0

    for w in range(1, 2000):
        for h in range(1, w + 1):
            rects = (w * (w + 1) // 2) * (h * (h + 1) // 2)
            diff = abs(rects - target)

            if diff < best_diff:
                best_diff = diff
                best_area = w * h

            if rects > target:
                break

    return best_area
