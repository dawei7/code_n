def solve() -> int:
    """Find the largest palindrome product of two 3-digit numbers.
    
    Time Complexity: O(D^2)
    Space Complexity: O(1)
    """
    max_pal = 0
    for i in range(999, 99, -1):
        if i * 999 <= max_pal:
            break
        for j in range(i, 99, -1):
            prod = i * j
            if prod <= max_pal:
                break
            s = str(prod)
            if s == s[::-1]:
                max_pal = prod
    return max_pal
