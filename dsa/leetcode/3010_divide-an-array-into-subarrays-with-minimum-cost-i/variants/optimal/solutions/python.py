def solve(nums: list[int]) -> int:
    """
    To minimize the sum of the first elements of three subarrays,
    we must pick nums[0] as the first element of the first subarray.
    Then, we pick the two smallest elements from the remaining array
    (nums[1:]) to be the first elements of the second and third subarrays.
    """
    # The first element is fixed as nums[0]
    first_element = nums[0]
    
    # Find the two smallest elements in the rest of the array
    remaining = nums[1:]
    remaining.sort()
    
    # The sum is the first element plus the two smallest from the rest
    return first_element + remaining[0] + remaining[1]
