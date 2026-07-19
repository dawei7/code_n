"""Optimal app-local solution for LeetCode 1093."""


def solve(count: list[int]) -> list[float]:
    total = sum(count)
    weighted_sum = 0
    minimum = -1
    maximum = -1
    mode = 0

    for value, frequency in enumerate(count):
        if frequency:
            if minimum == -1:
                minimum = value
            maximum = value
            weighted_sum += value * frequency
        if frequency > count[mode]:
            mode = value

    left_rank = (total - 1) // 2
    right_rank = total // 2
    seen = 0
    left_value = -1
    right_value = -1
    for value, frequency in enumerate(count):
        seen += frequency
        if left_value == -1 and seen > left_rank:
            left_value = value
        if seen > right_rank:
            right_value = value
            break

    return [
        float(minimum),
        float(maximum),
        weighted_sum / total,
        (left_value + right_value) / 2.0,
        float(mode),
    ]
