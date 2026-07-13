import heapq
import math

def solve(nums: list[int], k: int) -> int:
    """
    Maximizes the score by repeatedly picking the largest element,
    adding it to the score, and replacing it with ceil(val / 3).
    Uses a max-heap (simulated with negative values in Python's min-heap).
    """
    # Python's heapq is a min-heap. To simulate a max-heap, 
    # we store the negative of each number.
    max_heap = [-x for x in nums]
    heapq.heapify(max_heap)
    
    total_score = 0
    
    for _ in range(k):
        # Extract the largest element
        largest = -heapq.heappop(max_heap)
        total_score += largest
        
        # Calculate ceil(largest / 3)
        # Using integer arithmetic: (largest + 2) // 3 is equivalent to ceil(largest / 3)
        new_val = (largest + 2) // 3
        
        # Push the new value back into the heap
        heapq.heappush(max_heap, -new_val)
        
    return total_score
