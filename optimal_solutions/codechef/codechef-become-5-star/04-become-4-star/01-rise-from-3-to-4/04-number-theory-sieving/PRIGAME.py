import sys
LIMIT = 1000000

def build_prime_count() -> list[int]:
    prime = bytearray(b'\x01') * (LIMIT + 1)
    prime[0] = prime[1] = 0
    p = 2
    while p * p <= LIMIT:
        if prime[p]:
            prime[p * p:LIMIT + 1:p] = b'\x00' * ((LIMIT - p * p) // p + 1)
        p += 1
    pref = [0] * (LIMIT + 1)
    count = 0
    for i in range(LIMIT + 1):
        count += prime[i]
        pref[i] = count
    return pref

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    pref = build_prime_count()
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        x, y = (data[idx], data[idx + 1])
        idx += 2
        out.append('Chef' if pref[x] <= y else 'Divyam')
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
