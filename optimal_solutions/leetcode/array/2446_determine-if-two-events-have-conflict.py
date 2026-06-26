from typing import List

def solve(event1: List[str], event2: List[str]) -> bool:
    """
    Determines if two time intervals overlap.
    Since the time format is HH:MM, lexicographical comparison is equivalent
    to chronological comparison.
    """
    start1, end1 = event1
    start2, end2 = event2
    
    # Two intervals [s1, e1] and [s2, e2] overlap if:
    # The start of one is before or at the end of the other,
    # AND the start of the other is before or at the end of the first.
    # Simplified: max(start1, start2) <= min(end1, end2)
    
    return max(start1, start2) <= min(end1, end2)
