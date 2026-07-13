def solve(n: int, logs: list[list[int]]) -> int:
    max_duration = -1
    result_id = -1
    prev_time = 0
    
    for emp_id, end_time in logs:
        duration = end_time - prev_time
        
        if duration > max_duration:
            max_duration = duration
            result_id = emp_id
        elif duration == max_duration:
            if emp_id < result_id:
                result_id = emp_id
        
        prev_time = end_time
        
    return result_id
