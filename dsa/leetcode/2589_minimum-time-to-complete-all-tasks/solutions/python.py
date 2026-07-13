def solve(tasks: list[list[int]]) -> int:
    # Sort tasks by their end time to process them greedily
    tasks.sort(key=lambda x: x[1])
    
    # Find the maximum end time to determine the size of our timeline
    max_end = 0
    for task in tasks:
        if task[1] > max_end:
            max_end = task[1]
            
    # timeline[i] is True if time unit i is already marked as active
    timeline = [False] * (max_end + 1)
    
    for start, end, duration in tasks:
        # Count how many time units are already active in the current task's range
        active_count = 0
        for t in range(start, end + 1):
            if timeline[t]:
                active_count += 1
        
        # If we still need more time units, fill from the end backwards
        needed = duration - active_count
        if needed > 0:
            for t in range(end, start - 1, -1):
                if not timeline[t]:
                    timeline[t] = True
                    needed -= 1
                    if needed == 0:
                        break
                        
    # The result is the total number of True values in the timeline
    return sum(timeline)
