def solve(limit: int = 2**50) -> int:
    """Find number of squarefree positive integers n < limit.
    
    Time Complexity: O(sqrt(limit) * log log(sqrt(limit)))
    Space Complexity: O(sqrt(limit))
    """
    N = limit - 1
    max_d = int(N**0.5)

    mu = bytearray([1]) * (max_d + 1)
    mu[0] = 0
    primes = []
    is_prime = bytearray([1]) * (max_d + 1)
    is_prime[0] = is_prime[1] = 0

    for i in range(2, max_d + 1):
        if is_prime[i]:
            primes.append(i)
            mu[i] = 255  # -1
        for p in primes:
            ip = i * p
            if ip > max_d:
                break
            is_prime[ip] = 0
            if i % p == 0:
                mu[ip] = 0
                break
            else:
                mu[ip] = 1 if mu[i] == 255 else 255

    count = 0
    for d in range(1, max_d + 1):
        m = mu[d]
        if m == 1:
            count += (N // (d * d))
        elif m == 255:
            count -= (N // (d * d))

    return count
