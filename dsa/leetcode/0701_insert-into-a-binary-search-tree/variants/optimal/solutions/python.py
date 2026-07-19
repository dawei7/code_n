class TreeNode:
    def __init__(self, val: int, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solve(root, val: int):
    if root is None:
        return TreeNode(val)

    current = root
    new_node = type(root)(val)

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
