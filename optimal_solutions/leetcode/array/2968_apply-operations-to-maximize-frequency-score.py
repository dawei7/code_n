def solve(nums: list[int], k: int) -> int:
    nums.sort()
    n = len(nums)
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + nums[i]

    def get_cost(left: int, right: int) -> int:
        # Median index
        mid = (left + right) // 2
        median = nums[mid]
        
        # Cost = (elements to the right of median) - (elements to the left)
        # Sum of right side: nums[mid+1...right]
        # Sum of left side: nums[left...mid-1]
        
        right_count = right - mid
        left_count = mid - left
        
        right_sum = prefix_sum[right + 1] - prefix_sum[mid + 1]
        left_sum = prefix_sum[mid] - prefix_sum[left]
        
        return (right_count * median - right_sum) + (left_sum - left_count * median)

    max_freq = 0
    left = 0
    for right in range(n):
        while get_cost(left, right) > k:
            left += 1
        max_freq = max(max_freq, right - left + 1)
        
    return max_freq
