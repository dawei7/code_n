"""
Description
-----------
Given n sorted keys with access probabilities probs[i],
build a BST that minimizes the expected search cost
sum(probs[i] * (depth(i) + 1)). DP: opt[i][j] = min cost
over BSTs containing keys[i..j]; try k in [i, j] as the
root. The cost of putting a subtree at depth+1 adds
the total probability of the subtree to the cost.
Source: https://www.geeksforgeeks.org/optimal-binary-search-tree-dp-24/

Examples
--------
Example 1:
Input:  keys = [10, 12, 20], probs = [0.1, 0.2, 0.7], n = 3
Output: 1.5 (root = 20)
"""

def solve(keys, probs, n):
    # Write your code here.
    return None
