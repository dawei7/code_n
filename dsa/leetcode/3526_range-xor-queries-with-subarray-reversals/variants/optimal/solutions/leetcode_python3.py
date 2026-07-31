class Solution:
    def getResults(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        class Node:
            __slots__ = ("value", "priority", "size", "total", "reverse", "left", "right")

            def __init__(self, value, priority):
                self.value = value
                self.priority = priority
                self.size = 1
                self.total = value
                self.reverse = False
                self.left = None
                self.right = None

        random_state = 2463534242

        def next_priority():
            nonlocal random_state
            random_state ^= (random_state << 13) & 0xFFFFFFFF
            random_state ^= random_state >> 17
            random_state ^= (random_state << 5) & 0xFFFFFFFF
            random_state &= 0xFFFFFFFF
            return random_state

        def node_size(node):
            return node.size if node else 0

        def node_xor(node):
            return node.total if node else 0

        def pull(node):
            node.size = 1 + node_size(node.left) + node_size(node.right)
            node.total = node_xor(node.left) ^ node.value ^ node_xor(node.right)

        def apply_reverse(node):
            if node:
                node.left, node.right = node.right, node.left
                node.reverse = not node.reverse

        def push(node):
            if node.reverse:
                apply_reverse(node.left)
                apply_reverse(node.right)
                node.reverse = False

        def split(node, count):
            if not node:
                return None, None
            push(node)
            if node_size(node.left) >= count:
                first, node.left = split(node.left, count)
                pull(node)
                return first, node
            node.right, second = split(
                node.right, count - node_size(node.left) - 1
            )
            pull(node)
            return node, second

        def merge(left, right):
            if not left or not right:
                return left or right
            if left.priority > right.priority:
                push(left)
                left.right = merge(left.right, right)
                pull(left)
                return left
            push(right)
            right.left = merge(left, right.left)
            pull(right)
            return right

        root = None
        for value in nums:
            root = merge(root, Node(value, next_priority()))

        result = []
        for query_type, first, second in queries:
            if query_type == 1:
                before, rest = split(root, first)
                middle, after = split(rest, 1)
                middle.value = second
                pull(middle)
                root = merge(before, merge(middle, after))
                continue

            before, rest = split(root, first)
            middle, after = split(rest, second - first + 1)
            if query_type == 2:
                result.append(middle.total)
            else:
                apply_reverse(middle)
            root = merge(before, merge(middle, after))

        return result
