"""Optimal app-local solution for LeetCode 362: Design Hit Counter."""


def solve(operations: list[list]) -> list[int]:
    timestamps = [0] * 300
    counts = [0] * 300
    results: list[int] = []

    for operation in operations:
        name = operation[0]
        timestamp = operation[1]

        if name == "hit":
            slot = timestamp % 300
            if timestamps[slot] != timestamp:
                timestamps[slot] = timestamp
                counts[slot] = 1
            else:
                counts[slot] += 1
        elif name == "getHits":
            total = 0
            for stored_timestamp, count in zip(timestamps, counts):
                if timestamp - stored_timestamp < 300:
                    total += count
            results.append(total)
        else:
            raise ValueError(f"Unsupported HitCounter operation: {name}")

    return results

