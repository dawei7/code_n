def solve(limit: int = 100000000) -> int:
    """Find sum of all numbers < limit that are palindromic and expressible as sum of consecutive squares.
    
    Time Complexity: O(K^2)
    Space Complexity: O(P)
    """
    max_k = int(limit**0.5)
    palindromic_sums = set()

    for i in range(1, max_k):
        sq_sum = i * i
        for j in range(i + 1, max_k + 1):
            sq_sum += j * j
            if sq_sum >= limit:
                break

            s = str(sq_sum)
            if s == s[::-1]:
                palindromic_sums.add(sq_sum)

    return sum(palindromic_sums)
