import heapq

def solve(costs: list[int], k: int, candidates: int) -> int:
    n = len(costs)
    left_heap = []
    right_heap = []
    
    left_ptr = 0
    right_ptr = n - 1
    
    # Fill the heaps initially
    # We use (cost, index) to handle tie-breaking by index automatically
    while len(left_heap) < candidates and left_ptr <= right_ptr:
        heapq.heappush(left_heap, (costs[left_ptr], left_ptr))
        left_ptr += 1
        
    while len(right_heap) < candidates and left_ptr <= right_ptr:
        heapq.heappush(right_heap, (costs[right_ptr], right_ptr))
        right_ptr -= 1
        
    total_cost = 0
    for _ in range(k):
        # Determine which heap has the smaller minimum
        # If one heap is empty, we must pick from the other
        if not right_heap or (left_heap and left_heap[0] <= right_heap[0]):
            cost, idx = heapq.heappop(left_heap)
            total_cost += cost
            # Replenish left heap if possible
            if left_ptr <= right_ptr:
                heapq.heappush(left_heap, (costs[left_ptr], left_ptr))
                left_ptr += 1
        else:
            cost, idx = heapq.heappop(right_heap)
            total_cost += cost
            # Replenish right heap if possible
            if left_ptr <= right_ptr:
                heapq.heappush(right_heap, (costs[right_ptr], right_ptr))
                right_ptr -= 1
                
    return total_cost
