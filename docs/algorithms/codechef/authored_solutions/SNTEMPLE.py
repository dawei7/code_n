import sys


def minimum_removed(heights: list[int]) -> int:
    n = len(heights)
    left = [0] * n
    right = [0] * n

    for i, height in enumerate(heights):
        left[i] = min(height, (left[i - 1] + 1) if i else 1)
    for i in range(n - 1, -1, -1):
        right[i] = min(heights[i], (right[i + 1] + 1) if i + 1 < n else 1)

    best_peak = max(min(left[i], right[i]) for i in range(n))
    return sum(heights) - best_peak * best_peak


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
        heights = data[idx : idx + n]
        idx += n
        out.append(str(minimum_removed(heights)))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
