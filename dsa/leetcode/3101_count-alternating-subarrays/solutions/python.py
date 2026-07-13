from typing import List

def solve(nums: List[int]) -> int:
    """
    Calculates the number of alternating subarrays in O(n) time and O(1) space.
    """
    if not nums:
        return 0
    
    total_count = 0
    current_chain_length = 0
    
    for i in range(len(nums)):
        # If not the first element and current element differs from previous,
        # extend the current alternating chain.
        if i > 0 and nums[i] != nums[i - 1]:
            current_chain_length += 1
        else:
            # Otherwise, start a new chain of length 1.
            current_chain_length = 1
        
        # The number of alternating subarrays ending at index i is equal
        # to the length of the alternating chain ending at i.
        total_count += current_chain_length
        
    return total_count
