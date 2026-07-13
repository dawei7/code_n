from collections import Counter
import bisect

def solve(power: list[int]) -> int:
    # Count occurrences of each spell power
    counts = Counter(power)
    # Sort unique power levels to process them in order
    unique_powers = sorted(counts.keys())
    n = len(unique_powers)
    
    # dp[i] will store the maximum damage using a subset of the first i unique powers
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        current_power = unique_powers[i - 1]
        current_damage = current_power * counts[current_power]
        
        # Find the index of the largest power level that is < current_power - 2
        # This is the last index we can safely include without violating constraints
        idx = bisect.bisect_right(unique_powers, current_power - 3)
        
        # Option 1: Include current power level
        # We add current_damage to the max damage found up to the valid index
        include = current_damage + dp[idx]
        
        # Option 2: Exclude current power level
        # We take the max damage found up to the previous power level
        exclude = dp[i - 1]
        
        dp[i] = max(include, exclude)
        
    return dp[n]
