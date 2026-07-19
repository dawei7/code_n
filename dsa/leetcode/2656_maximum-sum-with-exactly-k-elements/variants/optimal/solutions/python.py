def solve(nums: list[int], k: int) -> int:
    """
    Calculates the maximum score achievable by performing exactly k operations.

    In each operation, the largest element 'm' is chosen from the array,
    'm' is added to the score, 'm' is removed, and 'm + 1' is added back.

    Args:
        nums: A list of integers.
        k: The number of operations to perform.

    Returns:
        The maximum possible score after k operations.
    """
    # The greedy strategy is to always pick the largest available number.
    # If we pick 'm', we get 'm' points and 'm+1' is added to the array.
    # This means the numbers picked will be:
    # max_val, max_val + 1, max_val + 2, ..., max_val + (k - 1)

    max_val = max(nums)

    # The sum of an arithmetic series:
    # Sum = (number_of_terms / 2) * (first_term + last_term)
    # Here, number_of_terms = k
    # first_term = max_val
    # last_term = max_val + (k - 1)

    # Alternatively, the sum can be seen as:
    # k * max_val + (0 + 1 + 2 + ... + (k - 1))
    # The sum of 0 to (k-1) is (k * (k - 1)) // 2

    total_score = k * max_val + (k * (k - 1)) // 2

    return total_score
