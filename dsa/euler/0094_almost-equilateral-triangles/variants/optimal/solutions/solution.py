def solve(limit: int = 1000000000) -> int:
    """Find sum of perimeters of all almost equilateral triangles with perimeters <= limit.
    
    Time Complexity: O(log limit)
    Space Complexity: O(1)
    """
    total_perim = 0

    # Case 1: b = a + 1 -> Perimeter P = 3a + 1
    a_prev, a_curr = 1, 5
    while True:
        p = 3 * a_curr + 1
        if p > limit:
            break
        total_perim += p
        a_next = 14 * a_curr - a_prev - 4
        a_prev, a_curr = a_curr, a_next

    # Case 2: b = a - 1 -> Perimeter P = 3a - 1
    a_prev, a_curr = 1, 17
    while True:
        p = 3 * a_curr - 1
        if p > limit:
            break
        total_perim += p
        a_next = 14 * a_curr - a_prev + 4
        a_prev, a_curr = a_curr, a_next

    return total_perim
