def solve(pizzas: list[int]) -> int:
    n = len(pizzas)
    days = n // 4
    pizzas.sort()
    
    # We need to pick 'days' pizzas to eat.
    # To maximize the sum, we want to pick the largest possible values.
    # We have 'days' groups. 
    # Let 'd1' be the number of groups where we pick the largest available,
    # and 'd2' be the number of groups where we pick the second largest available.
    # Actually, a simpler greedy strategy:
    # We have 'days' groups. We need to pick 'days' pizzas.
    # We use the smallest (n // 2) pizzas to fill the 3-pizza slots for all groups.
    # We use the largest (n // 2) pizzas to pick from.
    # Specifically, we take the largest 'days' pizzas, but we must account for the 
    # fact that each group needs 3 smaller pizzas.
    
    # Correct Greedy:
    # Sort pizzas.
    # We have 'days' groups.
    # We take the largest 'days' pizzas.
    # For the first 'days // 2' groups, we use the largest available.
    # For the remaining, we skip one to satisfy the "3 filler" constraint.
    
    pizzas.sort()
    
    # Number of groups where we can pick the absolute largest
    num_large = (days + 1) // 2
    # Number of groups where we pick the next largest
    num_small = days // 2
    
    total_weight = 0
    
    # Pick from the very end for the largest groups
    idx = n - 1
    for _ in range(num_large):
        total_weight += pizzas[idx]
        idx -= 1
        
    # For the remaining groups, we must skip one pizza (the filler)
    # to satisfy the 3-pizza requirement for the groups.
    for _ in range(num_small):
        idx -= 2
        total_weight += pizzas[idx]
        idx -= 1
        
    return total_weight
