from collections import defaultdict

def get_digit_sum(n: int) -> int:
    """
    Calculates the sum of digits for a given positive integer.
    """
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

def solve(nums: list[int]) -> int:
    """
    Finds the maximum sum of a pair of numbers from `nums` that have an equal sum of digits.
    
    Args:
        nums: A list of positive integers.
    
    Returns:
        The maximum sum of such a pair, or -1 if no such pair exists.
    """
    max_pair_sum = -1
    
    # digit_sum_largest_two: A dictionary where keys are digit sums,
    # and values are lists [largest_num, second_largest_num] encountered so far
    # for that digit sum. Initialized with [0, 0] as numbers are positive.
    digit_sum_largest_two = defaultdict(lambda: [0, 0])

    for num in nums:
        s = get_digit_sum(num)
        
        # Update the two largest numbers for the current digit sum 's'
        if num > digit_sum_largest_two[s][0]:
            # If 'num' is greater than the current largest,
            # the old largest becomes the new second largest.
            digit_sum_largest_two[s][1] = digit_sum_largest_two[s][0]
            digit_sum_largest_two[s][0] = num
        elif num > digit_sum_largest_two[s][1]:
            # If 'num' is not greater than the largest but is greater than the second largest,
            # it becomes the new second largest.
            digit_sum_largest_two[s][1] = num
    
    # Iterate through the stored pairs (largest, second_largest) for each digit sum
    for largest_num, second_largest_num in digit_sum_largest_two.values():
        # A valid pair exists if 'second_largest_num' is greater than 0.
        # (Since all input numbers are positive, 0 indicates that either
        # no number or only one number was found for this digit sum).
        if second_largest_num > 0:
            current_pair_sum = largest_num + second_largest_num
            max_pair_sum = max(max_pair_sum, current_pair_sum)
            
    return max_pair_sum
