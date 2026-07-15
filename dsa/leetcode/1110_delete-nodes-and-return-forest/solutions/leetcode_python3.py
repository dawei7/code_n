# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        deleted = set(to_delete)
        forest = []

        def dfs(node, is_root):
            if node is None:
                return None
            remove = node.val in deleted
            if is_root and not remove:
                forest.append(node)
            node.left = dfs(node.left, remove)
            node.right = dfs(node.right, remove)
            return None if remove else node

        dfs(root, True)
        return forest
