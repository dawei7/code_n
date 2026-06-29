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
        x = 0
        for value in arr:
            x |= value
        answer = 0
        for value in arr:
            answer |= value ^ x
        out.append(f"{x} {answer}")
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
