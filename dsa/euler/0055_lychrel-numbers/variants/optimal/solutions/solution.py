def is_lychrel(n: int) -> bool:
    curr = n
    for _ in range(49):
        curr += int(str(curr)[::-1])
        s = str(curr)
        if s == s[::-1]:
            return False
    return True


def solve(limit: int = 10000) -> int:
    """Find number of Lychrel numbers below limit.
    
    Time Complexity: O(limit * 50)
    Space Complexity: O(1)
    """
    return sum(1 for i in range(1, limit) if is_lychrel(i))
