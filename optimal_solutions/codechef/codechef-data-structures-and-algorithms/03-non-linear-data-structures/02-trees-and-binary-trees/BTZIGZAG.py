


def solve():
    class Solution:
        def zigzag_traversal(self, root):
            if not root:
                return

            result = []
            nodes_queue = [root]
            left_to_right = True

            while nodes_queue:
                size = len(nodes_queue)
                row = [0] * size

                for i in range(size):
                    node = nodes_queue.pop(0)
                    index = i if left_to_right else (size - 1 - i)
                    row[index] = node.val

                    if node.left:
                        nodes_queue.append(node.left)
                    if node.right:
                        nodes_queue.append(node.right)

                result.append(row)
                left_to_right = not left_to_right

            for level_nodes in result:
                print(" ".join(map(str, level_nodes)))


if __name__ == "__main__":
    solve()
