def get_digit_sum(n: int) -> int:
    s = 0
    n = abs(n)
    while n > 0:
        s += n % 10
        n //= 10
    return s

def solve(nums: list[int]) -> int:
    n = len(nums)
    # Create pairs of (digit_sum, original_index, value)
    # We use original_index to ensure stability
    indexed_nums = []
    for i, val in enumerate(nums):
        indexed_nums.append((get_digit_sum(val), i, val))
    
    # Sort based on digit sum, then original index
    indexed_nums.sort(key=lambda x: (x[0], x[1]))
    
    # target_pos[i] is the index where the element currently at i should go
    target_pos = [0] * n
    for new_idx, (d_sum, old_idx, val) in enumerate(indexed_nums):
        target_pos[old_idx] = new_idx
        
    # Count cycles in the permutation
    visited = [False] * n
    swaps = 0
    
    for i in range(n):
        if visited[i] or target_pos[i] == i:
            continue
            
        cycle_size = 0
        curr = i
        while not visited[curr]:
            visited[curr] = True
            curr = target_pos[curr]
            cycle_size += 1
            
        if cycle_size > 1:
            swaps += (cycle_size - 1)
            
    return swaps
