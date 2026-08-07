class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nodes = []
        stack = []
        current = root

        while current is not None or stack:
            while current is not None:
                stack.append(current)
                current = current.left
            current = stack.pop()
            nodes.append(current)
            current = current.right

        def build(left, right):
            if left > right:
                return None
            middle = (left + right) // 2
            node = nodes[middle]
            node.left = build(left, middle - 1)
            node.right = build(middle + 1, right)
            return node

        return build(0, len(nodes) - 1)
