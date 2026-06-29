from collections import Counter
import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []

    for _ in range(t):
        n = data[idx]
        idx += 1
        arr = data[idx:idx + n]
        idx += n

        freq = Counter(arr)
        shift = max(freq.values())
        ordered = sorted((value, i) for i, value in enumerate(arr))
        values = [value for value, _ in ordered]
        ans = [0] * n
        for i, (_, original_index) in enumerate(ordered):
            ans[original_index] = values[(i + shift) % n]

        distance = sum(a != b for a, b in zip(arr, ans))
        out.append(str(distance))
        out.append(" ".join(map(str, ans)))

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
