import heapq
from typing import List

def solve(queries: List[List[int]], k: int) -> List[int]:
    # We use a max-heap to keep track of the k smallest distances.
    # Since Python's heapq is a min-heap, we store negative values to simulate a max-heap.
    max_heap = []
    results = []
    
    for x, y in queries:
        dist = abs(x) + abs(y)
        
        if len(max_heap) < k:
            heapq.heappush(max_heap, -dist)
        elif dist < -max_heap[0]:
            heapq.heapreplace(max_heap, -dist)
            
        if len(max_heap) < k:
            results.append(-1)
        else:
            results.append(-max_heap[0])
            
    return results
