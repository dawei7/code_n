def solve(nums: list[int], cost: list[int]) -> int:
    # Combine nums and cost, then sort by the value
    data = sorted(zip(nums, cost))
    n = len(data)
    
    # Calculate prefix sums of costs to compute total cost efficiently
    prefix_costs = [0] * (n + 1)
    for i in range(n):
        prefix_costs[i + 1] = prefix_costs[i] + data[i][1]
    
    total_cost_sum = prefix_costs[n]
    
    # The optimal target value is the weighted median
    median_weight = total_cost_sum / 2
    median_val = 0
    for i in range(n):
        if prefix_costs[i + 1] >= median_weight:
            median_val = data[i][0]
            break
            
    # Calculate total cost for the chosen median_val
    ans = 0
    for val, c in data:
        ans += abs(val - median_val) * c
        
    return ans
