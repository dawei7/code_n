class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if root is None:
            return None

        cloned_root = Node(root.val, [])
        stack = [(root, cloned_root)]

        while stack:
            original, cloned = stack.pop()
            for child in original.children:
                child_clone = Node(child.val, [])
                cloned.children.append(child_clone)
                stack.append((child, child_clone))

        return cloned_root

