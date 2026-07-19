def solve(points: list[list[int]]) -> int:
    point_set = set(tuple(p) for p in points)
    n = len(points)
    max_area = -1
    
    # Sort points to potentially optimize or just iterate
    # We iterate through all pairs of points as potential diagonals
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = points[i]
            x2, y2 = points[j]
            
            # A rectangle must have sides parallel to axes
            # So x1 != x2 and y1 != y2
            if x1 == x2 or y1 == y2:
                continue
            
            # Check if the other two corners exist
            p3 = (x1, y2)
            p4 = (x2, y1)
            
            if p3 in point_set and p4 in point_set:
                # Calculate area
                width = abs(x1 - x2)
                height = abs(y1 - y2)
                area = width * height
                
                # Check if any other point is inside or on the boundary
                min_x, max_x = min(x1, x2), max(x1, x2)
                min_y, max_y = min(y1, y2), max(y1, y2)
                
                is_valid = True
                for k in range(n):
                    px, py = points[k]
                    # Check if point is inside or on boundary
                    # We already know the 4 corners are in the set
                    if min_x <= px <= max_x and min_y <= py <= max_y:
                        if (px, py) not in {(x1, y1), (x2, y2), p3, p4}:
                            is_valid = False
                            break
                
                if is_valid:
                    max_area = max(max_area, area)
                    
    return max_area
