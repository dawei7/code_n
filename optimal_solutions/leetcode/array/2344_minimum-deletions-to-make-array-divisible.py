import math

def solve(nums: list[int], numsDivide: list[int]) -> int:
    """
    Calculates the minimum number of deletions from `nums` such that the smallest
    remaining element in `nums` divides all elements in `numsDivide`.

    Args:
        nums: A list of integers.
        numsDivide: A list of integers.

    Returns:
        The minimum number of deletions, or -1 if no such element exists.
    """
    # Step 1: Calculate the Greatest Common Divisor (GCD) of all elements in numsDivide.
    # A number x divides all elements in numsDivide if and only if x divides their GCD.
    g_nums_divide = numsDivide[0]
    for i in range(1, len(numsDivide)):
        g_nums_divide = math.gcd(g_nums_divide, numsDivide[i])

    # Step 2: Sort nums in ascending order.
    # This allows us to find the smallest qualifying number with the minimum deletions.
    nums.sort()

    # Step 3: Iterate through the sorted nums array.
    # The first element that divides g_nums_divide is our answer.
    for i, num in enumerate(nums):
        if g_nums_divide % num == 0:
            # If num divides g_nums_divide, it means num divides all elements in numsDivide.
            # Since nums is sorted, this is the smallest such num, and 'i' is the
            # number of elements we had to delete to get to this num.
            return i

    # Step 4: If no such number is found after checking all elements in nums.
    return -1
