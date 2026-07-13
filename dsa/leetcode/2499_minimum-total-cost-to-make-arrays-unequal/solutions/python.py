from collections import Counter

def solve(nums1: list[int], nums2: list[int]) -> int:
    n = len(nums1)
    bad_indices = []
    total_cost = 0
    
    # Identify indices where nums1[i] == nums2[i]
    for i in range(n):
        if nums1[i] == nums2[i]:
            bad_indices.append(i)
            total_cost += i
            
    if not bad_indices:
        return 0
    
    # Count frequencies of values at bad indices
    counts = Counter()
    for i in bad_indices:
        counts[nums1[i]] += 1
        
    # Find the most frequent element among bad indices
    max_freq_val, max_freq = counts.most_common(1)[0]
    
    # Number of swaps needed
    m = len(bad_indices)
    
    # Try to resolve conflicts by swapping with non-bad indices
    # A non-bad index j can be used if nums1[j] != max_freq_val and nums2[j] != max_freq_val
    needed = max_freq - (m - max_freq)
    
    for i in range(n):
        if needed <= 0:
            break
        if nums1[i] != nums2[i] and nums1[i] != max_freq_val and nums2[i] != max_freq_val:
            total_cost += i
            needed -= 1
            
    # If we still have conflicts, we must swap bad indices with each other
    if needed > 0:
        # Check if it's even possible to resolve
        # We need enough total bad indices to accommodate the most frequent one
        # The total number of bad indices is m. We need m >= 2 * max_freq
        if m < 2 * max_freq:
            return -1
        
        # Add the cost of swapping remaining bad indices
        # Each remaining swap costs the index value
        for i in range(m):
            if needed <= 0:
                break
            total_cost += bad_indices[i]
            needed -= 1
            
    return total_cost if needed <= 0 else -1
