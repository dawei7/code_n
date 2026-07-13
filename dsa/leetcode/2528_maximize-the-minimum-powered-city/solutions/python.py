def solve(stations: list[int], r: int, k: int) -> int:
    n = len(stations)
    
    # Initial power calculation using sliding window
    power = [0] * n
    current_sum = sum(stations[:r + 1])
    for i in range(n):
        power[i] = current_sum
        if i + r + 1 < n:
            current_sum += stations[i + r + 1]
        if i - r >= 0:
            current_sum -= stations[i - r]
            
    def check(target: int) -> bool:
        added_stations = 0
        diff = [0] * (n + 1)
        current_added = 0
        
        # We need to track the effect of added stations on the power array
        # We use a difference array to keep track of added power efficiently
        added_power = [0] * (n + 1)
        curr_added_val = 0
        
        for i in range(n):
            curr_added_val += added_power[i]
            actual_power = power[i] + curr_added_val
            
            if actual_power < target:
                needed = target - actual_power
                added_stations += needed
                if added_stations > k:
                    return False
                
                # Add stations at the rightmost possible position: i + r
                # This covers cities from i to i + 2*r
                pos = min(n - 1, i + r)
                curr_added_val += needed
                if pos + r + 1 < n:
                    added_power[pos + r + 1] -= needed
        return True

    low = min(power)
    high = min(power) + k
    ans = low
    
    while low <= high:
        mid = (low + high) // 2
        if check(mid):
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
            
    return ans
