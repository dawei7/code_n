from collections import defaultdict

def solve(nums: list[int], k: int) -> int:
    """
    Counts the number of good subarrays using a sliding window approach.
    A subarray is good if it has at least k pairs.
    """
    n = len(nums)
    count = 0
    left = 0
    current_pairs = 0
    freq = defaultdict(int)
    
    for right in range(n):
        # Add the current element to the window
        # If it appeared 'f' times before, it forms 'f' new pairs
        x = nums[right]
        current_pairs += freq[x]
        freq[x] += 1
        
        # While the window is valid (has at least k pairs),
        # all subarrays starting at 'left' and ending at 'right' or further
        # are also valid.
        while current_pairs >= k:
            # All subarrays from [left, right], [left, right+1]...[left, n-1] are good
            count += (n - right)
            
            # Shrink the window from the left
            left_val = nums[left]
            freq[left_val] -= 1
            # Removing an element that appeared 'f' times removes 'f-1' pairs
            current_pairs -= freq[left_val]
            left += 1
            
    return count
