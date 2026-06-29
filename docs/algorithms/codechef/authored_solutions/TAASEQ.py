import sys


def is_arithmetic_after_removal(values: list[int], remove: int) -> bool:
    remaining = [values[i] for i in range(len(values)) if i != remove]
    if len(remaining) <= 2:
        return True
    diff = remaining[1] - remaining[0]
    return all(remaining[i] - remaining[i - 1] == diff for i in range(2, len(remaining)))


def removed_value(values: list[int]) -> int:
    n = len(values)
    if n <= 2:
        return min(values)

    candidates = {0, 1, n - 1}
    diff = values[1] - values[0]
    previous = values[0]
    for i in range(1, n):
        if values[i] - previous != diff:
            candidates.add(i)
            candidates.add(i - 1)
            break
        previous = values[i]

    if n >= 3:
        candidates.add(0)
        candidates.add(1)
        candidates.add(2)

    valid = [values[i] for i in candidates if 0 <= i < n and is_arithmetic_after_removal(values, i)]
    return min(valid) if valid else -1


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
        out.append(str(removed_value(values)))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
