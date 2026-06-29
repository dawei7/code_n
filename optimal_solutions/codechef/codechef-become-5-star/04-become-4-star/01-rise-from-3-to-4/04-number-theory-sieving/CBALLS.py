import sys
LIMIT = 10000

def primes_up_to(limit: int) -> list[int]:
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, int(limit ** 0.5) + 1):
        if is_prime[p]:
            for q in range(p * p, limit + 1, p):
                is_prime[q] = False
    return [i for i in range(2, limit + 1) if is_prime[i]]
PRIMES = primes_up_to(LIMIT)

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        arr = data[idx:idx + n]
        idx += n
        best = 10 ** 18
        for p in PRIMES:
            current = 0
            cost = 0
            for value in arr:
                if current < value:
                    current = (value + p - 1) // p * p
                cost += current - value
                if cost >= best:
                    break
            if cost < best:
                best = cost
        out.append(str(best))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
