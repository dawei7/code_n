import heapq

def solve(grid: list[list[int]], limits: list[int], k: int) -> int:
    """
    Calculates the maximum sum by picking at most k elements from the grid,
    respecting the row-specific limits.
    """
    candidates = []
    
    # For each row, pick the largest 'limits[i]' elements.
    # We use a min-heap to keep track of the largest elements in each row.
    for i in range(len(grid)):
        row = grid[i]
        limit = limits[i]
        
        # Get the largest 'limit' elements from the current row
        # nlargest is efficient for small limits, or sorting for larger ones.
        row_largest = heapq.nlargest(limit, row)
        candidates.extend(row_largest)
    
    # Now we have a pool of candidates. We want the largest k from this pool.
    # Sorting the candidates descending and taking the first k.
    candidates.sort(reverse=True)
    
    return sum(candidates[:k])
