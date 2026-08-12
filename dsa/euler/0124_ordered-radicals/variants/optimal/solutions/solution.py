def solve(limit: int = 100000, target_k: int = 10000) -> int:
    """Find E(target_k) where n in [1, limit] is sorted by (rad(n), n).
    
    Time Complexity: O(limit * log limit)
    Space Complexity: O(limit)
    """
    rad = [1] * (limit + 1)
    for i in range(2, limit + 1):
        if rad[i] == 1:  # i is prime
            for j in range(i, limit + 1, i):
                rad[j] *= i

    elements = [(rad[n], n) for n in range(1, limit + 1)]
    elements.sort()

    return elements[target_k - 1][1]
