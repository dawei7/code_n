import heapq

def solve(nums: list[int], changeIndices: list[int]) -> int:
    n = len(nums)
    m = len(changeIndices)
    
    def check(time_limit: int) -> bool:
        # last_occurrence[i] stores the latest time index i appears in changeIndices
        last_occurrence = [-1] * n
        for i in range(time_limit):
            last_occurrence[changeIndices[i] - 1] = i
            
        # If any index never appears, we can't mark it
        if -1 in last_occurrence:
            return False
            
        # Map time to the index that should be marked at that time
        mark_at = {}
        for i, time in enumerate(last_occurrence):
            mark_at[time] = i
            
        pq = []
        available_seconds = 0
        marked_count = 0
        
        # Iterate backwards from the time_limit
        for t in range(time_limit - 1, -1, -1):
            idx = changeIndices[t] - 1
            if t == last_occurrence[idx]:
                # We must mark this index here
                val = nums[idx]
                if available_seconds < val:
                    return False
                available_seconds -= val
                marked_count += 1
                heapq.heappush(pq, val)
            else:
                # We can use this second to reduce a value
                available_seconds += 1
                
        return marked_count == n

    low = 0
    high = m
    ans = -1
    
    while low <= high:
        mid = (low + high) // 2
        if check(mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
            
    return ans
