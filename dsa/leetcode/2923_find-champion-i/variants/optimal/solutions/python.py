def solve(grid: list[list[int]]) -> int:
    """
    Finds the champion by identifying the row with the maximum sum.
    In a tournament matrix where a champion exists, the champion's row
    will contain (n-1) ones, while all other rows will contain fewer.
    """
    n = len(grid)
    champion = 0
    max_wins = -1
    
    for i in range(n):
        current_wins = sum(grid[i])
        if current_wins > max_wins:
            max_wins = current_wins
            champion = i
            
    return champion
