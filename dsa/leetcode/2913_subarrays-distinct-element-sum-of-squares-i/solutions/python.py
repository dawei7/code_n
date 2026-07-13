def solve(nums: list[int]) -> int:
    """
    Calculates the sum of squares of the count of distinct elements 
    for all contiguous subarrays.
    """
    n = len(nums)
    total_sum = 0
    
    # Iterate over all possible starting positions of subarrays
    for i in range(n):
        distinct_elements = set()
        # Iterate over all possible ending positions
        for j in range(i, n):
            distinct_elements.add(nums[j])
            # Add the square of the count of distinct elements to the total
            count = len(distinct_elements)
            total_sum += count * count
            
    return total_sum
