import sys

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, m = (data[0], data[1])
    limit = n + m
    if limit < 2:
        print(0)
        return
    prime = bytearray(b'\x01') * (limit + 1)
    prime[0:2] = b'\x00\x00'
    p = 2
    while p * p <= limit:
        if prime[p]:
            prime[p * p:limit + 1:p] = b'\x00' * ((limit - p * p) // p + 1)
        p += 1
    print(sum(prime))


if __name__ == "__main__":
    solve()
