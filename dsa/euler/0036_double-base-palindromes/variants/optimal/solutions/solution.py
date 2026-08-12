def solve(limit: int = 1000000) -> int:
    """Find sum of all numbers < limit palindromic in base 10 and base 2.
    
    Time Complexity: O(limit)
    Space Complexity: O(1)
    """
    total = 0
    # Even binary numbers end in 0, so binary palindrome cannot start/end in 0 -> must be odd!
    for i in range(1, limit, 2):
        s10 = str(i)
        if s10 == s10[::-1]:
            s2 = bin(i)[2:]
            if s2 == s2[::-1]:
                total += i
    return total
