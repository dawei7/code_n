def solve(root, p: int, q: int) -> int:
    parent = {root.val: None}
    depth = {root.val: 0}
    stack = [root]

    while stack:
        node = stack.pop()
        for child in (node.left, node.right):
            if child is not None:
                parent[child.val] = node.val
                depth[child.val] = depth[node.val] + 1
                stack.append(child)

    first, second = p, q
    distance = 0
    while depth[first] > depth[second]:
        first = parent[first]
        distance += 1
    while depth[second] > depth[first]:
        second = parent[second]
        distance += 1
    while first != second:
        first = parent[first]
        second = parent[second]
        distance += 2

    return distance
