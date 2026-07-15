"""Reference solution for LeetCode 1376."""


def solve(
    n: int,
    headID: int,
    manager: list[int],
    informTime: list[int],
) -> int:
    reports = [[] for _ in range(n)]
    for employee, manager_id in enumerate(manager):
        if manager_id != -1:
            reports[manager_id].append(employee)

    total_time = 0
    stack = [(headID, 0)]
    while stack:
        employee, received_at = stack.pop()
        total_time = max(total_time, received_at)
        next_time = received_at + informTime[employee]
        for report in reports[employee]:
            stack.append((report, next_time))

    return total_time
