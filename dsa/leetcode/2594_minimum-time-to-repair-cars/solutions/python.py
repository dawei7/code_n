import math

def solve(ranks: list[int], cars: int) -> int:
    """
    Calculates the minimum time to repair all cars using binary search.
    """
    # The fastest mechanic is the one with the minimum rank.
    # In the worst case, the fastest mechanic repairs all cars.
    min_rank = min(ranks)
    
    # Binary search range:
    # Lower bound: 1
    # Upper bound: min_rank * cars^2 (time taken if fastest mechanic does all)
    low = 1
    high = min_rank * (cars ** 2)
    ans = high
    
    while low <= high:
        mid = (low + high) // 2
        
        # Calculate total cars repaired by all mechanics in 'mid' time
        # A mechanic with rank r repairs n cars in r * n^2 time.
        # r * n^2 <= mid  =>  n^2 <= mid / r  =>  n <= sqrt(mid / r)
        total_repaired = 0
        for r in ranks:
            total_repaired += int(math.isqrt(mid // r))
            
        if total_repaired >= cars:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
            
    return ans
