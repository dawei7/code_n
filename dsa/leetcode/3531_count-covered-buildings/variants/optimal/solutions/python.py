def solve(buildings: list[list[int]]) -> int:
    """
    Counts the number of buildings that are fully covered by another building.
    A building [s1, e1] is covered by [s2, e2] if s2 <= s1 and e1 <= e2.
    """
    if not buildings:
        return 0
    
    # Sort by start coordinate ascending. 
    # If start coordinates are equal, sort by end coordinate descending.
    # This ensures that if a building covers another, the covering building
    # appears first in the list.
    buildings.sort(key=lambda x: (x[0], -x[1]))
    
    covered_count = 0
    max_end = -float('inf')
    
    for _, end in buildings:
        # If the current building's end is within the max_end seen so far,
        # it is covered by a previous building (since its start is >= previous start).
        if end <= max_end:
            covered_count += 1
        else:
            # Update the furthest end coordinate seen so far
            max_end = end
            
    return covered_count
