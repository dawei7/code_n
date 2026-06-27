from bisect import bisect_right

def solve(coins: list[list[int]], k: int) -> int:
    coins.sort()
    n = len(coins)
    starts = [c[0] for c in coins]
    ends = [c[1] for c in coins]
    
    prefix_coins = [0] * (n + 1)
    for i in range(n):
        prefix_coins[i + 1] = prefix_coins[i] + coins[i][2]
        
    def get_max_coins(k_val):
        ans = 0
        for i in range(n):
            # Case 1: Window ends at coins[i][1]
            # Window range: [coins[i][1] - k_val + 1, coins[i][1]]
            end_pos = coins[i][1]
            start_pos = end_pos - k_val + 1
            
            idx = bisect_right(ends, end_pos - 1)
            # Bags fully inside: [idx, i]
            current = prefix_coins[i + 1] - prefix_coins[idx]
            
            # Partial overlap at left
            if idx > 0 and ends[idx - 1] >= start_pos:
                overlap = min(end_pos, ends[idx - 1]) - max(start_pos, coins[idx - 1][0]) + 1
                current += (overlap * coins[idx - 1][2]) // (ends[idx - 1] - coins[idx - 1][0] + 1)
            ans = max(ans, current)
            
            # Case 2: Window starts at coins[i][0]
            # Window range: [coins[i][0], coins[i][0] + k_val - 1]
            start_pos = coins[i][0]
            end_pos = start_pos + k_val - 1
            
            idx_start = i
            idx_end = bisect_right(starts, end_pos) - 1
            
            current = prefix_coins[idx_end + 1] - prefix_coins[idx_start]
            
            # Partial overlap at right
            if idx_end + 1 < n and starts[idx_end + 1] <= end_pos:
                overlap = min(end_pos, ends[idx_end + 1]) - max(start_pos, starts[idx_end + 1]) + 1
                current += (overlap * coins[idx_end + 1][2]) // (ends[idx_end + 1] - starts[idx_end + 1] + 1)
            ans = max(ans, current)
            
        return ans

    return get_max_coins(k)
