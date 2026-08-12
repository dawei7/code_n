def solve(family_size: int = 8) -> int:
    """Find the smallest prime that is part of an 8 prime value family.
    
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

    for p in range(11, limit):
        if p in prime_set:
            s = str(p)
            for digit in "012":
                if s.count(digit) == 3 and s[-1] != digit:
                    family = []
                    for r in "0123456789":
                        candidate = int(s.replace(digit, r))
                        if candidate >= 10**(len(s) - 1) and candidate in prime_set:
                            family.append(candidate)
                    if len(family) >= family_size:
                        return min(family)

    return -1
