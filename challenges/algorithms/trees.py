"""Tree traversal algorithms - the canonical pre/in/post-order,
height, and level-order walks.

Trees are passed as a list-of-lists: ``children[i]`` is the
list of node-i's children. This is a multi-way tree (each node
can have any number of children), which is the simplest shape
that lets the existing engine count reads. The setup function
builds a random tree rooted at the given root and stashes the
shape on the challenge for the verifier to re-derive the
expected traversals.

For an n-node tree, ``children`` is a list of length n. The root
is an integer in [0, n). Children are added breadth-first to
keep the shape roughly balanced.
"""

from __future__ import annotations

import random
from typing import Any, Optional

from challenges.spec import AlgorithmSpec, Sample
from code_n.counter import ComplexityClass


# === Shared setup / canonical walks ================================


def _build_tree(rng: random.Random, n: int) -> tuple[list[list[int]], int]:
    """Build a random tree with n nodes.

    Returns (children, root). The root is always 0 for
    determinism. Children are added breadth-first: each new
    node attaches as a child of a random earlier node.

    The shape is guaranteed to be a tree (no cycles): a node can
    only have a parent that's strictly less than its own index,
    so the resulting graph is acyclic and connected (because
    every new node has at least one parent).
    """
    n = max(1, n)
    children: list[list[int]] = [[] for _ in range(n)]
    for i in range(1, n):
        parent = rng.randint(0, i - 1)
        children[parent].append(i)
    return children, 0


def _preorder(children: list[list[int]], root: int) -> list[int]:
    out: list[int] = []

    def walk(u: int) -> None:
        out.append(u)
        for v in children[u]:
            walk(v)

    walk(root)
    return out


def _inorder(children: list[list[int]], root: int) -> list[int]:
    """For a multi-way tree, 'inorder' = children-left, node,
    children-right. We treat it as: visit the first child
    subtree, then the node, then each remaining child subtree
    left-to-right. This is the standard generalization."""
    out: list[int] = []

    def walk(u: int) -> None:
        if children[u]:
            walk(children[u][0])
        out.append(u)
        for v in children[u][1:]:
            walk(v)

    walk(root)
    return out


def _postorder(children: list[list[int]], root: int) -> list[int]:
    out: list[int] = []

    def walk(u: int) -> None:
        for v in children[u]:
            walk(v)
        out.append(u)

    walk(root)
    return out


def _height(children: list[list[int]], root: int) -> int:
    if not children[root]:
        return 0

    def depth(u: int) -> int:
        if not children[u]:
            return 0
        return 1 + max(depth(v) for v in children[u])

    return depth(root)


def _level_order(children: list[list[int]], root: int) -> list[list[int]]:
    levels: list[list[int]] = []
    queue: list[tuple[int, int]] = [(root, 0)]
    while queue:
        u, d = queue.pop(0)
        # Extend levels list to fit this depth.
        while len(levels) <= d:
            levels.append([])
        levels[d].append(u)
        for v in children[u]:
            queue.append((v, d + 1))
    return levels


# === Setup / verify shared by all 5 tree specs =====================


def _setup_tree(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    children, root = _build_tree(rng, n)
    challenge._children = children
    challenge._root = root
    challenge._n = max(1, n)
    return {"children": children, "root": root, "n": challenge._n}


def _verify_preorder(challenge, result: Any) -> bool:
    return isinstance(result, list) and result == _preorder(challenge._children, challenge._root)


def _verify_inorder(challenge, result: Any) -> bool:
    return isinstance(result, list) and result == _inorder(challenge._children, challenge._root)


def _verify_postorder(challenge, result: Any) -> bool:
    return isinstance(result, list) and result == _postorder(challenge._children, challenge._root)


def _verify_height(challenge, result: Any) -> bool:
    return isinstance(result, int) and result == _height(challenge._children, challenge._root)


def _verify_level_order(challenge, result: Any) -> bool:
    if not isinstance(result, list):
        return False
    expected = _level_order(challenge._children, challenge._root)
    if len(result) != len(expected):
        return False
    return all(got == exp for got, exp in zip(result, expected))


# === Source strings ================================================
#
# The canonical solve() for each tree walk. The student is
# expected to write their own version that the verifier will
# compare against the one derived from the test's children
# (which the verifier re-computes deterministically).


TREE_01_SOURCE = '''
def solve(children, root, n):
    """Preorder: root, then each child subtree left-to-right."""
    out = []

    def walk(u):
        out.append(u)
        for v in children[u]:
            walk(v)

    walk(root)
    return out
'''


TREE_02_SOURCE = '''
def solve(children, root, n):
    """Inorder: first-child subtree, node, then remaining children."""
    out = []

    def walk(u):
        if children[u]:
            walk(children[u][0])
        out.append(u)
        for v in children[u][1:]:
            walk(v)

    walk(root)
    return out
'''


TREE_03_SOURCE = '''
def solve(children, root, n):
    """Postorder: each child subtree left-to-right, then root."""
    out = []

    def walk(u):
        for v in children[u]:
            walk(v)
        out.append(u)

    walk(root)
    return out
'''


TREE_04_SOURCE = '''
def solve(children, root, n):
    """Tree height = max depth of any node. A leaf has height 0."""
    def depth(u):
        if not children[u]:
            return 0
        return 1 + max(depth(v) for v in children[u])
    return depth(root)
'''


TREE_05_SOURCE = '''
def solve(children, root, n):
    """Level-order: BFS, return rows by depth (root = depth 0)."""
    from collections import deque
    levels = []
    q = deque()
    q.append((root, 0))
    while q:
        u, d = q.popleft()
        while len(levels) <= d:
            levels.append([])
        levels[d].append(u)
        for v in children[u]:
            q.append((v, d + 1))
    return levels
'''


# === Spec list =====================================================


SPECS: list[AlgorithmSpec] = [
    AlgorithmSpec(
        id="tree_01",
        name="Preorder Traversal",
        category="trees",
        difficulty=3,
        required_complexity=ComplexityClass.O_N,
        description=(
            "Return the nodes of the tree in preorder:\n"
            "visit the node, then recursively visit each child\n"
            "subtree from left to right.\n"
            "The tree is given as children[i] = list of i's children.\n"
            "Requirement: O(n) where n is the number of nodes.\n"
            "Source: https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/"
        ),
        source_url="https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/",
        params=["children", "root", "n"],
        inputs={
            "children": "list of length n; children[i] is the list of i's children.",
            "root": "the root node index.",
            "n": "number of nodes in the tree.",
        },
        returns="a list of node indices in preorder.",
        source=TREE_01_SOURCE,
        setup_fn=_setup_tree,
        verify_fn=_verify_preorder,
        samples=[
            Sample("children = [[1, 2], [], []], root = 0, n = 3", "[0, 1, 2]"),
            Sample("children = [[1], [2], []], root = 0, n = 3", "[0, 1, 2]"),
            Sample("children = [[]], root = 0, n = 1", "[0]"),
        ],
        hint="Recurse: visit node, then recurse on each child left-to-right.",
        parents=["intro_01"],
        children=["tree_02", "tree_04"],
    ),
    AlgorithmSpec(
        id="tree_02",
        name="Inorder Traversal",
        category="trees",
        difficulty=3,
        required_complexity=ComplexityClass.O_N,
        description=(
            "Return the nodes of the tree in inorder (multi-way form):\n"
            "recurse on the first child subtree, then visit the\n"
            "node, then recurse on each remaining child subtree.\n"
            "Requirement: O(n).\n"
            "Source: https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/"
        ),
        source_url="https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/",
        params=["children", "root", "n"],
        inputs={
            "children": "list of length n; children[i] is the list of i's children.",
            "root": "the root node index.",
            "n": "number of nodes in the tree.",
        },
        returns="a list of node indices in inorder.",
        source=TREE_02_SOURCE,
        setup_fn=_setup_tree,
        verify_fn=_verify_inorder,
        samples=[
            Sample("children = [[1, 2], [], []], root = 0, n = 3", "[1, 0, 2]"),
            Sample("children = [[]], root = 0, n = 1", "[0]"),
        ],
        hint="For a multi-way tree, 'inorder' = first-child, node, remaining children.",
        parents=["tree_01"],
        children=["tree_03"],
    ),
    AlgorithmSpec(
        id="tree_03",
        name="Postorder Traversal",
        category="trees",
        difficulty=3,
        required_complexity=ComplexityClass.O_N,
        description=(
            "Return the nodes of the tree in postorder:\n"
            "recursively visit each child subtree left-to-right,\n"
            "then visit the node.\n"
            "Requirement: O(n).\n"
            "Source: https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/"
        ),
        source_url="https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/",
        params=["children", "root", "n"],
        inputs={
            "children": "list of length n; children[i] is the list of i's children.",
            "root": "the root node index.",
            "n": "number of nodes in the tree.",
        },
        returns="a list of node indices in postorder.",
        source=TREE_03_SOURCE,
        setup_fn=_setup_tree,
        verify_fn=_verify_postorder,
        samples=[
            Sample("children = [[1, 2], [], []], root = 0, n = 3", "[1, 2, 0]"),
            Sample("children = [[]], root = 0, n = 1", "[0]"),
        ],
        hint="Recurse on every child, then visit the node.",
        parents=["tree_02"],
        children=[],
    ),
    AlgorithmSpec(
        id="tree_04",
        name="Tree Height",
        category="trees",
        difficulty=2,
        required_complexity=ComplexityClass.O_N,
        description=(
            "Return the height of the tree: the maximum depth of\n"
            "any node, where a single-node tree has height 0 and\n"
            "each child level adds 1.\n"
            "Requirement: O(n).\n"
            "Source: https://www.geeksforgeeks.org/write-a-c-program-to-find-the-maximum-depth-or-height-of-a-tree/"
        ),
        source_url="https://www.geeksforgeeks.org/write-a-c-program-to-find-the-maximum-depth-or-height-of-a-tree/",
        params=["children", "root", "n"],
        inputs={
            "children": "list of length n; children[i] is the list of i's children.",
            "root": "the root node index.",
            "n": "number of nodes in the tree.",
        },
        returns="the height of the tree (a leaf alone is height 0).",
        source=TREE_04_SOURCE,
        setup_fn=_setup_tree,
        verify_fn=_verify_height,
        samples=[
            Sample("children = [[]], root = 0, n = 1", "0"),
            Sample("children = [[1], []], root = 0, n = 2", "1"),
            Sample("children = [[1], [2, 3], [], []], root = 0, n = 4", "2"),
        ],
        hint="Recurse: height(u) = 0 if leaf, else 1 + max(height(child) for child in u).",
        parents=["tree_01"],
        children=["tree_05"],
    ),
    AlgorithmSpec(
        id="tree_05",
        name="Level-Order Traversal",
        category="trees",
        difficulty=3,
        required_complexity=ComplexityClass.O_N,
        description=(
            "Return the nodes of the tree grouped by depth (BFS):\n"
            "a list of lists where the d-th inner list is the nodes\n"
            "at depth d. The root is at depth 0.\n"
            "Requirement: O(n).\n"
            "Source: https://www.geeksforgeeks.org/level-order-tree-traversal/"
        ),
        source_url="https://www.geeksforgeeks.org/level-order-tree-traversal/",
        params=["children", "root", "n"],
        inputs={
            "children": "list of length n; children[i] is the list of i's children.",
            "root": "the root node index.",
            "n": "number of nodes in the tree.",
        },
        returns="a list of lists — one inner list per depth, in BFS order.",
        source=TREE_05_SOURCE,
        setup_fn=_setup_tree,
        verify_fn=_verify_level_order,
        samples=[
            Sample("children = [[1, 2], [], []], root = 0, n = 3", "[[0], [1], [2]]"),
            Sample("children = [[1, 2], [3], [4], [], []], root = 0, n = 5", "[[0], [1, 2], [3, 4]]"),
            Sample("children = [[]], root = 0, n = 1", "[[0]]"),
        ],
        hint="Use a queue. Track each node's depth as you dequeue it.",
        parents=["tree_04"],
        children=[],
    ),
]
