# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None


def solve():
    def in_order(root, nodes):
        if root is None:
            return
        in_order(root.left, nodes)
        nodes.append(root.val)
        in_order(root.right, nodes)

    class Solution:
        def kth_largest_node(self, root, k):
            nodes = []
            in_order(root, nodes)
            if k > len(nodes):
                raise ValueError("k is out of bounds")
            return nodes[-k]


if __name__ == "__main__":
    solve()
