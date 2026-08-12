def solve() -> int:
    """Find how many n-digit positive integers exist which are also an n-th power.
    
    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    count = 0
    for a in range(1, 10):
        n = 1
        while len(str(a**n)) == n:
            count += 1
            n += 1
    return count
