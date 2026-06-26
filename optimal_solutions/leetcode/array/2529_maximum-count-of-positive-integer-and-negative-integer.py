import bisect

def solve(nums: list[int]) -> int:
    """
    Finds the maximum of the count of negative and positive integers
    in a sorted array using binary search.
    """
    # The number of negative integers is the index of the first element >= 0
    neg_count = bisect.bisect_left(nums, 0)
    
    # The number of positive integers is the total length minus the index 
    # of the first element > 0
    pos_count = len(nums) - bisect.bisect_right(nums, 0)
    
    return max(neg_count, pos_count)
