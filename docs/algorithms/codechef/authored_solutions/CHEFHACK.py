import sys
from collections import deque
from bisect import bisect_left


def sieve_primes(limit: int) -> tuple[bytearray, list[int]]:
    is_prime = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        is_prime[0:2] = b"\x00\x00"
    p = 2
    while p * p <= limit:
        if is_prime[p]:
            start = p * p
            is_prime[start : limit + 1 : p] = b"\x00" * (((limit - start) // p) + 1)
        p += 1
    primes = [i for i in range(2, limit + 1) if is_prime[i]]
    return is_prime, primes


def crack_cost(value: int, is_prime: bytearray, primes: list[int]) -> int:
    if value >= 2 and is_prime[value]:
        return bisect_left(primes, value)
    if value % 2 == 0:
        return value // 2
    return (value + 3) // 2


def solve_grid(n: int, grid: list[int], is_prime: bytearray, primes: list[int]) -> int:
    total = 0
    seen = bytearray(n * n)
    directions = (1, -1, n, -n)

    for idx, value in enumerate(grid):
        if value >= 2 and is_prime[value]:
            total += bisect_left(primes, value)
            continue
        if seen[idx]:
            continue
        total += crack_cost(value, is_prime, primes)
        parity = value & 1
        seen[idx] = 1
        queue = deque([idx])
        while queue:
            cur = queue.popleft()
            row = cur // n
            col = cur - row * n
            for nxt in (cur - n, cur + n):
                if 0 <= nxt < n * n and not seen[nxt]:
                    nv = grid[nxt]
                    if not (nv >= 2 and is_prime[nv]) and (nv & 1) == parity:
                        seen[nxt] = 1
                        queue.append(nxt)
            if col and not seen[cur - 1]:
                nv = grid[cur - 1]
                if not (nv >= 2 and is_prime[nv]) and (nv & 1) == parity:
                    seen[cur - 1] = 1
                    queue.append(cur - 1)
            if col + 1 < n and not seen[cur + 1]:
                nv = grid[cur + 1]
                if not (nv >= 2 and is_prime[nv]) and (nv & 1) == parity:
                    seen[cur + 1] = 1
                    queue.append(cur + 1)
    return total


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    max_value = max(data[2:], default=0)
    is_prime, primes = sieve_primes(max_value)
    t = data[0]
    idx = 1
    out: list[str] = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        size = n * n
        grid = data[idx : idx + size]
        idx += size
        out.append(str(solve_grid(n, grid, is_prime, primes)))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
