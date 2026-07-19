def solve(colors: list[int], k: int) -> int:
    n = len(colors)
    if k > n:
        return 0
    
    # The circular nature means we can treat the array as if it 
    # wraps around. We only need to check up to n + k - 2 
    # to cover all possible windows of length k.
    count = 0
    alternating_len = 1
    
    # We iterate through the array, effectively wrapping around
    # by using the modulo operator.
    for i in range(1, n + k - 1):
        # Check if current element alternates with the previous one
        if colors[i % n] != colors[(i - 1) % n]:
            alternating_len += 1
        else:
            alternating_len = 1
            
        # If the current alternating sequence is at least k,
        # it means we have found a valid group of length k.
        if alternating_len >= k:
            count += 1
            
    return count
