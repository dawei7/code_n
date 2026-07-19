def solve(n: int) -> int:
    """
    Calculates the number of distinct integers on the board.
    For n = 1, the result is 1.
    For n > 1, the result is n - 1 because all integers from 2 to n 
    will eventually be added to the board.
    """
    if n == 1:
        return 1
    return n - 1
