def solve(points: list[list[int]]) -> int:
    # Sort points: x ascending, then y descending.
    # This allows us to process points such that for any pair (i, j) with i < j,
    # we know points[i].x <= points[j].x.
    # By sorting y descending, if points[i].y >= points[j].y,
    # then points[j] is in the bottom-right quadrant relative to points[i].
    points.sort(key=lambda p: (p[0], -p[1]))
    
    n = len(points)
    count = 0
    
    for i in range(n):
        max_y = float('-inf')
        for j in range(i + 1, n):
            x1, y1 = points[i]
            x2, y2 = points[j]
            
            # Since we sorted by x ascending and y descending:
            # x1 <= x2 is guaranteed.
            # We only care about pairs where y1 >= y2.
            if y2 <= y1:
                # Check if any point k exists between i and j
                # such that x1 <= xk <= x2 and y2 <= yk <= y1.
                # Because of our sort, any k between i and j satisfies x1 <= xk <= x2.
                # We only need to check if yk is within [y2, y1].
                if y2 > max_y:
                    count += 1
                    max_y = y2
                    
    return count
