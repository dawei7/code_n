from typing import List
import bisect

def solve(n: int, offers: List[List[int]]) -> int:
    # Group offers by their end house for efficient lookup
    # end_map[end_house] = list of (start, gold)
    end_map = {}
    for start, end, gold in offers:
        if end not in end_map:
            end_map[end] = []
        end_map[end].append((start, gold))
    
    # dp[i] will store the max profit using houses up to index i-1
    # dp[0] = 0 (no houses)
    dp = [0] * (n + 1)
    
    # Iterate through each house index
    for i in range(1, n + 1):
        # Option 1: Don't include any offer ending at house i-1
        dp[i] = dp[i-1]
        
        # Option 2: Consider all offers that end exactly at house i-1
        if (i - 1) in end_map:
            for start, gold in end_map[i - 1]:
                # If we take this offer, we add its gold to the max profit
                # achievable up to the house before the offer started
                current_profit = dp[start] + gold
                if current_profit > dp[i]:
                    dp[i] = current_profit
                    
    return dp[n]
