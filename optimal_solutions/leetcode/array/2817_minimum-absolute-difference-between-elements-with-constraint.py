import bisect

def solve(nums: list[int], x: int) -> int:
    if x == 0:
        return 0
    
    n = len(nums)
    sorted_elements = []
    min_diff = float('inf')
    
    # We iterate through the array. For each index i, we consider
    # elements at index j <= i - x.
    for i in range(x, n):
        # Add the element that just became valid (index i - x)
        val_to_add = nums[i - x]
        idx = bisect.bisect_left(sorted_elements, val_to_add)
        sorted_elements.insert(idx, val_to_add)
        
        # Find the closest values in the sorted list to nums[i]
        current_val = nums[i]
        pos = bisect.bisect_left(sorted_elements, current_val)
        
        # Check the element at pos (the smallest element >= current_val)
        if pos < len(sorted_elements):
            min_diff = min(min_diff, abs(sorted_elements[pos] - current_val))
            
        # Check the element at pos - 1 (the largest element < current_val)
        if pos > 0:
            min_diff = min(min_diff, abs(sorted_elements[pos - 1] - current_val))
            
        # Optimization: if we found 0, we can't do better
        if min_diff == 0:
            return 0
            
    return int(min_diff)
