"""Optimal solution for LeetCode 1093: Statistics from a Large Sample."""


def solve(count: list[int]) -> list[float]:
    total_count = sum(count)
    minimum = next(i for i, freq in enumerate(count) if freq)
    maximum = next(i for i in range(255, -1, -1) if count[i])
    mean = sum(i * freq for i, freq in enumerate(count)) / total_count
    mode = max(range(256), key=lambda i: count[i])

    def kth(k: int) -> int:
        seen = 0
        for value, freq in enumerate(count):
            seen += freq
            if seen >= k:
                return value
        return 255

    if total_count % 2:
        median = float(kth(total_count // 2 + 1))
    else:
        median = (kth(total_count // 2) + kth(total_count // 2 + 1)) / 2
    return [float(minimum), float(maximum), mean, median, float(mode)]
