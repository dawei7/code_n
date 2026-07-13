def solve(nums: list[int]) -> int:
    n = len(nums)
    total_sum = 0
    
    # Iterate through 1-based indices
    for i in range(1, n + 1):
        # Check if i is a divisor of n
        if n % i == 0:
            # Add the square of the element at 0-based index (i-1)
            total_sum += nums[i - 1] ** 2
            
    return total_sum
