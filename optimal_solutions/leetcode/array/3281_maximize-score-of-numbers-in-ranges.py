def solve(start: list[int], d: int) -> int:
    start.sort()
    n = len(start)
    
    def can_achieve(min_diff: int) -> bool:
        last_val = start[0]
        for i in range(1, n):
            # We need to pick a value x such that:
            # 1. start[i] <= x <= start[i] + d
            # 2. x >= last_val + min_diff
            target = last_val + min_diff
            
            # The smallest valid x is max(start[i], target)
            current_val = max(start[i], target)
            
            if current_val > start[i] + d:
                return False
            last_val = current_val
        return True

    low = 0
    high = start[-1] + d - start[0]
    ans = 0
    
    while low <= high:
        mid = (low + high) // 2
        if mid == 0:
            low = mid + 1
            continue
            
        if can_achieve(mid):
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
            
    return ans
