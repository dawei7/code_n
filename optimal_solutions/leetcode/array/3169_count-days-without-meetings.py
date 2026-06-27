def solve(days: int, meetings: list[list[int]]) -> int:
    if not meetings:
        return days
    
    # Sort meetings by start time
    meetings.sort()
    
    merged_days = 0
    # Initialize with the first meeting
    curr_start, curr_end = meetings[0]
    
    for i in range(1, len(meetings)):
        next_start, next_end = meetings[i]
        
        if next_start <= curr_end + 1:
            # Overlapping or contiguous, extend the current interval
            curr_end = max(curr_end, next_end)
        else:
            # Gap found, add the duration of the previous interval
            merged_days += (curr_end - curr_start + 1)
            curr_start, curr_end = next_start, next_end
            
    # Add the last interval
    merged_days += (curr_end - curr_start + 1)
    
    return days - merged_days
