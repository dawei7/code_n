def solve(nums: list[int], target: list[int]) -> int:
    """
    Calculates the minimum operations to transform nums to target.
    We define diff[i] = target[i] - nums[i].
    We want to reach an array of all zeros.
    This is equivalent to the classic problem of making an array zero
    using range increments/decrements.
    """
    n = len(nums)
    diff = [target[i] - nums[i] for i in range(n)]
    
    total_ops = 0
    inc = 0  # Current accumulated positive operations
    dec = 0  # Current accumulated negative operations
    
    for d in diff:
        if d > 0:
            if d > inc:
                total_ops += (d - inc)
            inc = d
            dec = 0
        elif d < 0:
            if d < dec:
                total_ops += (dec - d)
            dec = d
            inc = 0
        else:
            inc = 0
            dec = 0
            
    return total_ops
