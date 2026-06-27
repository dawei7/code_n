import heapq

def solve(heights, queries):
    n = len(heights)
    q = len(queries)
    results = [-1] * q
    
    # Store queries by their rightmost index (max(a, b))
    # We process from right to left to handle queries efficiently
    deferred_queries = [[] for _ in range(n)]
    
    for i in range(q):
        a, b = queries[i]
        if a > b:
            a, b = b, a
        
        # If a == b or heights[b] > heights[a], they can meet at b
        if a == b or heights[b] > heights[a]:
            results[i] = b
        else:
            # Otherwise, they need a building at index > b with height > max(heights[a], heights[b])
            deferred_queries[b].append((max(heights[a], heights[b]), i))
            
    min_heap = []
    
    # Iterate backwards through buildings
    for i in range(n - 1, -1, -1):
        # Add all queries waiting for a building at this index
        for height, query_idx in deferred_queries[i]:
            heapq.heappush(min_heap, (height, query_idx))
            
        # Check if current building can satisfy the smallest height requirement in heap
        while min_heap and heights[i] > min_heap[0][0]:
            height, query_idx = heapq.heappop(min_heap)
            results[query_idx] = i
            
    return results
