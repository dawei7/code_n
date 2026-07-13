from collections import defaultdict

def solve(nums: list[int], space: int) -> int:
    # Map remainder -> count of numbers with that remainder
    remainder_counts = defaultdict(int)
    # Map remainder -> smallest number found with that remainder
    min_val_for_remainder = {}
    
    for num in nums:
        rem = num % space
        remainder_counts[rem] += 1
        
        if rem not in min_val_for_remainder or num < min_val_for_remainder[rem]:
            min_val_for_remainder[rem] = num
            
    max_targets = -1
    best_start = float('inf')
    
    for rem in remainder_counts:
        count = remainder_counts[rem]
        start_val = min_val_for_remainder[rem]
        
        if count > max_targets:
            max_targets = count
            best_start = start_val
        elif count == max_targets:
            if start_val < best_start:
                best_start = start_val
                
    return best_start
