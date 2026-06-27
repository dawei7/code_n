from collections import Counter
import bisect

def solve(nums: list[int], k: int, numOperations: int) -> int:
    # Count original frequencies
    counts = Counter(nums)
    # Get all unique values and potential boundaries
    # A value x can be reached by nums[i] if nums[i]-k <= x <= nums[i]+k
    # We only care about x values that are reachable from at least one nums[i]
    # The critical points are nums[i]-k and nums[i]+k
    
    events = []
    for x in counts:
        # Interval [x-k, x+k]
        # We use a difference array approach on the sorted unique points
        events.append((x - k, 1))
        events.append((x + k + 1, -1))
    
    events.sort()
    
    max_freq = 0
    current_reachable = 0
    event_idx = 0
    n = len(events)
    
    # We need to check all unique values that could be the target
    # The candidates are the original numbers and the boundaries
    candidates = sorted(list(set(nums)))
    
    # Sweep line to find how many numbers can reach a value 'val'
    # using an operation
    for val in candidates:
        while event_idx < n and events[event_idx][0] <= val:
            current_reachable += events[event_idx][1]
            event_idx += 1
        
        # current_reachable is the count of numbers that can reach 'val'
        # via an operation.
        # Some of these numbers might already be 'val' (no operation needed).
        # The number of operations needed is:
        # (Total numbers that can reach val) - (Numbers already equal to val)
        
        needed = max(0, current_reachable - counts[val])
        
        if needed <= numOperations:
            # We can make all 'current_reachable' numbers equal to 'val'
            # but we are limited by numOperations.
            # The frequency is (original count) + (number of operations performed)
            # which is min(current_reachable, counts[val] + numOperations)
            max_freq = max(max_freq, min(current_reachable, counts[val] + numOperations))
            
    return max_freq
