# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None
from collections import deque


def solve():
    class Solution:
        def level_order_traversal(self, root):
            if root is None:
             return []

            result = []
            node_queue = deque([root])

            while node_queue:
                level_size = len(node_queue)
                level_values = []

                for _ in range(level_size):
                    node = node_queue.popleft()
                    level_values.append(node.val)

                    if node.left is not None:
                        node_queue.append(node.left)
                    if node.right is not None:
                        node_queue.append(node.right)

                result.append(level_values)

            for level_nodes in result:
                print(' '.join(map(str, level_nodes)))

            return result


if __name__ == "__main__":
    solve()
