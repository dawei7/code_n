class Node:
    """Local equivalent of LeetCode's Node for the standalone app template."""

    def __init__(
        self,
        val: bool,
        isLeaf: bool,
        topLeft: "Node | None" = None,
        topRight: "Node | None" = None,
        bottomLeft: "Node | None" = None,
        bottomRight: "Node | None" = None,
    ):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


def solve(quadTree1: Node, quadTree2: Node) -> Node:
    if quadTree1.isLeaf:
        return Node(True, True) if quadTree1.val else quadTree2
    if quadTree2.isLeaf:
        return Node(True, True) if quadTree2.val else quadTree1

    children = [
        solve(quadTree1.topLeft, quadTree2.topLeft),
        solve(quadTree1.topRight, quadTree2.topRight),
        solve(quadTree1.bottomLeft, quadTree2.bottomLeft),
        solve(quadTree1.bottomRight, quadTree2.bottomRight),
    ]

    if all(child.isLeaf and child.val == children[0].val for child in children):
        return Node(children[0].val, True)

    return Node(
        True,
        False,
        children[0],
        children[1],
        children[2],
        children[3],
    )
