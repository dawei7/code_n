import math
from collections import defaultdict

def solve(nums: list[int]) -> int:
    """
    Calculates the maximum element-sum of a complete subset of indices.
    Indices i and j form a complete subset if i * j is a perfect square.
    This is equivalent to saying i and j have the same square-free part.
    """
    n = len(nums)
    # Map to store the sum of elements for each square-free part
    groups = defaultdict(int)
    
    def get_square_free(k: int) -> int:
        """Returns the square-free part of k."""
        res = 1
        d = 2
        temp = k
        while d * d <= temp:
            count = 0
            while temp % d == 0:
                count += 1
                temp //= d
            if count % 2 == 1:
                res *= d
            d += 1
        if temp > 1:
            res *= temp
        return res

    # Iterate through 1-based indices
    for i in range(1, n + 1):
        sf = get_square_free(i)
        groups[sf] += nums[i - 1]
        
    return max(groups.values())
