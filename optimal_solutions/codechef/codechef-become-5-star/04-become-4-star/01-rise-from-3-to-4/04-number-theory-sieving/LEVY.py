import sys
LIMIT = 10000

def sieve(limit: int) -> list[bool]:
    prime = [True] * (limit + 1)
    prime[0] = prime[1] = False
    for p in range(2, int(limit ** 0.5) + 1):
        if prime[p]:
            step = p
            start = p * p
            prime[start:limit + 1:step] = [False] * ((limit - start) // step + 1)
    return prime

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    prime = sieve(LIMIT)
    primes = [i for i in range(2, LIMIT + 1) if prime[i]]
    ans = [0] * (LIMIT + 1)
    for n in range(1, LIMIT + 1):
        count = 0
        for q in primes:
            value = n - 2 * q
            if value < 2:
                break
            if prime[value]:
                count += 1
        ans[n] = count
    out = [str(ans[n]) for n in data[1:1 + data[0]]]
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
