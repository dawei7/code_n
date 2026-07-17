def solve(root, fromNode: int, toNode: int):
    source = None
    target = None
    stack = [root]
    while stack:
        node = stack.pop()
        if node is None:
            continue
        if node.val == fromNode:
            source = node
        if node.val == toNode:
            target = node
        stack.append(node.left)
        stack.append(node.right)

    source.right = target
    seen = set()

    def repair(node):
        if node is None:
            return None
        if node.right in seen:
            return None
        seen.add(node)
        node.right = repair(node.right)
        node.left = repair(node.left)
        return node

    return repair(root)
