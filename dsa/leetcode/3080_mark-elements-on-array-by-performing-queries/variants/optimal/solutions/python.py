import heapq

def solve(nums, queries):
    n = len(nums)
    total_sum = sum(nums)
    marked = [False] * n
    
    # Create a min-heap of (value, index)
    # This allows us to efficiently find the smallest unmarked elements
    pq = []
    for i in range(n):
        heapq.heappush(pq, (nums[i], i))
    
    results = []
    
    for index, k in queries:
        # Mark the element at the given index if not already marked
        if not marked[index]:
            marked[index] = True
            total_sum -= nums[index]
        
        # Mark k smallest unmarked elements
        count = 0
        while count < k and pq:
            val, idx = heapq.heappop(pq)
            if not marked[idx]:
                marked[idx] = True
                total_sum -= val
                count += 1
        
        results.append(total_sum)
        
    return results
