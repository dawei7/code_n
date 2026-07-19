from collections import Counter

def solve(basket1: list[int], basket2: list[int]) -> int:
    n = len(basket1)
    count1 = Counter(basket1)
    count2 = Counter(basket2)
    
    # Total count of each fruit across both baskets
    total_counts = Counter(basket1) + Counter(basket2)
    
    # If any fruit has an odd total count, we cannot split them equally
    for fruit in total_counts:
        if total_counts[fruit] % 2 != 0:
            return -1
            
    # Identify the global minimum fruit value to use as a "cheaper" swap option
    min_val = min(min(basket1), min(basket2))
    
    # Find excess fruits in each basket
    excess1 = []
    excess2 = []
    
    for fruit in total_counts:
        target = total_counts[fruit] // 2
        if count1[fruit] > target:
            excess1.extend([fruit] * (count1[fruit] - target))
        elif count2[fruit] > target:
            excess2.extend([fruit] * (count2[fruit] - target))
            
    # Sort excess fruits to pair the smallest ones together
    excess1.sort()
    excess2.sort(reverse=True)
    
    # The number of excess fruits must be equal in both baskets
    # We pair them up. For each pair, we can either swap them directly
    # or use the global minimum to swap them if it's cheaper.
    total_cost = 0
    for i in range(len(excess1)):
        total_cost += min(min(excess1[i], excess2[i]), 2 * min_val)
        
    return total_cost
