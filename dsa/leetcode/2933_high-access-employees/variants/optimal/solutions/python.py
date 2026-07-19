from collections import defaultdict

def solve(access_times: list[list[str]]) -> list[str]:
    # Group access times by employee
    employee_map = defaultdict(list)
    for name, time_str in access_times:
        # Convert HHMM to total minutes from start of day
        hours = int(time_str[:2])
        minutes = int(time_str[2:])
        total_minutes = hours * 60 + minutes
        employee_map[name].append(total_minutes)
    
    high_access_employees = []
    
    for name, times in employee_map.items():
        # We need at least 3 accesses to qualify
        if len(times) < 3:
            continue
            
        # Sort times to check sliding window
        times.sort()
        
        # Check if any 3 accesses occur within a 60-minute window
        # If times[i+2] - times[i] < 60, then times[i], times[i+1], times[i+2]
        # are all within a 60-minute range.
        for i in range(len(times) - 2):
            if times[i + 2] - times[i] < 60:
                high_access_employees.append(name)
                break
                
    return high_access_employees
