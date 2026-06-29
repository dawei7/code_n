


def solve():
    class Solution:
        def heightOfBinaryTree(self, root):
            # Base case
            if root is None:
                return -1

            # Recursively calculate left and right subtree heights
            left_height = self.heightOfBinaryTree(root.left)
            right_height = self.heightOfBinaryTree(root.right)

            # Return height of current node
            return 1 + max(left_height, right_height)

    def build_binary_tree(edges):
        nodes = {}
        children = set()

        for p, c, r in edges:
            if p not in nodes:
                nodes[p] = Node(p)

            if c not in nodes:
                nodes[c] = Node(c)

            if r == 'L':
                nodes[p].left = nodes[c]
            else:
                nodes[p].right = nodes[c]

            children.add(c)

        root = None
        for node in nodes:
            if node not in children:
                root = nodes[node]
                break

        return root

    def in_order(root, bt_nodes):
        if root is None:
            return

        in_order(root.left, bt_nodes)
        bt_nodes.append(root.val)
        in_order(root.right, bt_nodes)


if __name__ == "__main__":
    solve()
