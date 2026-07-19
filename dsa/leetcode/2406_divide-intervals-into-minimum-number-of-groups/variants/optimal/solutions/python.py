from typing import List

def solve(intervals: List[List[int]]) -> int:
    """
    Calculates the minimum number of groups required to partition intervals
    using a sweep-line approach.
    """
    starts = sorted([i[0] for i in intervals])
    ends = sorted([i[1] for i in intervals])
    
    groups = 0
    max_groups = 0
    end_ptr = 0
    
    # Sweep through the sorted start times
    for start in starts:
        # If the current interval starts before the earliest ending interval,
        # we need a new group.
        if start <= ends[end_ptr]:
            groups += 1
        else:
            # Otherwise, an interval has finished, so we can reuse that group.
            end_ptr += 1
            
        max_groups = max(max_groups, groups)
        
    return max_groups
