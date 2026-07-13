class Solution:
    def insertIntoBST(self, root, val: int):
        if root is None:
            return TreeNode(val)

        current = root
        new_node = TreeNode(val)

        while True:
            if val < current.val:
                if current.left is None:
                    current.left = new_node
                    break
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    break
                current = current.right

        return root
