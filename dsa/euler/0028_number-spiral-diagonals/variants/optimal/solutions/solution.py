def solve(size: int = 1001) -> int:
    """Sum of numbers on diagonals of a size x size clockwise number spiral.
    
    Time Complexity: O(size)
    Space Complexity: O(1)
    """
    total = 1
    for k in range(3, size + 1, 2):
        total += 4 * k * k - 6 * (k - 1)
    return total
