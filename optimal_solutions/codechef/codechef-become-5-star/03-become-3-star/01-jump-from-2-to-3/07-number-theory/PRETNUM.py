import math
import sys

def primes_up_to(limit: int) -> list[int]:
    sieve = bytearray(b'\x01') * (limit + 1)
    if limit >= 0:
        sieve[0:2] = b'\x00\x00'
    for value in range(2, math.isqrt(limit) + 1):
        if sieve[value]:
            start = value * value
            sieve[start:limit + 1:value] = b'\x00' * ((limit - start) // value + 1)
    return [i for i in range(2, limit + 1) if sieve[i]]
PRIMES = primes_up_to(1000000)
SMALL_PRIME_DIVISOR_COUNTS = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37}

def count_pretty_numbers(left: int, right: int) -> int:
    size = right - left + 1
    remaining = [left + i for i in range(size)]
    divisor_counts = [1] * size
    for prime in PRIMES:
        if prime * prime > right:
            break
        start = (left + prime - 1) // prime * prime
        for value in range(start, right + 1, prime):
            idx = value - left
            exponent = 0
            while remaining[idx] % prime == 0:
                remaining[idx] //= prime
                exponent += 1
            if exponent:
                divisor_counts[idx] *= exponent + 1
    answer = 0
    for idx, rem in enumerate(remaining):
        if rem > 1:
            divisor_counts[idx] *= 2
        if divisor_counts[idx] in SMALL_PRIME_DIVISOR_COUNTS:
            answer += 1
    return answer

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    t = data[0]
    idx = 1
    out: list[str] = []
    for _ in range(t):
        left, right = (data[idx], data[idx + 1])
        idx += 2
        out.append(str(count_pretty_numbers(left, right)))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
