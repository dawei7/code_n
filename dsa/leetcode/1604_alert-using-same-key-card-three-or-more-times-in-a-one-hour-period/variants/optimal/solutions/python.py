from collections import defaultdict


def solve(keyName: list[str], keyTime: list[str]) -> list[str]:
    uses_by_name: dict[str, list[int]] = defaultdict(list)
    for name, timestamp in zip(keyName, keyTime):
        hour, minute = map(int, timestamp.split(":"))
        uses_by_name[name].append(hour * 60 + minute)

    alerted = []
    for name, uses in uses_by_name.items():
        uses.sort()
        if any(uses[i] - uses[i - 2] <= 60 for i in range(2, len(uses))):
            alerted.append(name)

    return sorted(alerted)
