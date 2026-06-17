"""Solution for tree_10: Max Path Sum.

Return the maximum root-to-leaf path sum in a multi-way
tree. All values are non-negative. The path starts at
the root and ends at any leaf.
Requirement: O(n) — single DFS.
Source: https://www.geeksforgeeks.org/find-the-maximum-sum-path-in-a-binary-tree/

Inputs passed to solve():
    children: list of length n; children[i] is the list of i's children.
    values: list of non-negative integers at each node.
    root: the root node index.
    n: number of nodes in the tree.

Goal:
    the maximum sum along any root-to-leaf path.

Samples:
Sample 1 input:  children = [[1, 2], [3], [4], [], []], values = [1, 2, 3, 4, 5], root = 0, n = 5
Sample 1 output: 9 (1→2→4)

Sample 2 input:  children = [[]], values = [42], root = 0, n = 1
Sample 2 output: 42


"""

def solve(children, values, root, n):
    # Write your code here.
    return None
