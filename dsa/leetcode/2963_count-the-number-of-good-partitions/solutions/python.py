def solve(nums: list[int]) -> int:
    MOD = 10**9 + 7
    
    # Map each number to its last occurrence index
    last_occurrence = {val: i for i, val in enumerate(nums)}
    
    num_blocks = 0
    max_reach = 0
    
    # Iterate through the array to find independent segments
    for i, val in enumerate(nums):
        # Update the furthest index we need to reach to satisfy the current partition
        max_reach = max(max_reach, last_occurrence[val])
        
        # If the current index is the end of a block
        if i == max_reach:
            num_blocks += 1
            
    # If there are k blocks, there are k-1 places to cut, 
    # resulting in 2^(k-1) possible ways to partition.
    return pow(2, num_blocks - 1, MOD)
