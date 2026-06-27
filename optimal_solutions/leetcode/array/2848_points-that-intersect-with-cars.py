from typing import List

def solve(nums: List[List[int]]) -> int:
    """
    Calculates the number of unique integer points covered by a list of intervals.
    Uses a set to track unique coordinates.
    """
    covered_points = set()
    
    for start, end in nums:
        # Add all integers in the inclusive range [start, end] to the set
        for point in range(start, end + 1):
            covered_points.add(point)
            
    return len(covered_points)
