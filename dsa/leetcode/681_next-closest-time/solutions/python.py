from itertools import product


def solve(time: str) -> str:
    allowed = set(time.replace(":", ""))
    start = int(time[:2]) * 60 + int(time[3:])
    best_distance = 1441
    best_time = time

    for first, second, third, fourth in product(allowed, repeat=4):
        hour = int(first + second)
        minute = int(third + fourth)
        if hour >= 24 or minute >= 60:
            continue

        candidate = hour * 60 + minute
        distance = (candidate - start) % 1440
        if distance == 0:
            distance = 1440
        if distance < best_distance:
            best_distance = distance
            best_time = f"{hour:02d}:{minute:02d}"

    return best_time

