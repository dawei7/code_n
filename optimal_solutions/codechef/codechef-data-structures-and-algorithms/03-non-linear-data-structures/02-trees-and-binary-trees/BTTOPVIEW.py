


def solve():
    class Solution:
        @staticmethod
        def topView(root):
            if not root:
                return

            # Map to store the top view of the tree
            top_view = {}
            # Queue for level order traversal
            queue = deque([(root, 0)])

            while queue:
                node, hd = queue.popleft()

                if hd not in top_view:
                    top_view[hd] = node.val

                if node.left:
                    queue.append((node.left, hd - 1))
                if node.right:
                    queue.append((node.right, hd + 1))

            # Printing top view
            for key in sorted(top_view.keys()):
                print(top_view[key], end=" ")


if __name__ == "__main__":
    solve()
