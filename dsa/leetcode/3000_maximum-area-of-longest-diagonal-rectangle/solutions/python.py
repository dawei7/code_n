from typing import List

def solve(dimensions: List[List[int]]) -> int:
    max_diag_sq = -1
    max_area = -1
    
    for w, h in dimensions:
        diag_sq = w * w + h * h
        area = w * h
        
        if diag_sq > max_diag_sq:
            max_diag_sq = diag_sq
            max_area = area
        elif diag_sq == max_diag_sq:
            if area > max_area:
                max_area = area
                
    return max_area
