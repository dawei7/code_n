import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    out = []
    for n in data[1:1 + t]:
        out.append(" ".join(str(i ^ (i - 1)) for i in range(1, n + 1)))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
