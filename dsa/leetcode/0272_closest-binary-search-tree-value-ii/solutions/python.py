def solve(root, target: float, k: int) -> list[int]:
    predecessors = []
    successors = []
    node = root
    while node is not None:
        if node.val <= target:
            predecessors.append(node)
            node = node.right
        else:
            node = node.left
    node = root
    while node is not None:
        if node.val > target:
            successors.append(node)
            node = node.left
        else:
            node = node.right

    def previous() -> int:
        current = predecessors.pop()
        value = current.val
        current = current.left
        while current is not None:
            predecessors.append(current)
            current = current.right
        return value

    def following() -> int:
        current = successors.pop()
        value = current.val
        current = current.right
        while current is not None:
            successors.append(current)
            current = current.left
        return value

    closest = []
    for _ in range(k):
        if not successors or (
            predecessors
            and target - predecessors[-1].val <= successors[-1].val - target
        ):
            closest.append(previous())
        else:
            closest.append(following())
    return closest
