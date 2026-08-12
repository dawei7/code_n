import math


def solve(target: int = 1000000) -> int:
    """Find the target-th lexicographic permutation of digits 0-9 using factoradix.
    
    Time Complexity: O(N^2)
    Space Complexity: O(N)
    """
    digits = list(range(10))
    target -= 1  # 0-indexed target rank
    result = []

    for i in range(9, -1, -1):
        fact = math.factorial(i)
        idx = target // fact
        target %= fact
        result.append(str(digits.pop(idx)))

    return int("".join(result))
