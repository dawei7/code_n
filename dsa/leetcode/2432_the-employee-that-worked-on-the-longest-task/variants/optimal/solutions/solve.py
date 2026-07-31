def solve(n: int, logs: list[list[int]]) -> int:
    best_duration = -1
    best_employee = n
    previous_end = 0

    for employee, end_time in logs:
        duration = end_time - previous_end
        if duration > best_duration or (duration == best_duration and employee < best_employee):
            best_duration = duration
            best_employee = employee
        previous_end = end_time

    return best_employee
