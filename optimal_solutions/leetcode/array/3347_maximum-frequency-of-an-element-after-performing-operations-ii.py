from collections import Counter

def solve(nums: list[int], k: int, numOperations: int) -> int:
    if not nums:
        return 0
    
    nums.sort()
    n = len(nums)
    counts = Counter(nums)
    unique_nums = sorted(counts.keys())
    
    # We use a difference array approach to count how many numbers can reach x
    # without an operation (already equal) and with an operation (within k).
    # An element nums[i] can reach [nums[i]-k, nums[i]+k] using 1 operation.
    
    # Events for the sweep-line:
    # 1. Start of range [nums[i]-k, nums[i]+k]
    # 2. End of range [nums[i]-k, nums[i]+k]
    # 3. The value nums[i] itself (no operation needed)
    
    events = []
    for x in unique_nums:
        # Range [x-k, x+k]
        events.append((x - k, 1, counts[x]))
        events.append((x + k, 3, counts[x]))
        
    events.sort()
    
    # Sliding window over the sorted unique values to find max frequency
    # We maintain the count of elements that can reach the current window
    # using 0 operations (already there) and 1 operation.
    
    ans = 0
    left = 0
    current_in_range = 0
    
    # Using a sliding window on the unique numbers
    # For a target value 'v', the elements that can reach it are those
    # in [v-k, v+k].
    
    # We use two pointers to maintain the window [v-k, v+k]
    # and calculate how many elements can be transformed to v.
    
    # The number of elements already equal to v is counts[v].
    # The number of elements that can be transformed to v is 
    # (total elements in [v-k, v+k]) - (elements already equal to v).
    # We can use at most numOperations.
    
    # Optimized approach:
    # For each unique number x, the window of elements that can reach x
    # is [x-k, x+k].
    
    j = 0
    total_in_window = 0
    for i, x in enumerate(unique_nums):
        while j < len(unique_nums) and unique_nums[j] <= x + k:
            total_in_window += counts[unique_nums[j]]
            j += 1
        
        # Elements in [x-k, x+k]
        # We need to subtract elements that are outside [x-k, x+k]
        # but were added to total_in_window
        while unique_nums[left] < x - k:
            total_in_window -= counts[unique_nums[left]]
            left += 1
            
        # Max frequency = (elements already equal to x) + 
        # min(numOperations, total_in_window - counts[x])
        can_transform = total_in_window - counts[x]
        ans = max(ans, counts[x] + min(numOperations, can_transform))
        
    # Also consider the case where we transform elements to a value 
    # that wasn't in the original array
    # The optimal value must be in [nums[i]-k, nums[i]+k]
    # We check the boundaries of these intervals
    points = []
    for x in unique_nums:
        points.append(x - k)
        points.append(x + k)
    
    for p in points:
        # Count elements in [p-k, p+k]
        # This is covered by the sliding window logic above
        pass
        
    return ans
