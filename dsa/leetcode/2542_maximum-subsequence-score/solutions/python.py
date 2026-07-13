import heapq

def solve(nums1: list[int], nums2: list[int], k: int) -> int:
    # Pair elements and sort by nums2 in descending order
    # This allows us to treat the current nums2 value as the minimum
    pairs = sorted(zip(nums1, nums2), key=lambda x: x[1], reverse=True)
    
    min_heap = []
    current_sum = 0
    max_score = 0
    
    for i in range(len(pairs)):
        val1, val2 = pairs[i]
        
        # Add current val1 to the heap and update the running sum
        heapq.heappush(min_heap, val1)
        current_sum += val1
        
        # If we have more than k elements, remove the smallest val1
        if len(min_heap) > k:
            smallest = heapq.heappop(min_heap)
            current_sum -= smallest
            
        # If we have exactly k elements, calculate the score
        if len(min_heap) == k:
            # The current val2 is the minimum because we sorted descending
            max_score = max(max_score, current_sum * val2)
            
    return max_score
