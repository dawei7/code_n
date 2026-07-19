def solve(nums: list[int]) -> int:
    n = len(nums)
    # Precompute prefix sums to allow O(1) subarray sum queries
    # prefix_sums[i] stores the sum of nums[0...i-1]
    prefix_sums = [0] * (n + 1)
    for i in range(n):
        prefix_sums[i + 1] = prefix_sums[i] + nums[i]
    
    total_sum = 0
    for i in range(n):
        start = max(0, i - nums[i])
        end = i
        # The sum of subarray nums[start...end] is prefix_sums[end + 1] - prefix_sums[start]
        current_subarray_sum = prefix_sums[end + 1] - prefix_sums[start]
        total_sum += current_subarray_sum
        
    return total_sum
