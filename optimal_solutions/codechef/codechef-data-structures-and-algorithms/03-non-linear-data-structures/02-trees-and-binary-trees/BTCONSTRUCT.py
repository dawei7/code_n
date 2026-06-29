


def solve():
    class Solution:
        def construct_binary_tree(self, preorder, inorder):
            root_idx = [0]  # Use list to allow modification within nested function
            return self.build(preorder, inorder, root_idx, 0, len(inorder) - 1)

        def build(self, preorder, inorder, root_idx, left, right):
            if left > right:
                return None
            pivot = left  # Find the root from inorder
            while inorder[pivot] != preorder[root_idx[0]]:
                pivot += 1

            root_val = inorder[pivot]
            root_idx[0] += 1
            new_node = Node(root_val)
            new_node.left = self.build(preorder, inorder, root_idx, left, pivot - 1)
            new_node.right = self.build(preorder, inorder, root_idx, pivot + 1, right)
            return new_node


if __name__ == "__main__":
    solve()
