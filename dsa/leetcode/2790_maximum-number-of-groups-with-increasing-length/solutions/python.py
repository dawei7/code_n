def solve(usageLimits: list[int]) -> int:
    """
    Calculates the maximum number of groups with strictly increasing lengths.
    
    The strategy is to sort the limits and greedily build groups.
    If we want to form 'k' groups, the smallest possible sizes are 1, 2, ..., k.
    The total number of items required is k*(k+1)/2.
    However, because we have constraints on individual item counts, we sort
    the limits and keep track of how many items we have 'accumulated' to 
    satisfy the increasing group size requirements.
    """
    usageLimits.sort()
    
    groups = 0
    total_items_accumulated = 0
    
    for limit in usageLimits:
        # If the current item's limit allows us to increase the size of the 
        # next group (which would be groups + 1), we increment the group count.
        # We track total_items_accumulated to ensure we have enough items 
        # to satisfy the requirement of having strictly increasing sizes.
        total_items_accumulated += limit
        if total_items_accumulated >= (groups + 1):
            groups += 1
            total_items_accumulated -= groups
            
    return groups
