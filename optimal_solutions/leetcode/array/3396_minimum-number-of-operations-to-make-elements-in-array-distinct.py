def solve(nums):
    """
    Calculates the minimum number of operations to make all elements in an array distinct.

    Args:
        nums: A list of integers.

    Returns:
        An integer representing the minimum number of operations.
    """
    nums.sort()
    operations = 0
    for i in range(1, len(nums)):
        if nums[i] <= nums[i-1]:
            increment_needed = nums[i-1] - nums[i] + 1
            operations += increment_needed
            nums[i] = nums[i-1] + 1
    return operations
