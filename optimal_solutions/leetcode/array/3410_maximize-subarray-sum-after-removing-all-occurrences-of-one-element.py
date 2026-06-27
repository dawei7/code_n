from collections import defaultdict

def solve(nums: list[int]) -> int:
    # Kadane's algorithm variant:
    # We want to find max subarray sum after removing all occurrences of x.
    # Let S be the total sum of the array.
    # If we remove x, we are essentially looking for the max subarray in the 
    # remaining sequence.
    
    n = len(nums)
    val_to_indices = defaultdict(list)
    for i, x in enumerate(nums):
        val_to_indices[x].append(i)
        
    # Global max subarray sum (Kadane's)
    def get_max_subarray(arr):
        max_so_far = 0
        current_max = 0
        for x in arr:
            current_max = max(0, current_max + x)
            max_so_far = max(max_so_far, current_max)
        return max_so_far

    # To optimize, for each unique value x, we calculate the max subarray
    # that doesn't contain x.
    # This is equivalent to finding the max subarray in segments separated by x.
    
    ans = 0
    # Case: remove nothing is not allowed, must remove one value.
    # If all numbers are negative, result is 0 (empty subarray).
    
    unique_vals = list(val_to_indices.keys())
    
    for val in unique_vals:
        indices = [-1] + val_to_indices[val] + [n]
        current_val_max = 0
        
        for i in range(len(indices) - 1):
            start = indices[i] + 1
            end = indices[i+1]
            if start < end:
                # Standard Kadane on the segment
                sub = nums[start:end]
                # Kadane
                local_max = 0
                curr = 0
                for x in sub:
                    curr = max(0, curr + x)
                    local_max = max(local_max, curr)
                current_val_max = max(current_val_max, local_max)
        
        ans = max(ans, current_val_max)
        
    return ans
