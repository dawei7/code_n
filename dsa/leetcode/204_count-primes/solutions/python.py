def solve(n: int) -> int:
    if n <= 2:
        return 0
    prime = bytearray(b"\x01") * n
    prime[0:2] = b"\x00\x00"
    limit = int((n - 1) ** 0.5)
    for candidate in range(2, limit + 1):
        if prime[candidate]:
            start = candidate * candidate
            prime[start:n:candidate] = b"\x00" * (((n - 1 - start) // candidate) + 1)
    return sum(prime)
