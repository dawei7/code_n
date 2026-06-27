from typing import List

def solve(nums: List[int]) -> int:
    """
    Calculates the number of subarrays where the first and last elements 
    are the maximum of that subarray using a monotonic stack.
    """
    # stack stores tuples of (value, count_of_this_value_in_current_sequence)
    stack = []
    total_subarrays = 0
    
    for x in nums:
        # Maintain a monotonic decreasing stack.
        # If we see a value larger than the top, the previous smaller values
        # can no longer be the maximum for any subarray extending to the current index.
        while stack and stack[-1][0] < x:
            stack.pop()
            
        if stack and stack[-1][0] == x:
            # If the current value is the same as the top, it extends all 
            # previous subarrays that had this value as the maximum.
            count = stack[-1][1] + 1
            stack.pop()
            stack.append((x, count))
            total_subarrays += count
        else:
            # If the current value is smaller than the top (or stack is empty),
            # it starts a new potential maximum sequence of length 1.
            stack.append((x, 1))
            total_subarrays += 1
            
    return total_subarrays
