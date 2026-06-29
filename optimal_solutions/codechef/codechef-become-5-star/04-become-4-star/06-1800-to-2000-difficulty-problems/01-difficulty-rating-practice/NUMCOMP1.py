import sys
from array import array
from math import isqrt

def build_prime_prefix(limit: int) -> array:
    is_prime = bytearray(b'\x01') * (limit + 1)
    if limit >= 0:
        is_prime[0] = 0
    if limit >= 1:
        is_prime[1] = 0
    root = isqrt(limit)
    for p in range(2, root + 1):
        if is_prime[p]:
            start = p * p
            is_prime[start:limit + 1:p] = b'\x00' * ((limit - start) // p + 1)
    pref = array('I', [0]) * (limit + 1)
    count = 0
    for i in range(limit + 1):
        count += is_prime[i]
        pref[i] = count
    if limit >= 1:
        pref[1] = 1
    return pref

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    t = data[0]
    values = data[1:1 + t]
    pref = build_prime_prefix(max(values))
    out = [str(pref[n] - pref[n // 2] + 1) for n in values]
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
