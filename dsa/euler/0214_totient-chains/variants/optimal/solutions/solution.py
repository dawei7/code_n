def solve(limit: int = 40000000, target_len: int = 25) -> int:
    """Find sum of all primes < limit that generate a totient chain of length `target_len`.
    
    Time Complexity: O(limit * log(log(limit)))
    Space Complexity: O(limit)
    """
    LIMIT = limit
    phi = list(range(LIMIT))
    for i in range(2, LIMIT):
        if phi[i] == i:
            for j in range(i, LIMIT, i):
                phi[j] -= phi[j] // i

    L = bytearray(LIMIT)
    L[1] = 1
    for i in range(2, LIMIT):
        L[i] = 1 + L[phi[i]]

    ans = 0
    for i in range(2, LIMIT):
        if phi[i] == i - 1:
            if L[i] == target_len:
                ans += i

    return ans
