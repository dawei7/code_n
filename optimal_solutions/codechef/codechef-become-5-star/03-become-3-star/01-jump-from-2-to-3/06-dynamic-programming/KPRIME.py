import sys
LIMIT = 100000

def build_prefix() -> list[list[int]]:
    factors = [0] * (LIMIT + 1)
    for p in range(2, LIMIT + 1):
        if factors[p] == 0:
            for multiple in range(p, LIMIT + 1, p):
                factors[multiple] += 1
    pref = [[0] * (LIMIT + 1) for _ in range(6)]
    for i in range(1, LIMIT + 1):
        for k in range(1, 6):
            pref[k][i] = pref[k][i - 1]
        if factors[i] <= 5:
            pref[factors[i]][i] += 1
    return pref

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    pref = build_prefix()
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        a, b, k = (data[idx], data[idx + 1], data[idx + 2])
        idx += 3
        out.append(str(pref[k][b] - pref[k][a - 1]))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
