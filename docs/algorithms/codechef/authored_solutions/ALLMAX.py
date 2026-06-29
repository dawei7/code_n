import sys


MOD = 1000000007


def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        values = data[idx:idx + n]
        idx += n
        values.sort()

        power = 1
        answer = 0
        for value in values:
            answer = (answer + value * power) % MOD
            power = (power * 2) % MOD
        out.append(str(answer))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
