def solve(points: list[list[int]]) -> int:
    # Sort points: x ascending, then y descending.
    # This ensures that if i < j, then points[i][0] <= points[j][0].
    # If points[i][0] <= points[j][0] and points[i][1] >= points[j][1],
    # then point i is top-left of point j.
    points.sort(key=lambda p: (p[0], -p[1]))
    
    n = len(points)
    count = 0
    
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = points[i]
            x2, y2 = points[j]
            
            # Since we sorted by x ascending and y descending:
            # x1 <= x2 is guaranteed.
            # We need y1 >= y2 for point i to be top-left of point j.
            if y1 >= y2:
                # Check if any other point k is inside the rectangle defined by i and j.
                # A point k is inside if x1 <= xk <= x2 and y2 <= yk <= y1.
                # We already know i and j are the corners.
                is_valid = True
                for k in range(n):
                    if k == i or k == j:
                        continue
                    
                    xk, yk = points[k]
                    if x1 <= xk <= x2 and y2 <= yk <= y1:
                        is_valid = False
                        break
                
                if is_valid:
                    count += 1
                    
    return count
