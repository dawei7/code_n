def solve(count_needed: int = 11) -> int:
    """Find the sum of the eleven truncatable primes.
    
    Time Complexity: O(N log log N)
    Space Complexity: O(N)
    """
    limit = 1000000
    is_prime = [True] * limit
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit, i):
                is_prime[j] = False

    prime_set = {i for i in range(limit) if is_prime[i]}

    truncatable = []
    for p in range(11, limit):
        if p in prime_set:
            s = str(p)
            # Left-to-right truncations
            if not all(int(s[i:]) in prime_set for i in range(len(s))):
                continue
            # Right-to-left truncations
            if not all(int(s[:i]) in prime_set for i in range(1, len(s) + 1)):
                continue

            truncatable.append(p)
            if len(truncatable) == count_needed:
                break

    return sum(truncatable)
