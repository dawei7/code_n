def solve(n: int, rectangles: list[list[int]]) -> bool:
    def can_cut(intervals):
        # Sort intervals by start point
        intervals.sort()
        
        count = 0
        current_end = 0
        
        for start, end in intervals:
            # If there is a gap between the current end and the next start,
            # we can potentially place a cut here.
            if start >= current_end:
                count += 1
                current_end = end
            else:
                current_end = max(current_end, end)
        
        # If we found at least 2 gaps, we can create 3 sections.
        # The logic: if we have 2 gaps, we have 3 segments.
        return count >= 3

    # Check horizontal cuts (using y-coordinates)
    # A horizontal cut is possible if we can find 2 lines y=k1, y=k2
    # that don't intersect any rectangle.
    y_intervals = [[r[1], r[3]] for r in rectangles]
    if can_cut(y_intervals):
        return True
        
    # Check vertical cuts (using x-coordinates)
    x_intervals = [[r[0], r[2]] for r in rectangles]
    if can_cut(x_intervals):
        return True
        
    return False
