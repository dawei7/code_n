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
        total = sum(arr)
        arr.sort()
        keep = 0
        for i, value in enumerate(arr, 1):
            if i * value <= total:
                keep = i
        out.append(str(n - keep))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
