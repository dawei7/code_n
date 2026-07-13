def solve(nums: list[int], divisors: list[int]) -> int:
    max_score = -1
    best_divisor = float('inf')
    
    # Sort divisors to handle the tie-breaking condition (smallest divisor)
    # naturally if we iterate in order, but we must check all to find the max.
    for d in divisors:
        current_score = 0
        for n in nums:
            if n % d == 0:
                current_score += 1
        
        if current_score > max_score:
            max_score = current_score
            best_divisor = d
        elif current_score == max_score:
            if d < best_divisor:
                best_divisor = d
                
    return int(best_divisor)
