import math

def solve(prices: list[int], money: int) -> int:
    """
    Determines if two cheapest chocolates can be bought and returns the remaining money,
    or the original money if not affordable.

    Args:
        prices: A list of integers representing the prices of chocolates.
        money: An integer representing the initial amount of money.

    Returns:
        An integer representing the money left after buying the two cheapest chocolates,
        or the original money if they cannot be afforded.
    """
    # Initialize min1 and min2 to positive infinity to ensure any price will be smaller.
    # min1 will store the smallest price found.
    # min2 will store the second smallest price found.
    min1 = math.inf
    min2 = math.inf

    # Iterate through the prices to find the two smallest values
    for price in prices:
        if price < min1:
            # If current price is smaller than the current smallest (min1),
            # then min1 becomes the new second smallest (min2),
            # and current price becomes the new smallest (min1).
            min2 = min1
            min1 = price
        elif price < min2:
            # If current price is not smaller than min1, but is smaller than min2,
            # then it becomes the new second smallest (min2).
            min2 = price
    
    # Calculate the total cost of the two cheapest chocolates
    total_cost = min1 + min2

    # Check if the total cost is within the available money
    if total_cost <= money:
        # If affordable, return the money left
        return money - total_cost
    else:
        # If not affordable, return the original money
        return money
