from collections import defaultdict


def solve(access_times: list[list[str]]) -> list[str]:
    minutes_by_employee: dict[str, list[int]] = defaultdict(list)
    for name, timestamp in access_times:
        minute = int(timestamp[:2]) * 60 + int(timestamp[2:])
        minutes_by_employee[name].append(minute)

    high_access = []
    for name, minutes in minutes_by_employee.items():
        minutes.sort()
        if any(minutes[index + 2] - minutes[index] < 60 for index in range(len(minutes) - 2)):
            high_access.append(name)

    return sorted(high_access)
