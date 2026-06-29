import sys

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    t = data[0]
    nums = data[1:1 + t]
    limit = max(nums, default=1)
    prime = bytearray(b'\x01') * (limit + 1)
    if limit >= 0:
        prime[0] = 0
    if limit >= 1:
        prime[1] = 0
    p = 2
    while p * p <= limit:
        if prime[p]:
            prime[p * p:limit + 1:p] = b'\x00' * ((limit - p * p) // p + 1)
        p += 1
    print('\n'.join(('yes' if prime[n] else 'no' for n in nums)))


if __name__ == "__main__":
    solve()
