from typing import List

def solve(processorTime: List[int], tasks: List[int]) -> int:
    """
    Calculates the minimum time to complete all tasks by greedily pairing
    the latest available processors with the longest tasks.
    """
    # Sort processors in descending order to pair the latest start times
    # with the largest tasks.
    processorTime.sort(reverse=True)
    
    # Sort tasks in ascending order.
    tasks.sort()
    
    max_completion_time = 0
    
    # Each processor handles 4 tasks.
    # We iterate through processors and pick the 4 largest remaining tasks.
    # Since tasks are sorted ascending, the largest tasks are at the end.
    task_idx = len(tasks) - 1
    
    for p_time in processorTime:
        # The current processor takes the 4 largest available tasks.
        # The time taken by this processor is p_time + max(assigned_tasks).
        # Because tasks are sorted, the largest task in this batch is at task_idx.
        current_processor_finish = p_time + tasks[task_idx]
        
        if current_processor_finish > max_completion_time:
            max_completion_time = current_processor_finish
            
        # Move to the next 4 largest tasks
        task_idx -= 4
        
    return max_completion_time
