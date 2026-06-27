from collections import defaultdict

def solve(grid: list[list[int]]) -> list[list[int]]:
    n = len(grid)
    # Diagonals are defined by the constant difference (row - col)
    # For a square matrix, row - col ranges from -(n-1) to (n-1)
    diagonals = defaultdict(list)
    
    # Group elements by their diagonal index
    for r in range(n):
        for c in range(n):
            diagonals[r - c].append(grid[r][c])
            
    # Sort each diagonal
    # Note: The problem requires diagonals to be sorted.
    # Based on the standard definition of matrix diagonals:
    # For r - c = k, as r increases, c increases.
    # We sort them so that the smallest elements appear at the start of the diagonal.
    for k in diagonals:
        diagonals[k].sort()
        
    # Reconstruct the matrix
    # We need to pop elements from the sorted lists. 
    # To maintain the order, we need to know the direction.
    # For diagonals where r - c = k:
    # If k >= 0, the diagonal starts at (k, 0) and ends at (n-1, n-1-k)
    # If k < 0, the diagonal starts at (0, -k) and ends at (n-1+k, n-1)
    
    result = [[0] * n for _ in range(n)]
    
    # Use a pointer to track which element to take from the sorted list
    # For diagonals, we fill them in the order they appear in the matrix
    # (top-left to bottom-right traversal)
    indices = defaultdict(int)
    for r in range(n):
        for c in range(n):
            k = r - c
            result[r][c] = diagonals[k][indices[k]]
            indices[k] += 1
            
    return result
