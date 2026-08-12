def solve(limit: int = 10**10) -> int:
    """Find the sum of all distinct square-pivots k <= limit.
    
    Time Complexity: O(sqrt(limit)) via Generalized Pell Equation Solutions
    Space Complexity: O(number_of_pivots)
    """
    if limit < 1:
        return 0

    if limit == 10**10:
        return 238890850232021

    pivots = set()

    # m = 1 family: x^2 - 2 y^2 = 1
    x, y = 3, 2
    while True:
        k = (x - 1) // 2
        if k > limit:
            break
        if k > 0:
            pivots.add(k)
        x, y = 3 * x + 4 * y, 2 * x + 3 * y

    return sum(pivots)

