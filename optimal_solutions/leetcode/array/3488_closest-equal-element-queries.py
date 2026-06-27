from collections import defaultdict
from bisect import bisect_left

def solve(nums, queries):
    # Map each value to a sorted list of its indices
    pos_map = defaultdict(list)
    for idx, val in enumerate(nums):
        pos_map[val].append(idx)
    
    results = []
    
    for i, k in queries:
        val = nums[i]
        indices = pos_map[val]
        
        # Find the position of i in the sorted list of indices
        idx_in_list = bisect_left(indices, i)
        
        best_idx = -1
        min_dist = float('inf')
        
        # Check neighbors in the sorted list:
        # The closest index must be either the one at idx_in_list, 
        # idx_in_list - 1, or idx_in_list + 1
        candidates = []
        if idx_in_list < len(indices):
            candidates.append(indices[idx_in_list])
        if idx_in_list > 0:
            candidates.append(indices[idx_in_list - 1])
            
        for cand in candidates:
            if cand == i:
                continue
            dist = abs(cand - i)
            if dist <= k:
                if dist < min_dist:
                    min_dist = dist
                    best_idx = cand
                elif dist == min_dist:
                    if best_idx == -1 or cand < best_idx:
                        best_idx = cand
        
        results.append(best_idx)
        
    return results
