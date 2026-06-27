import heapq
from collections import defaultdict

def solve(nums: list[int], freq: list[int]) -> list[int]:
    # Map to store the current frequency of each ID
    counts = defaultdict(int)
    # Max-heap to store (-frequency, id)
    # We use negative frequency because heapq is a min-heap by default
    max_heap = []
    results = []
    
    for i in range(len(nums)):
        id_val = nums[i]
        change = freq[i]
        
        # Update the frequency in the hash map
        counts[id_val] += change
        
        # Push the new frequency into the heap
        heapq.heappush(max_heap, (-counts[id_val], id_val))
        
        # Lazy removal: check if the top of the heap is stale
        # The top is stale if the frequency in the heap doesn't match the current map
        while max_heap and -max_heap[0][0] != counts[max_heap[0][1]]:
            heapq.heappop(max_heap)
            
        # The current max frequency is at the top of the heap
        if max_heap:
            results.append(-max_heap[0][0])
        else:
            results.append(0)
            
    return results
