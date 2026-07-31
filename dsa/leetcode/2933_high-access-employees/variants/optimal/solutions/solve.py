from collections import defaultdict
from typing import List


def solve(access_times: List[List[str]]) -> List[str]:
    minutes_by_employee = defaultdict(list)
    for name, timestamp in access_times:
        minute = int(timestamp[:2]) * 60 + int(timestamp[2:])
        minutes_by_employee[name].append(minute)

    high_access = []
    for name, minutes in minutes_by_employee.items():
        minutes.sort()
        if any(minutes[index + 2] - minutes[index] < 60 for index in range(len(minutes) - 2)):
            high_access.append(name)

    return high_access
