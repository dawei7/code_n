# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class FindElements:
    def __init__(self, root: 'TreeNode'):
        self.values = set()
        root.val = 0
        stack = [root]
        while stack:
            node = stack.pop()
            self.values.add(node.val)
            if node.left is not None:
                node.left.val = 2 * node.val + 1
                stack.append(node.left)
            if node.right is not None:
                node.right.val = 2 * node.val + 2
                stack.append(node.right)

    def find(self, target: int) -> bool:
        return target in self.values
