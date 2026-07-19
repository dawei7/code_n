from collections import defaultdict

def solve(nums: list[int], k: int) -> int:
    """
    Finds the length of the longest subarray where no element appears more than k times.
    Uses a sliding window approach with a hash map to track frequencies.
    """
    max_length = 0
    left = 0
    counts = defaultdict(int)
    
    for right in range(len(nums)):
        # Add the current element to the window
        counts[nums[right]] += 1
        
        # If the frequency exceeds k, shrink the window from the left
        while counts[nums[right]] > k:
            counts[nums[left]] -= 1
            left += 1
            
        # Update the maximum length found so far
        max_length = max(max_length, right - left + 1)
        
    return max_length
