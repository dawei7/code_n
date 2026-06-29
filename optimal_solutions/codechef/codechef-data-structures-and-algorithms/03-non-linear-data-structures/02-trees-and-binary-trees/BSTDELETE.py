# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None


def solve():
    def deleteNode(root, x):
        if root:
            if x < root.val:
                root.left = deleteNode(root.left, x)
            elif x > root.val:
                root.right = deleteNode(root.right, x)
            else:
                if root.left is None and root.right is None:
                    return None
                if root.left is None or root.right is None:
                    return root.left if root.left else root.right
                temp = root.right
                while temp.left is not None:
                    temp = temp.left
                root.val = temp.val
                root.right = deleteNode(root.right, temp.val)
        return root


if __name__ == "__main__":
    solve()
