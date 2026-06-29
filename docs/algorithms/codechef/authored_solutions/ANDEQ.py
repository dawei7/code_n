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
        target = arr[0]
        for value in arr[1:]:
            target &= value

        segments = 0
        current = (1 << 31) - 1
        for value in arr:
            current &= value
            if current == target:
                segments += 1
                current = (1 << 31) - 1
        out.append(str(n - segments))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
