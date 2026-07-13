from bisect import bisect_left, bisect_right

def count_pairs_with_sum_less_than(nums, target):
    """
    Helper function to count pairs (i, j) with i < j such that nums[i] + nums[j] < target.
    Uses two pointers on a sorted array.
    """
    count = 0
    left = 0
    right = len(nums) - 1
    while left < right:
        if nums[left] + nums[right] < target:
            # All elements between left and right form a valid pair with nums[left]
            count += (right - left)
            left += 1
        else:
            right -= 1
    return count

def solve(nums: list[int], lower: int, upper: int) -> int:
    """
    Calculates the number of fair pairs by finding pairs with sum <= upper
    and subtracting pairs with sum < lower.
    """
    nums.sort()
    
    # Pairs with sum <= upper is equivalent to sum < upper + 1
    count_upper = count_pairs_with_sum_less_than(nums, upper + 1)
    
    # Pairs with sum < lower
    count_lower = count_pairs_with_sum_less_than(nums, lower)
    
    return count_upper - count_lower
