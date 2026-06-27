import math

def solve(n: int, k: int) -> list[int]:
    """
    Finds the k-th lexicographical permutation of [1, ..., n]
    using the factorial number system.
    """
    # Adjust k to be 0-indexed for easier calculation
    k -= 1
    
    # Precompute factorials up to (n-1)!
    # We only need up to (n-1)! because the first digit choice
    # determines the block of (n-1)! permutations.
    factorials = [1] * n
    for i in range(2, n):
        factorials[i] = factorials[i - 1] * i
        
    numbers = list(range(1, n + 1))
    result = []
    
    # Iterate from n-1 down to 0
    for i in range(n - 1, -1, -1):
        # Determine the index of the current number
        idx = k // factorials[i]
        result.append(numbers.pop(idx))
        
        # Update k to the remainder
        k %= factorials[i]
        
    return result
