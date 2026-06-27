def solve(n: int) -> list[list[int]]:
    if n < 4:
        return []

    # Sieve of Eratosthenes to find all primes up to n
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    for p in range(2, int(n**0.5) + 1):
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
    
    result = []
    # Iterate to find pairs (x, y) such that x + y = n and x <= y
    for x in range(2, n // 2 + 1):
        y = n - x
        if is_prime[x] and is_prime[y]:
            result.append([x, y])
            
    return result
