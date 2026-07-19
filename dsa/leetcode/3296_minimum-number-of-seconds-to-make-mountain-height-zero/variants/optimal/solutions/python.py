import math

def solve(mountainHeight: int, workerTimes: list[int]) -> int:
    """
    Calculates the minimum time to reduce mountainHeight to zero using binary search.
    For a worker with coefficient w, the time to reduce k units is w * (k * (k + 1) / 2).
    We solve for k: k^2 + k - 2 * (time / w) <= 0.
    Using quadratic formula: k <= (-1 + sqrt(1 + 8 * (time / w))) / 2.
    """
    
    def get_max_units(time: int, w: int) -> int:
        # Solve w * k * (k + 1) / 2 <= time
        # k^2 + k - 2 * time / w <= 0
        # Positive root of k^2 + k - C = 0 is (-1 + sqrt(1 + 4C)) / 2
        # Here C = 2 * time / w
        val = 2 * time // w
        k = int((math.isqrt(1 + 4 * val) - 1) // 2)
        return k

    def can_reduce(time: int) -> bool:
        total_units = 0
        for w in workerTimes:
            total_units += get_max_units(time, w)
            if total_units >= mountainHeight:
                return True
        return total_units >= mountainHeight

    # Binary search range: 
    # Lower bound 0, Upper bound: worst case is one worker with max time 
    # reducing all height. Max height 10^5, min worker time 1.
    # Time approx 10^5 * 10^5 * 1 / 2 = 5 * 10^9. 
    # Using 10^18 to be safe for constraints.
    low = 0
    high = 10**18 
    ans = high
    
    while low <= high:
        mid = (low + high) // 2
        if can_reduce(mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
            
    return ans
