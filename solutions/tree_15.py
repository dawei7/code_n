"""Solution for tree_15: BST Delete.


            Delete a key from a BST. The setup picks a key that
            is in the tree; the canonical solve removes it. Three
            cases: leaf (just drop), one child (replace with child),
            two children (replace with inorder successor).
            Tree is given as a binary shape: children[i] = [left, right].
            Requirement: O(log n) on a balanced BST.
            Source: https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/
            

Inputs passed to solve():
    children: list of length n; children[i] = [left, right] (-1 = absent).
    values: list of length n; values[i] is the BST key at node i.
    root: the root node index.
    n: number of nodes.
    key: the value to delete (always in the tree).

Goal:
    (new_children, new_values) of the BST after deletion.

Samples:
Sample 1 input:  children = [[1, 2], [-1, -1], [-1, -1]], values = [5, 3, 7], root = 0, n = 3, key = 3
Sample 1 output: ([(-1,2),(-1,-1),(-1,-1)], [5,7])

Sample 2 input:  children = [[1, 2], [-1, -1], [-1, -1]], values = [5, 3, 7], root = 0, n = 3, key = 5
Sample 2 output: ([(-1,2),(-1,-1),(-1,-1)], [7,3])


"""

def solve(children, values, root, n, key):
    # Write your code here.
    return None
