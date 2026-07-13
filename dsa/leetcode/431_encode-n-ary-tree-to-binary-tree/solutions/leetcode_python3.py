class Codec:
    def encode(self, root: 'Node') -> 'TreeNode':
        if root is None:
            return None
        binary = TreeNode(root.val)
        previous = None
        for child in root.children:
            encoded_child = self.encode(child)
            if previous is None:
                binary.left = encoded_child
            else:
                previous.right = encoded_child
            previous = encoded_child
        return binary

    def decode(self, data: 'TreeNode') -> 'Node':
        if data is None:
            return None
        children = []
        child = data.left
        while child is not None:
            children.append(self.decode(child))
            child = child.right
        return Node(data.val, children)
