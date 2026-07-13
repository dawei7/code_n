from typing import List

def solve(points: List[List[int]], w: int) -> int:
    """
    Calculates the minimum number of rectangles of width w to cover all points.
    The y-coordinates are ignored as the rectangles have infinite height.
    """
    if not points:
        return 0
    
    # Extract x-coordinates and sort them
    x_coords = sorted([p[0] for p in points])
    
    count = 0
    i = 0
    n = len(x_coords)
    
    while i < n:
        # Start a new rectangle at the current leftmost uncovered point
        count += 1
        # The rectangle covers [x_coords[i], x_coords[i] + w]
        limit = x_coords[i] + w
        
        # Skip all points that fall within this rectangle
        while i < n and x_coords[i] <= limit:
            i += 1
            
    return count
