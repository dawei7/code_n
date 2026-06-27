from typing import List

def solve(citations: List[int]) -> int:
    """
    Calculates the h-index of a researcher using a bucket sort approach.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    n = len(citations)
    buckets = [0] * (n + 1)
    
    # Count the frequency of citations, capping counts at n
    for c in citations:
        if c >= n:
            buckets[n] += 1
        else:
            buckets[c] += 1
            
    # Accumulate papers from highest citation count to lowest
    total_papers = 0
    for i in range(n, -1, -1):
        total_papers += buckets[i]
        if total_papers >= i:
            return i
            
    return 0
