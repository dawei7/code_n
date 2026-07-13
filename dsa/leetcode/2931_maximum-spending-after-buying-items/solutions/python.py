import heapq
from typing import List

def solve(values: List[List[int]]) -> int:
    """
    Calculates the maximum spending by greedily picking the smallest available 
    items across all shops using a min-heap.
    """
    m = len(values)
    n = len(values[0])
    
    # Min-heap stores tuples of (price, row_index)
    # We initialize it with the last element of each row.
    min_heap = []
    for i in range(m):
        heapq.heappush(min_heap, (values[i][n - 1], i))
    
    # Keep track of the current index being pointed to in each row
    row_pointers = [n - 1] * m
    
    total_spending = 0
    # We buy one item per day for m * n days
    for day in range(1, (m * n) + 1):
        price, row_idx = heapq.heappop(min_heap)
        
        # Add to total spending multiplied by the current day
        total_spending += price * day
        
        # Move the pointer for this row to the left
        row_pointers[row_idx] -= 1
        
        # If there are still items in this row, push the next one to the heap
        if row_pointers[row_idx] >= 0:
            next_price = values[row_idx][row_pointers[row_idx]]
            heapq.heappush(min_heap, (next_price, row_idx))
            
    return total_spending
