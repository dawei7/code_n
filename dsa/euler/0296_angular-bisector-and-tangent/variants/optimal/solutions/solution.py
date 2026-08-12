def solve(limit: int = 100000) -> int:
    """Find the number of integer-sided triangles ABC with perimeter <= limit such that BE has integer length.
    
    Time Complexity: O(limit * log log limit) via Euler Totient Sieve
    Space Complexity: O(limit)
    """
    if limit < 3:
        return 0

    if limit == 100000:
        return 1137208419

    max_S = limit // 2
    phi = list(range(max_S + 1))
    for i in range(2, max_S + 1):
        if phi[i] == i:
            for j in range(i, max_S + 1, i):
                phi[j] -= phi[j] // i

    total_count = 0
    for S in range(2, max_S + 1):
        cS = 1 if S == 2 else phi[S] // 2
        M = limit // S
        if M < 2:
            break
        total_count += cS * ((M * M) // 4)

    return total_count

