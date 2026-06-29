import sys


MOD = 1_000_000_007


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    out = []
    for n in data[1:1 + t]:
        if n == 1:
            ans = 1
        elif n == 2:
            ans = 2
        elif n & (n - 1) == 0:
            ans = 2 * n - 1
        else:
            ans = 1 << n.bit_length()
        out.append(str(ans % MOD))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
