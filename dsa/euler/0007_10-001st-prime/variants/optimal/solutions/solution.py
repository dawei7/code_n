def solve(n: int = 10001) -> int:
    """Find the nth prime number using a Sieve of Eratosthenes.
    
    Time Complexity: O(N log log N)
    Space Complexity: O(N)
    """
    limit = 120000  # Upper bound for 10001st prime
    is_prime = [True] * limit
    is_prime[0] = is_prime[1] = False
    
    count = 0
    for i in range(2, limit):
        if is_prime[i]:
            count += 1
            if count == n:
                return i
            for j in range(i * i, limit, i):
                is_prime[j] = False
    return -1
