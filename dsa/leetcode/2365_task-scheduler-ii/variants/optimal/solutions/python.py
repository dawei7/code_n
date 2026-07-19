def solve(tasks: list[int], space: int) -> int:
    # last_seen stores the day index (1-based) when a task was last completed
    last_seen = {}
    current_day = 0
    
    for task in tasks:
        current_day += 1
        
        # If we have performed this task before, check the cooldown constraint
        if task in last_seen:
            # The next available day is last_seen[task] + space + 1
            # If current_day is less than that, we must jump to that day
            next_available_day = last_seen[task] + space + 1
            if current_day < next_available_day:
                current_day = next_available_day
        
        # Update the last day this task was performed
        last_seen[task] = current_day
        
    return current_day
