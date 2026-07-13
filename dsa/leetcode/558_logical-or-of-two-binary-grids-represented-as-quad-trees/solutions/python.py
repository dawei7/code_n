"""Recursive quad-tree OR with leaf short-circuiting for LeetCode 558."""

from types import SimpleNamespace


def solve(quadTree1, quadTree2):
    def make_leaf(value: bool):
        return SimpleNamespace(
            val=bool(value),
            isLeaf=True,
            topLeft=None,
            topRight=None,
            bottomLeft=None,
            bottomRight=None,
        )

    def combine(first, second):
        if first.isLeaf:
            return make_leaf(True) if first.val else second
        if second.isLeaf:
            return make_leaf(True) if second.val else first

        children = [
            combine(first.topLeft, second.topLeft),
            combine(first.topRight, second.topRight),
            combine(first.bottomLeft, second.bottomLeft),
            combine(first.bottomRight, second.bottomRight),
        ]

        if all(
            child.isLeaf and child.val == children[0].val
            for child in children
        ):
            return make_leaf(children[0].val)

        return SimpleNamespace(
            val=True,
            isLeaf=False,
            topLeft=children[0],
            topRight=children[1],
            bottomLeft=children[2],
            bottomRight=children[3],
        )

    return combine(quadTree1, quadTree2)

