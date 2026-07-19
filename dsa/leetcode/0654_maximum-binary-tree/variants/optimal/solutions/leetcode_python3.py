class Solution:
    def constructMaximumBinaryTree(self, nums):
        stack = []
        for value in nums:
            node = TreeNode(value)
            while stack and stack[-1].val < value:
                node.left = stack.pop()
            if stack:
                stack[-1].right = node
            stack.append(node)
        return stack[0]
