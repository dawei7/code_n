def solve(nums: list[int], k: int) -> int:
    unique_elements = set(nums)
    
    # If any element is smaller than k, it's impossible to reach k
    # because we can only decrease values.
    for val in unique_elements:
        if val < k:
            return -1
            
    # If k is not in the array, we need one extra operation to 
    # transform the smallest value (which is > k) into k.
    # If k is in the array, we just need to transform all values > k.
    if k in unique_elements:
        return len(unique_elements) - 1
    else:
        return len(unique_elements)
