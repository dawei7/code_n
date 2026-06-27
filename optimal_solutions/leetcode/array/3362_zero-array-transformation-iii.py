import heapq
from collections import defaultdict

def solve(nums: list[int], queries: list[list[int]]) -> int:
    n = len(nums)
    # Group queries by their start index
    starts = defaultdict(list)
    for l, r in queries:
        starts[l].append(r)
    
    # Max-heap to store the end indices of active queries
    # We want to pick queries that end as far as possible
    active_queries = []
    
    # Difference array to track current reduction applied to nums[i]
    diff = [0] * (n + 1)
    current_reduction = 0
    count = 0
    
    for i in range(n):
        # Add all queries starting at i to the heap
        for r in starts[i]:
            heapq.heappush(active_queries, -r)
        
        # Update current reduction using difference array
        current_reduction += diff[i]
        
        # While current value is not satisfied, use queries
        while nums[i] + current_reduction > 0:
            if not active_queries:
                return -1
            
            # Pick the query that ends furthest to the right
            r = -heapq.heappop(active_queries)
            
            # If the query ends before current index, it's useless
            if r < i:
                continue
            
            # Apply the query
            count += 1
            current_reduction -= 1
            # The effect of this query ends at r
            diff[r + 1] += 1
            
    return count
