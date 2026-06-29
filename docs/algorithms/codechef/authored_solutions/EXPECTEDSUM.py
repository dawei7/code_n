import sys


MOD = 998244353


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        ones, zeros = data[idx:idx + 2]
        idx += 2
        total = ones + zeros
        chef_turns = (total + 1) // 2
        ans = ones % MOD * chef_turns % MOD * pow(total, MOD - 2, MOD) % MOD
        out.append(str(ans))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
