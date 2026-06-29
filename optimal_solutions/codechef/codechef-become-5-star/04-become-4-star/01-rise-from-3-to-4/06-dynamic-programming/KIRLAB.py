import sys

def small_primes(limit: int=3163) -> list[int]:
    sieve = bytearray(b'\x01') * (limit + 1)
    sieve[0:2] = b'\x00\x00'
    for i in range(2, int(limit ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i:limit + 1:i] = b'\x00' * ((limit - i * i) // i + 1)
    return [i for i in range(2, limit + 1) if sieve[i]]
PRIMES = small_primes()

def factors(value: int) -> list[int]:
    result = []
    x = value
    for prime in PRIMES:
        if prime * prime > x:
            break
        if x % prime == 0:
            result.append(prime)
            while x % prime == 0:
                x //= prime
    if x > 1:
        result.append(x)
    return result

def longest_path(values: list[int]) -> int:
    best_for_factor: dict[int, int] = {}
    answer = 1
    for value in values:
        fs = factors(value)
        current = 1
        for factor in fs:
            current = max(current, best_for_factor.get(factor, 0) + 1)
        for factor in fs:
            if current > best_for_factor.get(factor, 0):
                best_for_factor[factor] = current
        if current > answer:
            answer = current
    return answer

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    t = data[0]
    idx = 1
    out: list[str] = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        values = data[idx:idx + n]
        idx += n
        out.append(str(longest_path(values)))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
