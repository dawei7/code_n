"""Solution for tree_16: Serialize / Deserialize.


            Serialize a binary tree to a string, then deserialize it back.
            Standard format: preorder traversal with 'N' for null,
            comma-separated. For example, [1, 2, 3] -> '1,2,N,N,3'.
            The deserialize function is called on the result of
            serialize, and the verifier checks structural equality.
            Requirement: O(n).
            Source: https://www.geeksforgeeks.org/serialize-deserialize-binary-tree/
            

Inputs passed to solve():
    children: list of length n; children[i] = [left, right] (-1 = absent).
    root: the root node index.
    n: number of nodes.

Goal:
    the deserialized children list (must match the original after a serialize+deserialize round-trip).

Samples:
Sample 1 input:  children = [[1, 2], [-1, -1], [-1, -1]], root = 0, n = 3
Sample 1 output: matches the original

Sample 2 input:  children = [[1, -1], [-1, -1]], root = 0, n = 2
Sample 2 output: matches the original


"""

def solve(children, root, n):
    # Write your code here.
    return None
