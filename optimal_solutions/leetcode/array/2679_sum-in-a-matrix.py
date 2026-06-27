def solve(nums: list[list[int]]) -> int:
    """
    Calculates the total score by repeatedly finding the maximum element
    across rows from the largest available elements in each row.

    The strategy is to sort each row first. Then, for each "column" of
    elements (from rightmost to leftmost in the sorted rows), find the
    maximum value among all rows in that column and add it to the score.

    Args:
        nums: A list of lists of integers representing an m x n matrix.

    Returns:
        An integer representing the total accumulated score.
    """
    m = len(nums)
    n = len(nums[0])

    # Step 1: Sort each row in ascending order.
    # This allows us to easily pick the largest available element
    # by iterating from right to left in each sorted row.
    for i in range(m):
        nums[i].sort()

    total_score = 0

    # Step 2: Iterate n times, simulating the n operations.
    # In each iteration, we consider the elements at the same "rank"
    # (e.g., largest, second largest, etc.) from each row.
    # We iterate from the rightmost column (largest elements) to the leftmost.
    for j in range(n - 1, -1, -1):
        current_max_across_rows = 0
        # Find the maximum element among all rows for the current column 'j'.
        for i in range(m):
            current_max_across_rows = max(current_max_across_rows, nums[i][j])
        
        # Add this maximum to the total score.
        total_score += current_max_across_rows
        
    return total_score
