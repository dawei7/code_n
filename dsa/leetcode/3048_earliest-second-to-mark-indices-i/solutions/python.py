def solve(nums: list[int], changeIndices: list[int]) -> int:
    n = len(nums)
    m = len(changeIndices)

    def check(time: int) -> bool:
        # last_occurrence stores the latest second an index can be marked
        last_occurrence = [-1] * (n + 1)
        for i in range(time):
            last_occurrence[changeIndices[i]] = i
        
        # If any index never appears in the first 'time' seconds, we can't mark it
        if -1 in last_occurrence[1:]:
            return False
        
        # Sort indices by their last occurrence to process greedily
        # We need to perform nums[i] decrements before the last_occurrence[i+1]
        needed = list(nums)
        events = sorted([(last_occurrence[i + 1], i) for i in range(n)])
        
        decrements_available = 0
        current_time = 0
        
        for deadline, idx in events:
            # Time available for decrements before this deadline
            # is the time elapsed minus time spent marking previous indices
            time_to_use = deadline - current_time
            if time_to_use < needed[idx]:
                return False
            
            # We use 'needed[idx]' seconds to decrement, and 1 second to mark
            current_time += needed[idx] + 1
            
        return True

    low = 1
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
