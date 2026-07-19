def solve(banned: list[int], n: int, maxSum: int) -> int:
    banned_set = set(banned)
    current_sum = 0
    count = 0
    
    for i in range(1, n + 1):
        if i in banned_set:
            continue
        
        if current_sum + i <= maxSum:
            current_sum += i
            count += 1
        else:
            # Since we are iterating in increasing order, 
            # if the current number exceeds the remaining sum, 
            # no further numbers will fit.
            break
            
    return count
