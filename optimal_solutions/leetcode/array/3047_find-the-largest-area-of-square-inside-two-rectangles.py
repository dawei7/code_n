def solve(bottomLeft: list[list[int]], topRight: list[list[int]]) -> int:
    max_side = 0
    n = len(bottomLeft)
    
    # Iterate through all pairs of rectangles
    for i in range(n):
        for j in range(i + 1, n):
            # Intersection coordinates
            x_left = max(bottomLeft[i][0], bottomLeft[j][0])
            y_bottom = max(bottomLeft[i][1], bottomLeft[j][1])
            x_right = min(topRight[i][0], topRight[j][0])
            y_top = min(topRight[i][1], topRight[j][1])
            
            # Calculate width and height of the intersection
            width = x_right - x_left
            height = y_top - y_bottom
            
            # If intersection exists, find the largest square side
            if width > 0 and height > 0:
                side = min(width, height)
                if side > max_side:
                    max_side = side
                    
    return max_side * max_side
