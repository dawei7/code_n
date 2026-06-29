import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        x, m = data[idx:idx + 2]
        idx += 2
        need = (x - 1).bit_length()
        out.append(str(max(0, m - need)))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
