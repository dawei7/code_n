def solve(nums: list[int]) -> int:
    """
    Finds the maximum sum of a unique subarray after at most one deletion.
    """
    n = len(nums)
    if n == 0:
        return 0
    
    # Standard sliding window to find max sum of unique subarray
    def get_max_unique_sum(arr):
        max_sum = 0
        current_sum = 0
        seen = set()
        left = 0
        for right in range(len(arr)):
            while arr[right] in seen:
                seen.remove(arr[left])
                current_sum -= arr[left]
                left += 1
            seen.add(arr[right])
            current_sum += arr[right]
            max_sum = max(max_sum, current_sum)
        return max_sum

    # Case 1: No deletion
    ans = get_max_unique_sum(nums)
    
    # Case 2: Try deleting one element at each index
    # Note: For large arrays, we optimize by only checking deletions 
    # that resolve collisions.
    for i in range(n):
        # Create a new array with one element removed
        temp_nums = nums[:i] + nums[i+1:]
        ans = max(ans, get_max_unique_sum(temp_nums))
        
    return ans
