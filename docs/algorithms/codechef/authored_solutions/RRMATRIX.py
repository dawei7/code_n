from math import gcd
import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n = data[idx]
        m = data[idx + 1]
        idx += 2
        if n == 1 and m == 1:
            out.append("1")
        else:
            out.append(str(gcd(n - 1, m - 1) + 1))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
