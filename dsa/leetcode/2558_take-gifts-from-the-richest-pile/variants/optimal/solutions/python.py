import heapq
import math

def solve(gifts: list[int], k: int) -> int:
    # Python's heapq is a min-heap by default. 
    # We negate the values to simulate a max-heap.
    max_heap = [-g for g in gifts]
    heapq.heapify(max_heap)
    
    for _ in range(k):
        # Extract the largest pile (smallest negative value)
        largest = -heapq.heappop(max_heap)
        
        # Calculate the new value: floor of the square root
        new_val = math.isqrt(largest)
        
        # Push the modified value back into the heap
        heapq.heappush(max_heap, -new_val)
        
    # The result is the sum of the absolute values of the heap elements
    return sum(-val for val in max_heap)
