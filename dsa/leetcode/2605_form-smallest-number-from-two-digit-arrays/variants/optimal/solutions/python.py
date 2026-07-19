def solve(nums1: list[int], nums2: list[int]) -> int:
    set1 = set(nums1)
    set2 = set(nums2)
    
    # Check for common digits
    common = set1.intersection(set2)
    if common:
        return min(common)
    
    # If no common digits, pick the smallest from each
    min1 = min(set1)
    min2 = min(set2)
    
    # Form the smallest two-digit number
    if min1 < min2:
        return min1 * 10 + min2
    else:
        return min2 * 10 + min1
