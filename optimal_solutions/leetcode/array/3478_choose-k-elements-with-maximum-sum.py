import heapq

def solve(nums1, nums2, k):
    n = len(nums1)
    # Create a list of indices and sort them based on nums1 values
    indices = sorted(range(n), key=lambda i: nums1[i])
    
    res = [0] * n
    min_heap = []
    current_sum = 0
    
    # We need to process indices such that we only consider j where nums1[j] < nums1[i]
    # Since multiple indices might have the same nums1 value, we group them
    i = 0
    while i < n:
        j = i
        # Find all indices with the same nums1 value
        while j < n and nums1[indices[j]] == nums1[indices[i]]:
            j += 1
        
        # For all indices in the current group, the valid j's are those processed before this group
        for idx in range(i, j):
            original_idx = indices[idx]
            if len(min_heap) < k:
                res[original_idx] = -1
            else:
                res[original_idx] = current_sum
        
        # Now add the current group's nums2 values to the heap
        for idx in range(i, j):
            val = nums2[indices[idx]]
            heapq.heappush(min_heap, val)
            current_sum += val
            if len(min_heap) > k:
                current_sum -= heapq.heappop(min_heap)
        
        i = j
        
    return res
