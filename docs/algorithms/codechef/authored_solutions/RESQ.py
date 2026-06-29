import math
import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    out = []
    for n in data[1:1 + t]:
        root = math.isqrt(n)
        while n % root:
            root -= 1
        out.append(str(n // root - root))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
