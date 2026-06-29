import sys


def max_delish_difference(values: list[int]) -> int:
    n = len(values)
    left_max = [0] * n
    left_min = [0] * n
    right_max = [0] * n
    right_min = [0] * n

    current_max = current_min = values[0]
    left_max[0] = left_min[0] = values[0]
    for i in range(1, n):
        value = values[i]
        current_max = max(value, current_max + value)
        current_min = min(value, current_min + value)
        left_max[i] = max(left_max[i - 1], current_max)
        left_min[i] = min(left_min[i - 1], current_min)

    current_max = current_min = values[-1]
    right_max[-1] = right_min[-1] = values[-1]
    for i in range(n - 2, -1, -1):
        value = values[i]
        current_max = max(value, current_max + value)
        current_min = min(value, current_min + value)
        right_max[i] = max(right_max[i + 1], current_max)
        right_min[i] = min(right_min[i + 1], current_min)

    answer = 0
    for split in range(n - 1):
        answer = max(
            answer,
            abs(left_max[split] - right_min[split + 1]),
            abs(left_min[split] - right_max[split + 1]),
        )
    return answer


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    t = data[0]
    idx = 1
    out: list[str] = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        values = data[idx : idx + n]
        idx += n
        out.append(str(max_delish_difference(values)))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
