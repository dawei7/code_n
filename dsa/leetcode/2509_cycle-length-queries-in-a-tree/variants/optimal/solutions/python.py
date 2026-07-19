from typing import List

def solve(n: int, queries: List[List[int]]) -> List[int]:
    """
    Calculates the cycle length for each query in a perfect binary tree.
    In a perfect binary tree where node i has children 2i and 2i+1,
    the parent of node i is i // 2.
    The distance between two nodes u and v is the number of edges on the 
    unique path between them. Adding an edge (u, v) creates a cycle of 
    length distance(u, v) + 1.
    """
    results = []
    
    for u, v in queries:
        dist = 0
        curr_u, curr_v = u, v
        
        # Move nodes up until they meet at the Lowest Common Ancestor (LCA)
        while curr_u != curr_v:
            if curr_u > curr_v:
                curr_u //= 2
            else:
                curr_v //= 2
            dist += 1
            
        # The cycle length is the path length + 1 (the new edge)
        results.append(dist + 1)
        
    return results
