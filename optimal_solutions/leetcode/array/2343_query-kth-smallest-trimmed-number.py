def solve(nums: list[str], queries: list[list[int]]) -> list[int]:
    """
    For each query [k, trim], finds the k-th smallest number after trimming
    each original number to its rightmost 'trim' digits, and returns its
    original 0-indexed position.
    """
    results = []
    
    for k, trim in queries:
        # Step 1: Trim numbers and store with original indices
        # We store (trimmed_value, original_index) pairs.
        # Python's int() handles leading zeros correctly (e.g., int("007") == 7).
        # Slicing num_str[-trim:] gets the rightmost 'trim' digits.
        trimmed_data = []
        for i, num_str in enumerate(nums):
            trimmed_val_str = num_str[-trim:]
            trimmed_val_int = int(trimmed_val_str)
            trimmed_data.append((trimmed_val_int, i))
            
        # Step 2: Sort the trimmed data.
        # Python's default sort for tuples sorts by the first element,
        # then by the second element (original_index) if the first elements are equal.
        # This provides a stable sort, which is generally good practice.
        trimmed_data.sort()
        
        # Step 3: Retrieve the original index of the k-th smallest.
        # k is 1-indexed, so we access the (k-1)-th element in the 0-indexed list.
        kth_smallest_original_index = trimmed_data[k - 1][1]
        results.append(kth_smallest_original_index)
        
    return results
