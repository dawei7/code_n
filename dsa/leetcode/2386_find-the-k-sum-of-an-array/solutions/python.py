import heapq

def solve(nums: list[int], k: int) -> int:
    # The maximum subsequence sum is the sum of all positive numbers.
    max_sum = sum(x for x in nums if x > 0)
    
    # We want to find the (k-1)-th smallest "loss" from the max_sum.
    # A loss is created by either removing a positive number or adding a negative number.
    # Both operations are equivalent to subtracting abs(x) from the max_sum.
    abs_nums = sorted([abs(x) for x in nums])
    
    # If k=1, the answer is simply the max_sum.
    if k == 1:
        return max_sum
    
    # Min-heap stores (loss, index)
    # We explore the smallest losses using a heap.
    pq = [(abs_nums[0], 0)]
    current_loss = 0
    
    for _ in range(k - 1):
        current_loss, i = heapq.heappop(pq)
        
        if i + 1 < len(abs_nums):
            # Option 1: Add the next element to the current loss
            heapq.heappush(pq, (current_loss + abs_nums[i + 1], i + 1))
            # Option 2: Replace the current element with the next element
            heapq.heappush(pq, (current_loss - abs_nums[i] + abs_nums[i + 1], i + 1))
            
    return max_sum - current_loss
