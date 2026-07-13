def solve(ranges: list[list[int]]) -> int:
    MOD = 10**9 + 7
    
    # Sort ranges by start time
    ranges.sort()
    
    # Count the number of disjoint components
    components = 0
    if not ranges:
        return 0
    
    # Initialize with the first range
    current_end = -1
    
    for start, end in ranges:
        # If the current range starts after the previous merged end,
        # it's a new disjoint component.
        if start > current_end:
            components += 1
            current_end = end
        else:
            # Otherwise, merge the range by extending the current end
            current_end = max(current_end, end)
            
    # The result is 2^components % (10^9 + 7)
    return pow(2, components, MOD)
