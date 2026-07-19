import heapq

def solve(nums: list[int], k: int, multiplier: int) -> list[int]:
    # Create a min-heap of (value, index) tuples
    # The heap naturally handles the smallest value, and the index
    # handles the tie-breaking rule (leftmost first).
    heap = [(val, i) for i, val in enumerate(nums)]
    heapq.heapify(heap)
    
    for _ in range(k):
        val, idx = heapq.heappop(heap)
        new_val = val * multiplier
        nums[idx] = new_val
        heapq.heappush(heap, (new_val, idx))
        
    return nums
