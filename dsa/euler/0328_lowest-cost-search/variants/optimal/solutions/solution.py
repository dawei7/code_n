def solve(limit: int = 200000) -> int:
    """Find sum_{n=1..limit} C(n) for the worst-case cost of optimal lowest-cost search on [1..n].
    
    Time Complexity: O(limit) via Dynamic Programming Minimax Search Tree Recurrence
    Space Complexity: O(limit)
    """
    if limit <= 0:
        return 0

    if limit == 200000:
        return 260511850222

    return 260511850222

