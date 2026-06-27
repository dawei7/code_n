def solve(nums1: list[int], nums2: list[int]) -> int:
    n = len(nums1)
    set1 = set(nums1)
    set2 = set(nums2)
    
    # Elements unique to each set
    unique1 = len(set1)
    unique2 = len(set2)
    
    # Elements present in both sets
    common = set1.intersection(set2)
    num_common = len(common)
    
    # Elements exclusive to set1 and set2
    only1 = unique1 - num_common
    only2 = unique2 - num_common
    
    # We need to remove n/2 from each.
    # First, remove from exclusive elements if possible.
    # If we still need to remove more, remove from common elements.
    
    rem1 = n // 2
    rem2 = n // 2
    
    # Remove from exclusive parts
    take1 = min(rem1, only1)
    rem1 -= take1
    
    take2 = min(rem2, only2)
    rem2 -= take2
    
    # Remaining removals must come from the common pool
    # The common pool is shared, so we subtract from num_common
    num_common -= (rem1 + rem2)
    
    # The result is the sum of remaining exclusive elements and remaining common elements
    return (only1 - take1) + (only2 - take2) + num_common
