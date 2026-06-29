


def solve():
    class Solution:
        def __init__(self):
            self.first_node = None
            self.second_node = None
            self.prev_node = Node(float('-inf'))

        def traverse(self, root):
            if root is None:
                return

            self.traverse(root.left)

            if self.first_node is None and self.prev_node.val >= root.val:
                self.first_node = self.prev_node

            if self.first_node is not None and self.prev_node.val >= root.val:
                self.second_node = root

            self.prev_node = root

            self.traverse(root.right)

        def recoverBST(self, root):
            self.traverse(root)
            if self.first_node and self.second_node:
                self.first_node.val, self.second_node.val = self.second_node.val, self.first_node.val
            return root


if __name__ == "__main__":
    solve()
