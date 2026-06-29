import sys


def omega_prefix(limit):
    omega = [0] * (limit + 1)
    for prime in range(2, limit + 1):
        if omega[prime] == 0:
            for multiple in range(prime, limit + 1, prime):
                omega[multiple] += 1
    pref = [0] * (limit + 1)
    for i in range(1, limit + 1):
        pref[i] = pref[i - 1] + omega[i]
    return pref


def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pairs = [(data[i], data[i + 1]) for i in range(1, 2 * t, 2)]
    pref = omega_prefix(max(m for _, m in pairs))
    out = [str(pref[m - 1] - pref[n - 1]) for n, m in pairs]
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
