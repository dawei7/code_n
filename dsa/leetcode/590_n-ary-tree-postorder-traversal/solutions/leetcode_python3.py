class Solution:
    def postorder(self, root: 'Node') -> list[int]:
        if root is None:
            return []

        reversed_postorder = []
        stack = [root]
        while stack:
            node = stack.pop()
            reversed_postorder.append(node.val)
            stack.extend(node.children)

        reversed_postorder.reverse()
        return reversed_postorder

