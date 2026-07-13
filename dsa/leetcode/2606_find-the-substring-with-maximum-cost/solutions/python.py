def solve(s: str, chars: str, vals: list[int]) -> int:
    # Initialize cost map with default 1-based alphabetical values
    cost_map = {chr(ord('a') + i): i + 1 for i in range(26)}
    
    # Override with custom costs
    for char, val in zip(chars, vals):
        cost_map[char] = val
        
    max_cost = 0
    current_running_sum = 0
    
    # Apply Kadane's Algorithm
    for char in s:
        current_running_sum += cost_map[char]
        
        # If the current subarray sum is better than the global max, update it
        if current_running_sum > max_cost:
            max_cost = current_running_sum
            
        # If the running sum drops below 0, reset it (start a new potential substring)
        if current_running_sum < 0:
            current_running_sum = 0
            
    return max_cost
