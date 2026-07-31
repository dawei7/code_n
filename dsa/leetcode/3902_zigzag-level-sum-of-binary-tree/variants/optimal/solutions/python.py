def solve(root) -> list[int]:
    if root is None:
        return []

    sums: list[int] = []
    nodes = [root]
    level_number = 1

    while nodes:
        total = 0
        if level_number % 2 == 1:
            for node in nodes:
                if node.left is None:
                    break
                total += node.val
        else:
            for node in reversed(nodes):
                if node.right is None:
                    break
                total += node.val
        sums.append(total)

        children = []
        for node in nodes:
            if node.left is not None:
                children.append(node.left)
            if node.right is not None:
                children.append(node.right)
        nodes = children
        level_number += 1

    return sums
