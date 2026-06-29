


def solve():
    '''
    class Node:
        def __init__(self, val):
            self.data = val
            self.left = None
            self.right = None
    '''

    class Solution:
        def inOrder(self, root):
            result = []

            # Nested helper function
            def inOrderTraversal(node):
                if node is None:
                    return

                inOrderTraversal(node.left)
                result.append(node.data)
                inOrderTraversal(node.right)

            # Start the traversal
            inOrderTraversal(root)

            return result


if __name__ == "__main__":
    solve()
