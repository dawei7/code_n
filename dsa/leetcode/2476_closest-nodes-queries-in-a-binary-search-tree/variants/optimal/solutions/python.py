import bisect
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
    # Extract all values from the BST using in-order traversal
    # This results in a sorted list of values
    sorted_vals = []
    
    def inorder(node):
        if not node:
            return
        inorder(node.left)
        sorted_vals.append(node.val)
        inorder(node.right)
        
    inorder(root)
    
    results = []
    n = len(sorted_vals)
    
    for q in queries:
        # Find the ceiling: smallest value >= q
        # bisect_left returns the leftmost insertion point to maintain order
        idx_ceil = bisect.bisect_left(sorted_vals, q)
        
        # Find the floor: largest value <= q
        # bisect_right returns the rightmost insertion point
        idx_floor = bisect.bisect_right(sorted_vals, q)
        
        # Determine ceiling
        if idx_ceil < n:
            ceil = sorted_vals[idx_ceil]
        else:
            ceil = -1
            
        # Determine floor
        if idx_floor > 0:
            floor = sorted_vals[idx_floor - 1]
        else:
            floor = -1
            
        results.append([floor, ceil])
        
    return results
