def solve(events: list[list[int]]) -> int:
    max_duration = -1
    result_index = -1
    prev_time = 0
    
    for index, time in events:
        duration = time - prev_time
        
        if duration > max_duration:
            max_duration = duration
            result_index = index
        elif duration == max_duration:
            if index < result_index:
                result_index = index
        
        prev_time = time
        
    return result_index
