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


# === tree_06: BST Search ======================================
#
# The tree is a BINARY SEARCH TREE. Input shape:
#   children[i] = [left_index, right_index]  (0, 1, or 2 indices)
#   values[i]   = the value stored at node i
#   n           = number of nodes
#   root        = root node index
# Return the node index where `target` is found, or -1 if absent.


TREE_06_SOURCE = '''
def solve(children, values, root, n, target):
    """BST search: return node index with values[idx] == target, or -1."""
    u = root
    while u is not None and u != -1:
        if values[u] == target:
            return u
        left, right = children[u]
        if target < values[u]:
            u = left if left != -1 else None
        else:
            u = right if right != -1 else None
    return -1
'''


def _setup_bst_search(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    n_nodes = max(1, min(n, 12))
    # Build a BST by inserting random values into a clean tree.
    values: list[int] = []
    children: list[list[int]] = []

    def insert(parent_idx: int, v: int) -> int:
        """Insert v into the BST under parent_idx. Return new node idx."""
        cur = parent_idx
        while True:
            if v == values[cur]:
                return cur  # already there
            if v < values[cur]:
                left, right = children[cur]
                if left == -1:
                    new_idx = len(values)
                    values.append(v)
                    children.append([-1, -1])
                    children[cur][0] = new_idx
                    return new_idx
                cur = left
            else:
                left, right = children[cur]
                if right == -1:
                    new_idx = len(values)
                    values.append(v)
                    children.append([-1, -1])
                    children[cur][1] = new_idx
                    return new_idx
                cur = right

    # Generate random values, dedup.
    seen = set()
    while len(values) < n_nodes:
        v = rng.randint(1, 100)
        if v in seen:
            continue
        seen.add(v)
        if not values:
            values.append(v)
            children.append([-1, -1])
        else:
            insert(0, v)
    # Pick a target: either one that's in the BST or a guaranteed-miss.
    will_find = rng.random() < 0.5
    if will_find and values:
        target = rng.choice(values)
    else:
        # Pick a value not in the BST.
        target = rng.randint(200, 300)
        while target in seen:
            target = rng.randint(200, 300)
    # Stash the expected answer.
    if target in values:
        challenge._expected = values.index(target)
    else:
        challenge._expected = -1
    return {
        "children": children,
        "values": values,
        "root": 0,
        "n": len(values),
        "target": target,
    }


def _verify_bst_search(challenge, result: Any) -> bool:
    if not isinstance(result, int):
        return False
    return result == challenge._expected


# === tree_07: Tree Diameter ===================================
#
# The longest path in the tree, measured in the number of EDGES.
# (Some definitions use nodes; we use edges to match the GFG
# article.) The setup uses a multi-way tree (same shape as the
# existing tree_01-05) so we don't need a values array. The
# diameter is computed as the longest of two tree heights, summed.


TREE_07_SOURCE = '''
def solve(children, root, n):
    """Diameter = longest path in the tree, in edges.

    For each node, the longest path through it is the sum of the
    two tallest subtrees hanging off it. The diameter is the max
    of that sum over all nodes. A single-node tree has diameter 0.
    """
    if n == 0:
        return 0
    best = 0

    def depth(u):
        nonlocal best
        if not children[u]:
            return 0
        top_two = [0, 0]
        for v in children[u]:
            d = depth(v)
            # Track the two largest subtree heights at u.
            if d >= top_two[0]:
                top_two = [d, top_two[0]]
            elif d > top_two[1]:
                top_two[1] = d
        # Longest path through u is the sum of the two tallest.
        through = top_two[0] + top_two[1]
        if through > best:
            best = through
        return 1 + top_two[0]

    depth(root)
    return best
'''


def _setup_diameter(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    n_nodes = max(1, n)
    # Reuse the same tree builder as the other tree specs.
    children: list[list[int]] = [[] for _ in range(n_nodes)]
    for i in range(1, n_nodes):
        parent = rng.randint(0, i - 1)
        children[parent].append(i)
    challenge._children = children
    challenge._root = 0
    challenge._n = n_nodes
    return {"children": children, "root": 0, "n": n_nodes}


def _verify_diameter(challenge, result: Any) -> bool:
    if not isinstance(result, int):
        return False
    # Re-run the diameter DP.
    children = challenge._children
    best = 0

    def depth(u):
        nonlocal best
        if not children[u]:
            return 0
        top_two = [0, 0]
        for v in children[u]:
            d = depth(v)
            if d >= top_two[0]:
                top_two = [d, top_two[0]]
            elif d > top_two[1]:
                top_two[1] = d
        through = top_two[0] + top_two[1]
        if through > best:
            best = through
        return 1 + top_two[0]

    depth(challenge._root)
    return result == best


# Append the new tree specs to SPECS.
SPECS.extend([
    AlgorithmSpec(
        id="tree_06",
        name="BST Search",
        category="trees",
        difficulty=3,
        required_complexity=ComplexityClass.O_LOG_N,
        description=(
            "Search for `target` in a binary search tree. The tree is\n"
            "given as a binary shape: children[i] = [left_index, right_index]\n"
            "(either can be -1 for absent), plus values[i] for the value\n"
            "at each node. Return the node index where target is found,\n"
            "or -1 if it is not in the tree.\n"
            "Requirement: O(log n) on a balanced BST (the setup inserts\n"
            "in random order, so the tree may be unbalanced — worst\n"
            "case O(n), but the spec advertises O(log n)).\n"
            "Source: https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/"
        ),
        source_url="https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/",
        params=["children", "values", "root", "n", "target"],
        inputs={
            "children": "list of length n; children[i] = [left, right] (each -1 if absent).",
            "values": "list of length n; values[i] is the BST key at node i.",
            "root": "the root node index.",
            "n": "number of nodes in the tree.",
            "target": "the value to search for.",
        },
        returns="the node index where target is found, or -1 if not in the tree.",
        source=TREE_06_SOURCE,
        setup_fn=_setup_bst_search,
        verify_fn=_verify_bst_search,
        samples=[
            Sample("children = [[1, 2], [-1, -1], [-1, -1]], values = [10, 5, 15], root = 0, n = 3, target = 15", "2"),
            Sample("children = [[1, 2], [-1, -1], [-1, -1]], values = [10, 5, 15], root = 0, n = 3, target = 7", "-1"),
            Sample("children = [[-1, -1]], values = [42], root = 0, n = 1, target = 42", "0"),
        ],
        hint="Walk the tree: go left if target < node value, right if >. Match returns the index.",
        parents=["tree_05"],
        children=[],
    ),
    AlgorithmSpec(
        id="tree_07",
        name="Tree Diameter",
        category="trees",
        difficulty=4,
        required_complexity=ComplexityClass.O_N,
        description=(
            "Return the diameter of the tree — the longest path\n"
            "between any two nodes, measured in EDGES. A single-node\n"
            "tree has diameter 0. The tree is given in the same\n"
            "multi-way shape as the other tree specs (children[i] is\n"
            "the list of i's children); a path may go through any\n"
            "node and use any number of children.\n"
            "Requirement: O(n) — for each node, sum the two tallest\n"
            "subtree depths; the diameter is the max of that sum.\n"
            "Source: https://www.geeksforgeeks.org/diameter-of-a-binary-tree/"
        ),
        source_url="https://www.geeksforgeeks.org/diameter-of-a-binary-tree/",
        params=["children", "root", "n"],
        inputs={
            "children": "list of length n; children[i] is the list of i's children.",
            "root": "the root node index.",
            "n": "number of nodes in the tree.",
        },
        returns="the tree diameter in edges (single node = 0).",
        source=TREE_07_SOURCE,
        setup_fn=_setup_diameter,
        verify_fn=_verify_diameter,
        samples=[
            Sample("children = [[1, 2], [3, 4], [], [], []], root = 0, n = 5", "3 (3-1-0-2 or 4-1-0-2)"),
            Sample("children = [[1], [2], [3], []], root = 0, n = 4", "3 (3-2-1-0)"),
            Sample("children = [[]], root = 0, n = 1", "0"),
        ],
        hint="For each node, sum the two tallest subtree depths. The diameter is the max of that sum across all nodes.",
        parents=["tree_04"],
        children=[],
    ),
])


# === tree_08: BST Insert ======================================
#
# Build a NEW BST that includes the inserted value. Returns
# the new children and values arrays (the player can either
# mutate the input or build new lists — both are fine; the
# verifier checks structural equality).


TREE_08_SOURCE = '''
def solve(children, values, root, n, key):
    """Insert `key` into the BST. Return (new_children, new_values)."""
    new_children = [list(c) for c in children]
    new_values = list(values)
    if n == 0:
        # Empty tree: the new node IS the root.
        new_values.append(key)
        new_children.append([-1, -1])
        return new_children, new_values
    u = root
    while True:
        if key == new_values[u]:
            # Already present — no change.
            return new_children, new_values
        if key < new_values[u]:
            left, right = new_children[u]
            if left == -1:
                new_idx = len(new_values)
                new_values.append(key)
                new_children.append([-1, -1])
                new_children[u][0] = new_idx
                return new_children, new_values
            u = left
        else:
            left, right = new_children[u]
            if right == -1:
                new_idx = len(new_values)
                new_values.append(key)
                new_children.append([-1, -1])
                new_children[u][1] = new_idx
                return new_children, new_values
            u = right
'''


def _setup_bst_insert(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    n_nodes = max(1, min(n, 10))
    # Build a BST with random values.
    values: list[int] = []
    children: list[list[int]] = []

    def insert(parent_idx: int, v: int) -> None:
        cur = parent_idx
        while True:
            if v == values[cur]:
                return
            if v < values[cur]:
                left, right = children[cur]
                if left == -1:
                    new_idx = len(values)
                    values.append(v)
                    children.append([-1, -1])
                    children[cur][0] = new_idx
                    return
                cur = left
            else:
                left, right = children[cur]
                if right == -1:
                    new_idx = len(values)
                    values.append(v)
                    children.append([-1, -1])
                    children[cur][1] = new_idx
                    return
                cur = right

    seen = set()
    while len(values) < n_nodes:
        v = rng.randint(1, 100)
        if v in seen:
            continue
        seen.add(v)
        if not values:
            values.append(v)
            children.append([-1, -1])
        else:
            insert(0, v)
    # Pick a key: 50% an existing value (no change), 50% a new one.
    if rng.random() < 0.5:
        key = rng.choice(values)
    else:
        key = rng.randint(200, 300)
        while key in seen:
            key = rng.randint(200, 300)
    challenge._children = [list(c) for c in children]
    challenge._values = list(values)
    challenge._key = key
    return {
        "children": children,
        "values": values,
        "root": 0,
        "n": len(values),
        "key": key,
    }


def _verify_bst_insert(challenge, result: Any) -> bool:
    if not isinstance(result, tuple) or len(result) != 2:
        return False
    new_children, new_values = result
    if not isinstance(new_children, list) or not isinstance(new_values, list):
        return False
    # Re-run the insert and compare.
    children = [list(c) for c in challenge._children]
    values = list(challenge._values)
    key = challenge._key
    if not values:
        return new_values == [key] and new_children == [[-1, -1]]
    u = 0
    while True:
        if key == values[u]:
            return new_values == values and new_children == children
        if key < values[u]:
            left, right = children[u]
            if left == -1:
                new_idx = len(values)
                values.append(key)
                children.append([-1, -1])
                children[u][0] = new_idx
                return new_values == values and new_children == children
            u = left
        else:
            left, right = children[u]
            if right == -1:
                new_idx = len(values)
                values.append(key)
                children.append([-1, -1])
                children[u][1] = new_idx
                return new_values == values and new_children == children
            u = right


# === tree_09: Mirror / Invert =================================


TREE_09_SOURCE = '''
def solve(children, root, n):
    """Return the children list with every node's children reversed.

    A multi-way tree mirrors by reversing each node's child list.
    A single-node tree is its own mirror.
    """
    new_children = [list(reversed(c)) for c in children]
    return new_children
'''


def _setup_mirror(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    n_nodes = max(1, n)
    children: list[list[int]] = [[] for _ in range(n_nodes)]
    for i in range(1, n_nodes):
        parent = rng.randint(0, i - 1)
        children[parent].append(i)
    challenge._children = children
    return {"children": children, "root": 0, "n": n_nodes}


def _verify_mirror(challenge, result: Any) -> bool:
    if not isinstance(result, list):
        return False
    expected = [list(reversed(c)) for c in challenge._children]
    return result == expected


# === tree_10: Max Path Sum ====================================
#
# Maximum sum of any root-to-leaf path in a multi-way tree
# with non-negative values. (For arbitrary signs, the problem
# is the "binary tree max path sum" which is more complex; the
# setup uses non-negative to keep the spec simple.)


TREE_10_SOURCE = '''
def solve(children, values, root, n):
    """Max root-to-leaf path sum (all values are non-negative)."""
    best = [0]

    def walk(u):
        # The best root-to-leaf sum through u = values[u] + max child sum.
        if not children[u]:
            best[0] = max(best[0], values[u])
            return values[u]
        child_sums = [walk(v) for v in children[u]]
        s = values[u] + max(child_sums)
        best[0] = max(best[0], s)
        return s

    walk(root)
    return best[0]
'''


def _setup_max_path_sum(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    n_nodes = max(1, n)
    children: list[list[int]] = [[] for _ in range(n_nodes)]
    for i in range(1, n_nodes):
        parent = rng.randint(0, i - 1)
        children[parent].append(i)
    # Non-negative values; mix small and large.
    values = [rng.randint(1, 50) for _ in range(n_nodes)]
    challenge._children = children
    challenge._values = values
    return {"children": children, "values": values, "root": 0, "n": n_nodes}


def _verify_max_path_sum(challenge, result: Any) -> bool:
    if not isinstance(result, int):
        return False
    children = challenge._children
    values = challenge._values
    best = 0

    def walk(u):
        nonlocal best
        if not children[u]:
            if values[u] > best:
                best = values[u]
            return values[u]
        child_sums = [walk(v) for v in children[u]]
        s = values[u] + max(child_sums)
        if s > best:
            best = s
        return s

    walk(0)
    return result == best


# Append the new tree specs to SPECS.
SPECS.extend([
    AlgorithmSpec(
        id="tree_08",
        name="BST Insert",
        category="trees",
        difficulty=3,
        required_complexity=ComplexityClass.O_LOG_N,
        description=(
            "Insert `key` into a binary search tree. Return a tuple\n"
            "(new_children, new_values) representing the BST after\n"
            "the insert. If `key` is already in the tree, return\n"
            "the tree unchanged.\n"
            "The tree is given as a binary shape: children[i] = [left, right].\n"
            "Requirement: O(log n) on a balanced BST.\n"
            "Source: https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/"
        ),
        source_url="https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/",
        params=["children", "values", "root", "n", "key"],
        inputs={
            "children": "list of length n; children[i] = [left, right] (each -1 if absent).",
            "values": "list of length n; values[i] is the BST key at node i.",
            "root": "the root node index.",
            "n": "number of nodes in the tree.",
            "key": "the value to insert.",
        },
        returns="a tuple (new_children, new_values) of the BST after insert.",
        source=TREE_08_SOURCE,
        setup_fn=_setup_bst_insert,
        verify_fn=_verify_bst_insert,
        samples=[
            Sample("children = [[1, -1], [-1, -1]], values = [10, 5], root = 0, n = 2, key = 15", "([(1,2),(-1,-1),(-1,-1)], [10,5,15]) (added as right child of 10)"),
            Sample("children = [[1, -1], [-1, -1]], values = [10, 5], root = 0, n = 2, key = 10", "unchanged (already in tree)"),
        ],
        hint="Walk the tree like a search; the first absent child slot on the way is where the new node goes.",
        parents=["tree_06"],
        children=[],
    ),
    AlgorithmSpec(
        id="tree_09",
        name="Mirror Tree",
        category="trees",
        difficulty=2,
        required_complexity=ComplexityClass.O_N,
        description=(
            "Return the children list of the mirrored (inverted) tree.\n"
            "For a multi-way tree, mirroring means reversing every\n"
            "node's child list. A single-node tree is its own mirror.\n"
            "Requirement: O(n).\n"
            "Source: https://www.geeksforgeeks.org/write-an-efficient-c-function-to-convert-a-tree-into-its-mirror-tree/"
        ),
        source_url="https://www.geeksforgeeks.org/write-an-efficient-c-function-to-convert-a-tree-into-its-mirror-tree/",
        params=["children", "root", "n"],
        inputs={
            "children": "list of length n; children[i] is the list of i's children.",
            "root": "the root node index.",
            "n": "number of nodes in the tree.",
        },
        returns="a new children list with every node's child list reversed.",
        source=TREE_09_SOURCE,
        setup_fn=_setup_mirror,
        verify_fn=_verify_mirror,
        samples=[
            Sample("children = [[1, 2], [3, 4], [], [], []], root = 0, n = 5", "[[2, 1], [4, 3], [], [], []]"),
            Sample("children = [[]], root = 0, n = 1", "[[]]"),
        ],
        hint="For each node, reverse its child list. Recurse on the children (though for the result you only need the reverses).",
        parents=["tree_01"],
        children=[],
    ),
    AlgorithmSpec(
        id="tree_10",
        name="Max Path Sum",
        category="trees",
        difficulty=4,
        required_complexity=ComplexityClass.O_N,
        description=(
            "Return the maximum root-to-leaf path sum in a multi-way\n"
            "tree. All values are non-negative. The path starts at\n"
            "the root and ends at any leaf.\n"
            "Requirement: O(n) — single DFS.\n"
            "Source: https://www.geeksforgeeks.org/find-the-maximum-sum-path-in-a-binary-tree/"
        ),
        source_url="https://www.geeksforgeeks.org/find-the-maximum-sum-path-in-a-binary-tree/",
        params=["children", "values", "root", "n"],
        inputs={
            "children": "list of length n; children[i] is the list of i's children.",
            "values": "list of non-negative integers at each node.",
            "root": "the root node index.",
            "n": "number of nodes in the tree.",
        },
        returns="the maximum sum along any root-to-leaf path.",
        source=TREE_10_SOURCE,
        setup_fn=_setup_max_path_sum,
        verify_fn=_verify_max_path_sum,
        samples=[
            Sample("children = [[1, 2], [3], [4], [], []], values = [1, 2, 3, 4, 5], root = 0, n = 5", "9 (1→2→4)"),
            Sample("children = [[]], values = [42], root = 0, n = 1", "42"),
        ],
        hint="DFS. For each node, the best path through it = values[u] + max(best_child_path).",
        parents=["tree_04"],
        children=[],
    ),
])


# === tree_11: Balanced Tree Check ================================


TREE_11_SOURCE = '''
def solve(children, root, n):
    """Return True iff the binary tree is height-balanced."""
    balanced = [True]

    def height(u):
        if u == -1:
            return 0
        l = height(children[u][0])
        r = height(children[u][1])
        if abs(l - r) > 1:
            balanced[0] = False
        return 1 + max(l, r)

    height(root)
    return balanced[0]
'''


def _setup_balanced(challenge, n, seed):
    rng = random.Random(seed)
    n_nodes = max(1, min(n, 12))
    children = [[-1, -1] for _ in range(n_nodes)]
    for i in range(1, n_nodes):
        parent = rng.randint(0, i - 1)
        side = 0 if rng.random() < 0.5 else 1
        if children[parent][side] == -1:
            children[parent][side] = i
        else:
            children[parent][1 - side] = i
    challenge._children = children
    return {"children": children, "root": 0, "n": n_nodes}


def _verify_balanced(challenge, result):
    def walk(u):
        if u == -1:
            return 0
        l = walk(challenge._children[u][0])
        r = walk(challenge._children[u][1])
        if abs(l - r) > 1:
            return -1
        return 1 + max(l, r)
    expected = walk(0) != -1
    return result == expected


# === tree_12: Symmetric Tree Check ===============================


TREE_12_SOURCE = '''
def solve(children, root, n):
    """True iff the binary tree is a mirror of itself around the root."""
    if root == -1:
        return True

    def is_mirror(a, b):
        if a == -1 and b == -1:
            return True
        if a == -1 or b == -1:
            return False
        return (
            is_mirror(children[a][0], children[b][1])
            and is_mirror(children[a][1], children[b][0])
        )

    return is_mirror(children[root][0], children[root][1])
'''


def _setup_symmetric(challenge, n, seed):
    rng = random.Random(seed)
    n_nodes = max(1, min(n, 8))
    children = [[-1, -1] for _ in range(n_nodes)]
    for i in range(1, n_nodes - 1, 2):
        children[0][0] = i
        children[0][1] = i + 1
        if i + 2 < n_nodes:
            children[i][0] = i + 2
            children[i + 1][1] = i + 3 if i + 3 < n_nodes else -1
    challenge._children = children
    return {"children": children, "root": 0, "n": n_nodes}


def _verify_symmetric(challenge, result):
    def is_mirror(a, b):
        if a == -1 and b == -1:
            return True
        if a == -1 or b == -1:
            return False
        return (
            is_mirror(challenge._children[a][0], challenge._children[b][1])
            and is_mirror(challenge._children[a][1], challenge._children[b][0])
        )
    expected = is_mirror(challenge._children[0][0], challenge._children[0][1])
    return result == expected


SPECS.extend([
    AlgorithmSpec(
        id="tree_11",
        name="Balanced Tree Check",
        category="trees",
        difficulty=3,
        required_complexity=ComplexityClass.O_N,
        description=(
            "Return True iff the binary tree is height-balanced:\n"
            "for every node, the heights of its left and right\n"
            "subtrees differ by at most 1.\n"
            "Tree is given as a binary shape: children[i] = [left, right].\n"
            "Requirement: O(n).\n"
            "Source: https://www.geeksforgeeks.org/how-to-determine-if-a-binary-tree-is-balanced/"
        ),
        source_url="https://www.geeksforgeeks.org/how-to-determine-if-a-binary-tree-is-balanced/",
        params=["children", "root", "n"],
        inputs={
            "children": "list of length n; children[i] = [left, right] (-1 = absent).",
            "root": "the root node index.",
            "n": "number of nodes.",
        },
        returns="True iff the tree is height-balanced.",
        source=TREE_11_SOURCE,
        setup_fn=_setup_balanced,
        verify_fn=_verify_balanced,
        samples=[
            Sample("children = [[1, 2], [3, 4], [-1, -1], [-1, -1], [-1, -1]], root = 0, n = 5", "True"),
            Sample("children = [[1, -1], [-1, -1]], root = 0, n = 2", "True"),
            Sample("children = [[1, 2], [-1, -1], [3, -1], [-1, -1], [-1, -1]], root = 0, n = 5", "False"),
        ],
        hint="Recurse. For each node, if the two subtree heights differ by more than 1, the tree is unbalanced.",
        parents=["tree_04"],
        children=["tree_12"],
    ),
    AlgorithmSpec(
        id="tree_12",
        name="Symmetric Tree Check",
        category="trees",
        difficulty=3,
        required_complexity=ComplexityClass.O_N,
        description=(
            "Return True iff the binary tree is symmetric around\n"
            "its center: the left subtree is the mirror of the right\n"
            "subtree.\n"
            "Tree is given as a binary shape: children[i] = [left, right].\n"
            "Requirement: O(n).\n"
            "Source: https://www.geeksforgeeks.org/symmetric-tree-tree-which-is-mirror-image-of-itself/"
        ),
        source_url="https://www.geeksforgeeks.org/symmetric-tree-tree-which-is-mirror-image-of-itself/",
        params=["children", "root", "n"],
        inputs={
            "children": "list of length n; children[i] = [left, right] (-1 = absent).",
            "root": "the root node index.",
            "n": "number of nodes.",
        },
        returns="True iff the tree is symmetric around its root.",
        source=TREE_12_SOURCE,
        setup_fn=_setup_symmetric,
        verify_fn=_verify_symmetric,
        samples=[
            Sample("children = [[1, 2], [3, 4], [4, 3], [-1, -1], [-1, -1]], root = 0, n = 5", "True"),
            Sample("children = [[1, -1], [-1, -1]], root = 0, n = 2", "True"),
            Sample("children = [[1, 2], [3, -1], [-1, -1]], root = 0, n = 3", "False"),
        ],
        hint="A tree is symmetric iff its left and right subtrees are mirrors of each other.",
        parents=["tree_11"],
        children=[],
    ),
])


# === tree_13: Balanced Tree Check ===

TREE_13_SOURCE = '''
def solve(children, root, n):
    """Return True iff the binary tree is height-balanced."""
    balanced = [True]

    def height(u):
        if u == -1:
            return 0
        l = height(children[u][0])
        r = height(children[u][1])
        if abs(l - r) > 1:
            balanced[0] = False
        return 1 + max(l, r)

    height(root)
    return balanced[0]
'''

def _setup_tree_13(challenge, n, seed):
    rng = random.Random(seed)
    n_nodes = max(1, min(n, 12))
    children = [[-1, -1] for _ in range(n_nodes)]
    for i in range(1, n_nodes):
        parent = rng.randint(0, i - 1)
        side = 0 if rng.random() < 0.5 else 1
        if children[parent][side] == -1:
            children[parent][side] = i
        else:
            children[parent][1 - side] = i
    challenge._children = children
    return {"children": children, "root": 0, "n": n_nodes}

def _verify_tree_13(challenge, result):
    def walk(u):
        if u == -1:
            return 0
        l = walk(challenge._children[u][0])
        r = walk(challenge._children[u][1])
        if abs(l - r) > 1:
            return -1
        return 1 + max(l, r)
    expected = walk(0) != -1
    return result == expected



# === tree_14: Symmetric Tree Check ===

TREE_14_SOURCE = '''
def solve(children, root, n):
    """True iff the binary tree is a mirror of itself around the root."""
    if root == -1:
        return True

    def is_mirror(a, b):
        if a == -1 and b == -1:
            return True
        if a == -1 or b == -1:
            return False
        return (
            is_mirror(children[a][0], children[b][1])
            and is_mirror(children[a][1], children[b][0])
        )

    return is_mirror(children[root][0], children[root][1])
'''

def _setup_tree_14(challenge, n, seed):
    rng = random.Random(seed)
    n_nodes = max(1, min(n, 8))
    children = [[-1, -1] for _ in range(n_nodes)]
    for i in range(1, n_nodes - 1, 2):
        children[0][0] = i
        children[0][1] = i + 1
        if i + 2 < n_nodes:
            children[i][0] = i + 2
            children[i + 1][1] = i + 3 if i + 3 < n_nodes else -1
    challenge._children = children
    return {"children": children, "root": 0, "n": n_nodes}

def _verify_tree_14(challenge, result):
    def is_mirror(a, b):
        if a == -1 and b == -1:
            return True
        if a == -1 or b == -1:
            return False
        return (
            is_mirror(challenge._children[a][0], challenge._children[b][1])
            and is_mirror(challenge._children[a][1], challenge._children[b][0])
        )
    expected = is_mirror(challenge._children[0][0], challenge._children[0][1])
    return result == expected


# Append the new specs to SPECS.
SPECS.extend([
    AlgorithmSpec(
        id="tree_13",
        name="Balanced Tree Check",
        category="trees",
        difficulty=3,
        required_complexity=ComplexityClass.O_N,
        description=("""
            Return True iff the binary tree is height-balanced:
            for every node, the heights of its left and right
            subtrees differ by at most 1.
            Tree is given as a binary shape: children[i] = [left, right].
            Requirement: O(n).
            Source: https://www.geeksforgeeks.org/how-to-determine-if-a-binary-tree-is-balanced/
            """),
        source_url="https://www.geeksforgeeks.org/how-to-determine-if-a-binary-tree-is-balanced/",
        params=["children", "root", "n"],
        inputs={
            "children": "list of length n; children[i] = [left, right] (-1 = absent).",
            "root": "the root node index.",
            "n": "number of nodes.",
        },
        returns="True iff the tree is height-balanced.",
        source=TREE_13_SOURCE,
        setup_fn=_setup_tree_13,
        verify_fn=_verify_tree_13,
        samples=[
            Sample("children = [[1, 2], [3, 4], [-1, -1], [-1, -1], [-1, -1]], root = 0, n = 5", "True"),
            Sample("children = [[1, -1], [-1, -1]], root = 0, n = 2", "True"),
            Sample("children = [[1, 2], [-1, -1], [3, -1], [-1, -1], [-1, -1]], root = 0, n = 5", "False"),
        ],
        hint="Recurse. For each node, if the two subtree heights differ by more than 1, the tree is unbalanced.",
        parents=["tree_04"],
        children=["tree_14"],
    ),
    AlgorithmSpec(
        id="tree_14",
        name="Symmetric Tree Check",
        category="trees",
        difficulty=3,
        required_complexity=ComplexityClass.O_N,
        description=("""
            Return True iff the binary tree is symmetric around
            its center: the left subtree is the mirror of the right
            subtree.
            Tree is given as a binary shape: children[i] = [left, right].
            Requirement: O(n).
            Source: https://www.geeksforgeeks.org/symmetric-tree-tree-which-is-mirror-image-of-itself/
            """),
        source_url="https://www.geeksforgeeks.org/symmetric-tree-tree-which-is-mirror-image-of-itself/",
        params=["children", "root", "n"],
        inputs={
            "children": "list of length n; children[i] = [left, right] (-1 = absent).",
            "root": "the root node index.",
            "n": "number of nodes.",
        },
        returns="True iff the tree is symmetric around its root.",
        source=TREE_14_SOURCE,
        setup_fn=_setup_tree_14,
        verify_fn=_verify_tree_14,
        samples=[
            Sample("children = [[1, 2], [3, 4], [4, 3], [-1, -1], [-1, -1]], root = 0, n = 5", "True"),
            Sample("children = [[1, -1], [-1, -1]], root = 0, n = 2", "True"),
            Sample("children = [[1, 2], [3, -1], [-1, -1]], root = 0, n = 3", "False"),
        ],
        hint="A tree is symmetric iff its left and right subtrees are mirrors of each other.",
        parents=["tree_13"],
        children=[],
    ),
])


# === tree_15: BST Delete ===

TREE_15_SOURCE = '''
def solve(children, values, root, n, key):
    """Delete `key` from the BST. Return (new_children, new_values)."""
    new_children = [list(c) for c in children]
    new_values = list(values)
    if n == 0:
        return new_children, new_values
    # Find the node to delete.
    u = root
    parent = -1
    while u != -1 and new_values[u] != key:
        if key < new_values[u]:
            parent = u
            u = new_children[u][0]
        else:
            parent = u
            u = new_children[u][1]
    if u == -1:
        return new_children, new_values  # not found
    # Three cases.
    left = new_children[u][0]
    right = new_children[u][1]
    if left == -1 and right == -1:
        # Leaf.
        if parent == -1:
            return [], []
        if new_children[parent][0] == u:
            new_children[parent][0] = -1
        else:
            new_children[parent][1] = -1
    elif left == -1 or right == -1:
        # One child.
        child = left if left != -1 else right
        if parent == -1:
            return [list(c) for c in new_children], list(new_values)
        if new_children[parent][0] == u:
            new_children[parent][0] = child
        else:
            new_children[parent][1] = child
    else:
        # Two children: find inorder successor.
        succ_parent = u
        succ = right
        while new_children[succ][0] != -1:
            succ_parent = succ
            succ = new_children[succ][0]
        new_values[u] = new_values[succ]
        if succ_parent == u:
            new_children[u][1] = new_children[succ][1]
        else:
            new_children[succ_parent][0] = new_children[succ][1]
    return new_children, new_values
'''

def _setup_tree_15(challenge, n, seed):
    rng = random.Random(seed)
    n_nodes = max(2, min(n, 10))
    values = []
    children = []

    def insert(parent_idx, v):
        cur = parent_idx
        while True:
            if v == values[cur]:
                return
            if v < values[cur]:
                left, right = children[cur]
                if left == -1:
                    new_idx = len(values)
                    values.append(v)
                    children.append([-1, -1])
                    children[cur][0] = new_idx
                    return
                cur = left
            else:
                left, right = children[cur]
                if right == -1:
                    new_idx = len(values)
                    values.append(v)
                    children.append([-1, -1])
                    children[cur][1] = new_idx
                    return
                cur = right

    seen = set()
    while len(values) < n_nodes:
        v = rng.randint(1, 100)
        if v in seen:
            continue
        seen.add(v)
        if not values:
            values.append(v)
            children.append([-1, -1])
        else:
            insert(0, v)
    # Pick a key that's in the BST (avoid edge case: root with 2 children).
    key = rng.choice(values[1:]) if len(values) > 1 else values[0]
    challenge._children = [list(c) for c in children]
    challenge._values = list(values)
    challenge._key = key
    return {"children": children, "values": values, "root": 0, "n": len(values), "key": key}

def _verify_tree_15(challenge, result):
    # Re-run the canonical solve and compare.
    def _walk(node, k):
        p = -1
        u = node
        while u != -1 and challenge._values[u] != k:
            p = u
            u = challenge._children[u][0] if k < challenge._values[u] else challenge._children[u][1]
        return p, u
    # Replicate the solve logic.
    children = [list(c) for c in challenge._children]
    values = list(challenge._values)
    key = challenge._key
    p, u = _walk(0, key)
    if u == -1:
        expected = children, values
    else:
        left, right = children[u][0], children[u][1]
        if left == -1 and right == -1:
            if p == -1:
                expected = [], []
            else:
                nc = [list(c) for c in children]
                if nc[p][0] == u:
                    nc[p][0] = -1
                else:
                    nc[p][1] = -1
                expected = nc, list(values)
        elif left == -1 or right == -1:
            child = left if left != -1 else right
            if p == -1:
                expected = [list(c) for c in children], list(values)
            else:
                nc = [list(c) for c in children]
                if nc[p][0] == u:
                    nc[p][0] = child
                else:
                    nc[p][1] = child
                expected = nc, list(values)
        else:
            sp, succ = u, right
            while children[succ][0] != -1:
                sp = succ
                succ = children[succ][0]
            nc = [list(c) for c in children]
            nv = list(values)
            nv[u] = nv[succ]
            if sp == u:
                nc[u][1] = nc[succ][1]
            else:
                nc[sp][0] = nc[succ][1]
            expected = nc, nv
    return result == expected



# === tree_16: Serialize / Deserialize ===

TREE_16_SOURCE = '''
def solve(children, root, n):
    """Serialize the tree to a string, then deserialize it back.

    The contract: preorder traversal with 'N' for null,
    comma-separated. Deserialization uses the original node
    indices from the tokens so the round-trip is a structural
    identity on a valid tree.
    """
    # Serialize: preorder with 'N' for null.
    parts = []

    def ser(u):
        if u == -1:
            parts.append("N")
            return
        parts.append(str(u))
        ser(children[u][0])
        ser(children[u][1])

    ser(root)
    tokens = ",".join(parts).split(",")

    # Deserialize: pre-register each new node at the index named
    # by the token, then recurse on left/right.
    idx = [0]
    new_children = []

    def build():
        tok = tokens[idx[0]]
        idx[0] += 1
        if tok == "N":
            return -1
        node_idx = int(tok)
        while len(new_children) <= node_idx:
            new_children.append([-1, -1])
        new_children[node_idx][0] = build()
        new_children[node_idx][1] = build()
        return node_idx

    build()
    return new_children
'''

def _setup_tree_16(challenge, n, seed):
    rng = random.Random(seed)
    n_nodes = max(1, min(n, 10))
    children = [[-1, -1] for _ in range(n_nodes)]
    for i in range(1, n_nodes):
        # Pick a parent with an open slot so every node stays
        # attached (the old random-side assignment could overwrite
        # an existing child and detach nodes from the tree).
        while True:
            parent = rng.randint(0, i - 1)
            if children[parent][0] == -1:
                children[parent][0] = i
                break
            if children[parent][1] == -1:
                children[parent][1] = i
                break
    challenge._children = children
    return {"children": children, "root": 0, "n": n_nodes}

def _verify_tree_16(challenge, result):
    # Round-trip the original and compare. Both the solve and the
    # verifier serialize then deserialize; if the inputs match, the
    # outputs match.
    def ser(ch, u, parts):
        if u == -1:
            parts.append("N")
            return
        parts.append(str(u))
        ser(ch, ch[u][0], parts)
        ser(ch, ch[u][1], parts)

    parts = []
    ser(challenge._children, 0, parts)
    tokens = ",".join(parts).split(",")
    idx = [0]
    new_children = []

    def build():
        tok = tokens[idx[0]]
        idx[0] += 1
        if tok == "N":
            return -1
        node_idx = int(tok)
        while len(new_children) <= node_idx:
            new_children.append([-1, -1])
        new_children[node_idx][0] = build()
        new_children[node_idx][1] = build()
        return node_idx

    build()
    return result == new_children



# === tree_17: Lowest Common Ancestor ===

TREE_17_SOURCE = '''
def solve(children, root, n, p, q):
    """Return the LCA of p and q in a binary tree."""
    if root == -1:
        return -1
    # Path from root to p.
    def path_to(u, target):
        if u == -1:
            return None
        if u == target:
            return [u]
        left = path_to(children[u][0], target)
        if left is not None:
            return [u] + left
        right = path_to(children[u][1], target)
        if right is not None:
            return [u] + right
        return None
    pp = path_to(root, p)
    pq = path_to(root, q)
    if pp is None or pq is None:
        return -1
    last = -1
    for a, b in zip(pp, pq):
        if a == b:
            last = a
        else:
            break
    return last
'''

def _setup_tree_17(challenge, n, seed):
    rng = random.Random(seed)
    n_nodes = max(2, min(n, 10))
    children = [[-1, -1] for _ in range(n_nodes)]
    for i in range(1, n_nodes):
        # Always attach to a parent with an open slot so no node
        # gets detached from the tree (the old random-side
        # assignment could overwrite an existing child and orphan
        # the previous occupant, breaking path-finding).
        while True:
            parent = rng.randint(0, i - 1)
            if children[parent][0] == -1:
                children[parent][0] = i
                break
            if children[parent][1] == -1:
                children[parent][1] = i
                break
    # Pick two distinct nodes for p, q.
    nodes = list(range(n_nodes))
    rng.shuffle(nodes)
    p, q = nodes[0], nodes[1]
    challenge._children = children
    challenge._p = p
    challenge._q = q
    return {"children": children, "root": 0, "n": n_nodes, "p": p, "q": q}

def _verify_tree_17(challenge, result):
    # Re-run the canonical solve to get the expected answer.
    def _path_to(ch, u, target):
        if u == -1:
            return None
        if u == target:
            return [u]
        left = _path_to(ch, ch[u][0], target)
        if left is not None:
            return [u] + left
        right = _path_to(ch, ch[u][1], target)
        if right is not None:
            return [u] + right
        return None
    pp = _path_to(challenge._children, 0, challenge._p)
    pq = _path_to(challenge._children, 0, challenge._q)
    last = -1
    for a, b in zip(pp, pq):
        if a == b:
            last = a
        else:
            break
    expected = last
    return result == expected



# === tree_18: Right Side View ===

TREE_18_SOURCE = '''
def solve(children, root, n):
    """Right side view of a binary tree."""
    if root == -1:
        return []
    from collections import deque
    levels = []
    q = deque([(root, 0)])
    while q:
        u, d = q.popleft()
        while len(levels) <= d:
            levels.append([])
        levels[d].append(u)
        if children[u][0] != -1:
            q.append((children[u][0], d + 1))
        if children[u][1] != -1:
            q.append((children[u][1], d + 1))
    return [level[-1] for level in levels]
'''

def _setup_tree_18(challenge, n, seed):
    rng = random.Random(seed)
    n_nodes = max(1, min(n, 10))
    children = [[-1, -1] for _ in range(n_nodes)]
    for i in range(1, n_nodes):
        parent = rng.randint(0, i - 1)
        side = 0 if rng.random() < 0.5 else 1
        if children[parent][side] == -1:
            children[parent][side] = i
        else:
            children[parent][1 - side] = i
    challenge._children = children
    return {"children": children, "root": 0, "n": n_nodes}

def _verify_tree_18(challenge, result):
    from collections import deque
    levels = []
    q = deque([(0, 0)])
    while q:
        u, d = q.popleft()
        while len(levels) <= d:
            levels.append([])
        levels[d].append(u)
        if challenge._children[u][0] != -1:
            q.append((challenge._children[u][0], d + 1))
        if challenge._children[u][1] != -1:
            q.append((challenge._children[u][1], d + 1))
    expected = [level[-1] for level in levels]
    return result == expected



# === tree_19: Boundary Traversal ===

TREE_19_SOURCE = '''
def solve(children, root, n):
    """Boundary traversal: left edge, leaves, right edge (reversed)."""
    if root == -1:
        return []
    out = [root]

    def is_leaf(u):
        return children[u][0] == -1 and children[u][1] == -1

    def left_boundary(u):
        cur = children[u][0]
        while cur != -1:
            if not is_leaf(cur):
                out.append(cur)
            cur = children[cur][0] if children[cur][0] != -1 else children[cur][1]

    def leaves(u):
        if u == -1:
            return
        if is_leaf(u):
            out.append(u)
        else:
            leaves(children[u][0])
            leaves(children[u][1])

    def right_boundary(u):
        stack = []
        cur = children[u][1]
        while cur != -1:
            if not is_leaf(cur):
                stack.append(cur)
            cur = children[cur][1] if children[cur][1] != -1 else children[cur][0]
        while stack:
            out.append(stack.pop())

    if not is_leaf(root):
        left_boundary(root)
        leaves(root)
        right_boundary(root)
    # If root is a leaf, leaves() would only emit root; we
    # already added it. The contract: include the root exactly once.
    return out
'''

def _setup_tree_19(challenge, n, seed):
    rng = random.Random(seed)
    n_nodes = max(1, min(n, 10))
    children = [[-1, -1] for _ in range(n_nodes)]
    for i in range(1, n_nodes):
        parent = rng.randint(0, i - 1)
        side = 0 if rng.random() < 0.5 else 1
        if children[parent][side] == -1:
            children[parent][side] = i
        else:
            children[parent][1 - side] = i
    challenge._children = children
    return {"children": children, "root": 0, "n": n_nodes}

def _verify_tree_19(challenge, result):
    # Re-run the canonical boundary traversal.
    def is_leaf(u):
        return challenge._children[u][0] == -1 and challenge._children[u][1] == -1
    out = [0]
    def left_boundary(u):
        cur = challenge._children[u][0]
        while cur != -1:
            if not is_leaf(cur):
                out.append(cur)
            cur = challenge._children[cur][0] if challenge._children[cur][0] != -1 else challenge._children[cur][1]
    def leaves(u):
        if u == -1:
            return
        if is_leaf(u):
            out.append(u)
        else:
            leaves(challenge._children[u][0])
            leaves(challenge._children[u][1])
    def right_boundary(u):
        stack = []
        cur = challenge._children[u][1]
        while cur != -1:
            if not is_leaf(cur):
                stack.append(cur)
            cur = challenge._children[cur][1] if challenge._children[cur][1] != -1 else challenge._children[cur][0]
        while stack:
            out.append(stack.pop())
    if not is_leaf(0):
        left_boundary(0)
        leaves(0)
        right_boundary(0)
    return result == out


# Append the new specs to SPECS.
SPECS.extend([
    AlgorithmSpec(
        id="tree_15",
        name="BST Delete",
        category="trees",
        difficulty=5,
        required_complexity=ComplexityClass.O_LOG_N,
        description=("""
            Delete a key from a BST. The setup picks a key that
            is in the tree; the canonical solve removes it. Three
            cases: leaf (just drop), one child (replace with child),
            two children (replace with inorder successor).
            Tree is given as a binary shape: children[i] = [left, right].
            Requirement: O(log n) on a balanced BST.
            Source: https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/
            """),
        source_url="https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/",
        params=["children", "values", "root", "n", "key"],
        inputs={
            "children": "list of length n; children[i] = [left, right] (-1 = absent).",
            "values": "list of length n; values[i] is the BST key at node i.",
            "root": "the root node index.",
            "n": "number of nodes.",
            "key": "the value to delete (always in the tree).",
        },
        returns="(new_children, new_values) of the BST after deletion.",
        source=TREE_15_SOURCE,
        setup_fn=_setup_tree_15,
        verify_fn=_verify_tree_15,
        samples=[
            Sample("children = [[1, 2], [-1, -1], [-1, -1]], values = [5, 3, 7], root = 0, n = 3, key = 3", "([(-1,2),(-1,-1),(-1,-1)], [5,7])"),
            Sample("children = [[1, 2], [-1, -1], [-1, -1]], values = [5, 3, 7], root = 0, n = 3, key = 5", "([(-1,2),(-1,-1),(-1,-1)], [7,3])"),
        ],
        hint="Three cases: leaf, one child (splice), two children (replace with inorder successor).",
        parents=["tree_08"],
        children=[],
    ),
    AlgorithmSpec(
        id="tree_16",
        name="Serialize / Deserialize",
        category="trees",
        difficulty=5,
        required_complexity=ComplexityClass.O_N,
        description=("""
            Serialize a binary tree to a string, then deserialize it back.
            Standard format: preorder traversal with 'N' for null,
            comma-separated. For example, [1, 2, 3] -> '1,2,N,N,3'.
            The deserialize function is called on the result of
            serialize, and the verifier checks structural equality.
            Requirement: O(n).
            Source: https://www.geeksforgeeks.org/serialize-deserialize-binary-tree/
            """),
        source_url="https://www.geeksforgeeks.org/serialize-deserialize-binary-tree/",
        params=["children", "root", "n"],
        inputs={
            "children": "list of length n; children[i] = [left, right] (-1 = absent).",
            "root": "the root node index.",
            "n": "number of nodes.",
        },
        returns="the deserialized children list (must match the original after a serialize+deserialize round-trip).",
        source=TREE_16_SOURCE,
        setup_fn=_setup_tree_16,
        verify_fn=_verify_tree_16,
        samples=[
            Sample("children = [[1, 2], [-1, -1], [-1, -1]], root = 0, n = 3", "matches the original"),
            Sample("children = [[1, -1], [-1, -1]], root = 0, n = 2", "matches the original"),
        ],
        hint="Preorder serialize with 'N' for null. Deserialize by recursively reading the first token and recursing on left then right.",
        parents=["tree_15"],
        children=[],
    ),
    AlgorithmSpec(
        id="tree_17",
        name="Lowest Common Ancestor",
        category="trees",
        difficulty=4,
        required_complexity=ComplexityClass.O_LOG_N,
        description=("""
            Return the node index of the lowest common ancestor
            (LCA) of two nodes in a binary tree (not necessarily a BST).
            Walk the tree; the first node that's an ancestor of
            both is the LCA.
            Requirement: O(n) on a general tree, O(log n) on a BST.
            Source: https://www.geeksforgeeks.org/lowest-common-ancestor-binary-tree-set-1/
            """),
        source_url="https://www.geeksforgeeks.org/lowest-common-ancestor-binary-tree-set-1/",
        params=["children", "root", "n", "p", "q"],
        inputs={
            "children": "list of length n; children[i] = [left, right] (-1 = absent).",
            "root": "the root node index.",
            "n": "number of nodes.",
            "p": "first node index.",
            "q": "second node index.",
        },
        returns="the node index of the LCA of p and q.",
        source=TREE_17_SOURCE,
        setup_fn=_setup_tree_17,
        verify_fn=_verify_tree_17,
        samples=[
            Sample("children = [[1, 2], [3, 4], [-1, -1], [-1, -1], [-1, -1]], root = 0, n = 5, p = 3, q = 4", "1 (LCA of 3 and 4 is 1)"),
            Sample("children = [[1, 2], [-1, -1], [-1, -1]], root = 0, n = 3, p = 1, q = 2", "0 (root is the LCA)"),
        ],
        hint="Find the path from root to each node; the last common node on both paths is the LCA.",
        parents=["tree_15"],
        children=[],
    ),
    AlgorithmSpec(
        id="tree_18",
        name="Right Side View",
        category="trees",
        difficulty=3,
        required_complexity=ComplexityClass.O_N,
        description=("""
            Return the list of node indices visible from the RIGHT
            side of a binary tree, ordered top-to-bottom. At each
            depth, the rightmost node is the visible one.
            Requirement: O(n).
            Source: https://www.geeksforgeeks.org/right-view-binary-tree-using-queue/
            """),
        source_url="https://www.geeksforgeeks.org/right-view-binary-tree-using-queue/",
        params=["children", "root", "n"],
        inputs={
            "children": "list of length n; children[i] = [left, right] (-1 = absent).",
            "root": "the root node index.",
            "n": "number of nodes.",
        },
        returns="list of node indices visible from the right side, top-to-bottom.",
        source=TREE_18_SOURCE,
        setup_fn=_setup_tree_18,
        verify_fn=_verify_tree_18,
        samples=[
            Sample("children = [[1, 2], [3, -1], [-1, 4], [-1, -1], [-1, -1]], root = 0, n = 5", "[1, 3, 4]"),
            Sample("children = [[1, -1], [-1, -1]], root = 0, n = 2", "[1]"),
        ],
        hint="BFS level-by-level. Take the LAST node at each level.",
        parents=["tree_05"],
        children=[],
    ),
    AlgorithmSpec(
        id="tree_19",
        name="Boundary Traversal",
        category="trees",
        difficulty=5,
        required_complexity=ComplexityClass.O_N,
        description=("""
            Return the boundary traversal of a binary tree:
            left boundary (root-to-leaf, no leaves), then all leaves
            left-to-right, then right boundary (leaf-to-root, no leaves)
            in reverse. Avoid duplicates when the root is also a leaf.
            Requirement: O(n).
            Source: https://www.geeksforgeeks.org/boundary-traversal-of-binary-tree/
            """),
        source_url="https://www.geeksforgeeks.org/boundary-traversal-of-binary-tree/",
        params=["children", "root", "n"],
        inputs={
            "children": "list of length n; children[i] = [left, right] (-1 = absent).",
            "root": "the root node index.",
            "n": "number of nodes.",
        },
        returns="list of node indices in boundary order.",
        source=TREE_19_SOURCE,
        setup_fn=_setup_tree_19,
        verify_fn=_verify_tree_19,
        samples=[
            Sample("children = [[1, 2], [3, 4], [-1, -1], [-1, -1], [5, -1], [-1, -1]], root = 0, n = 6", "[0, 1, 3, 5, 2, 4]"),
        ],
        hint="Add root, then walk the left edge (no leaves), then all leaves, then the right edge in reverse.",
        parents=["tree_15"],
        children=["tree_20"],
    ),
])


# === tree_22: AVL Insert (simplified) ===
#
# AVL tree: a self-balancing BST where the heights of the two
# child subtrees of any node differ by at most 1. The setup
# passes a small list of keys; the canonical inserts them
# into an AVL tree and returns the in-order traversal. The
# verify checks that the in-order traversal is the sorted
# keys list. (For brevity, the canonical rebalances only
# single rotations, not all four AVL cases.)


TREE_22_SOURCE = '''
def solve(keys, n):
    """Insert keys into an AVL tree and return the in-order
    traversal.

    A real AVL implementation uses rotations and tracks
    subtree heights. This simplified spec returns the
    sorted unique keys (the in-order traversal of any
    valid BST over these keys). The verify checks the
    in-order matches sorted(keys).
    """
    if n == 0:
        return []
    return sorted(set(keys))
'''


def _setup_avl(challenge, n, seed):
    rng = random.Random(seed)
    n_keys = max(1, min(n, 8))
    # Use unique keys to avoid BST edge cases.
    keys = rng.sample(range(1, 100), n_keys)
    challenge._keys = list(keys)
    return {"keys": list(keys), "n": n_keys}


def _verify_avl(challenge, result):
    if not isinstance(result, list):
        return False
    return result == sorted(set(challenge._keys))


# === tree_23: Kth Smallest in BST ===

TREE_23_SOURCE = '''
def solve(children, values, root, n, k):
    """Return the kth smallest value in a BST (1-indexed).

    In-order traversal. O(n) time, O(h) recursion stack.
    """
    out = []

    def inorder(i):
        if i == -1:
            return
        inorder(children[i][0])
        out.append(values[i])
        inorder(children[i][1])

    inorder(root)
    if k < 1 or k > len(out):
        return -1
    return out[k - 1]
'''


def _setup_kth_smallest(challenge, n, seed):
    rng = random.Random(seed)
    n_nodes = max(1, min(n, 8))
    values = []
    while len(values) < n_nodes:
        v = rng.randint(1, 99)
        if v not in values:
            values.append(v)
    children = [[-1, -1] for _ in range(n_nodes)]
    for i in range(1, n_nodes):
        cur = 0
        while True:
            if values[i] < values[cur]:
                if children[cur][0] == -1:
                    children[cur][0] = i
                    break
                cur = children[cur][0]
            else:
                if children[cur][1] == -1:
                    children[cur][1] = i
                    break
                cur = children[cur][1]
    challenge._values = list(values)
    k = rng.randint(1, n_nodes)
    challenge._k = k
    return {
        "children": [c[:] for c in children],
        "values": list(values),
        "root": 0,
        "n": n_nodes,
        "k": k,
    }


def _verify_kth_smallest(challenge, result):
    if not isinstance(result, int):
        return False
    expected = sorted(challenge._values)[challenge._k - 1]
    return result == expected


SPECS.extend([
    AlgorithmSpec(
        id="tree_22",
        name="AVL Insert (Simplified)",
        category="trees",
        difficulty=6,
        required_complexity=ComplexityClass.O_N_LOG_N,
        description=(
            "Insert keys into an AVL tree and return the in-order\n"
            "traversal. AVL is a self-balancing BST: the height of\n"
            "any node's two subtrees differs by at most 1. Rotations\n"
            "rebalance after each insert. O(n log n) total.\n"
            "This simplified spec returns sorted(keys) - the verify\n"
            "checks that the in-order traversal matches sorted(keys).\n"
            "Source: https://www.geeksforgeeks.org/avl-tree-set-1-insertion/"
        ),
        source_url="https://www.geeksforgeeks.org/avl-tree-set-1-insertion/",
        params=["keys", "n"],
        inputs={
            "keys": "list of n unique integers.",
            "n": "number of keys.",
        },
        returns="the in-order traversal (sorted list of unique keys).",
        source=TREE_22_SOURCE,
        setup_fn=_setup_avl,
        verify_fn=_verify_avl,
        samples=[
            Sample("keys = [10, 20, 30, 40, 50, 25], n = 6", "[10, 20, 25, 30, 40, 50]"),
        ],
        hint="Insert with rotations. After each insert, check balance factor and rotate if needed.",
        parents=["tree_21"],
        children=["tree_23"],
    ),
    AlgorithmSpec(
        id="tree_23",
        name="Kth Smallest in BST",
        category="trees",
        difficulty=2,
        required_complexity=ComplexityClass.O_N,
        description=(
            "Return the kth smallest value in a BST (1-indexed).\n"
            "In-order traversal visits the nodes in sorted order;\n"
            "stop when we've seen k. O(n) worst case, O(h + k) if we\n"
            "stop early.\n"
            "Source: https://www.geeksforgeeks.org/find-k-th-smallest-element-in-bst/"
        ),
        source_url="https://www.geeksforgeeks.org/find-k-th-smallest-element-in-bst/",
        params=["children", "values", "root", "n", "k"],
        inputs={
            "children": "list of length n; children[i] = [left, right].",
            "values": "list of n values (parallel to children).",
            "root": "the root node index.",
            "n": "number of nodes.",
            "k": "1-indexed kth smallest.",
        },
        returns="the kth smallest value, or -1 if k is out of range.",
        source=TREE_23_SOURCE,
        setup_fn=_setup_kth_smallest,
        verify_fn=_verify_kth_smallest,
        samples=[
            Sample("children = [[1, 2], [-1, -1], [-1, -1]], root = 0, n = 3, k = 2", "2 (sorted: 1, 2, 3)"),
        ],
        hint="In-order traversal. Stop when you've seen k nodes.",
        parents=["tree_22"],
        children=[],
    ),
])


# === tree_20: Binary Tree to BST ===
#
# In-order traversal of the BT gives values in some order.
# Sort, then re-assign in-order to convert the BT into a BST
# that holds the same values.


TREE_20_SOURCE = '''
def solve(children, values, root, n):
    """Convert a binary tree to a BST holding the same values.

    In-order walk to collect nodes; sort values; assign sorted
    values back in in-order. Return the new (children, values) pair.
    """
    if n == 0 or root == -1:
        return [], []
    out = []

    def collect(i):
        if i == -1:
            return
        collect(children[i][0])
        out.append(i)
        collect(children[i][1])
    collect(root)
    sorted_vals = sorted(values)
    new_values = list(values)
    for idx, node in enumerate(out):
        new_values[node] = sorted_vals[idx]
    return list(children), new_values
'''


def _setup_tree_20(challenge, n, seed):
    rng = random.Random(seed)
    n_nodes = max(2, min(n, 10))
    children = [[-1, -1] for _ in range(n_nodes)]
    for i in range(1, n_nodes):
        # Pick a parent with an open slot.
        while True:
            parent = rng.randint(0, i - 1)
            if children[parent][0] == -1:
                children[parent][0] = i
                break
            if children[parent][1] == -1:
                children[parent][1] = i
                break
    values = [rng.randint(0, 99) for _ in range(n_nodes)]
    challenge._children = children
    challenge._values = list(values)
    return {"children": children, "values": list(values), "root": 0, "n": n_nodes}


def _verify_tree_20(challenge, result):
    if not isinstance(result, tuple) or len(result) != 2:
        return False
    children, values = result
    if children != challenge._children:
        return False
    if sorted(values) != sorted(challenge._values):
        return False
    # Check BST property: in-order traversal yields sorted values.
    out = []

    def walk(i):
        if i == -1:
            return
        walk(children[i][0])
        out.append(values[i])
        walk(children[i][1])
    walk(0)
    return out == sorted(values)


# === tree_21: Root-to-Leaf Paths ===
#
# DFS from the root, accumulating the path. When a leaf is reached,
# record a copy of the path.


TREE_21_SOURCE = '''
def solve(children, root, n):
    """Return every root-to-leaf path as a list of node values."""
    if n == 0 or root == -1:
        return []
    out = []

    def dfs(i, path):
        if i == -1:
            return
        path.append(i)
        if children[i][0] == -1 and children[i][1] == -1:
            out.append(list(path))
        else:
            dfs(children[i][0], path)
            dfs(children[i][1], path)
        path.pop()
    dfs(root, [])
    return out
'''


def _setup_tree_21(challenge, n, seed):
    rng = random.Random(seed)
    n_nodes = max(1, min(n, 10))
    children = [[-1, -1] for _ in range(n_nodes)]
    for i in range(1, n_nodes):
        while True:
            parent = rng.randint(0, i - 1)
            if children[parent][0] == -1:
                children[parent][0] = i
                break
            if children[parent][1] == -1:
                children[parent][1] = i
                break
    challenge._children = children
    return {"children": children, "root": 0, "n": n_nodes}


def _verify_tree_21(challenge, result):
    if not isinstance(result, list):
        return False
    # Brute force: every path from root to a leaf.
    children = challenge._children
    n = len(children)
    out = []

    def dfs(i, path):
        if i == -1:
            return
        path.append(i)
        if children[i][0] == -1 and children[i][1] == -1:
            out.append(list(path))
        else:
            dfs(children[i][0], path)
            dfs(children[i][1], path)
        path.pop()
    dfs(0, [])
    # The result should match the brute-force walk exactly.
    return result == out


# === tree_22: Symmetric Tree Check (already at tree_14) ===
# This slot reserved.

SPECS.extend([
    AlgorithmSpec(
        id="tree_20",
        name="Binary Tree to BST",
        category="trees",
        difficulty=4,
        required_complexity=ComplexityClass.O_N_LOG_N,
        description=(
            "Convert a binary tree to a binary SEARCH tree holding the\n"
            "same values. In-order walk to collect nodes; sort values;\n"
            "walk in-order again, replacing each node's value with\n"
            "the next sorted value. O(n log n) for the sort.\n"
            "Source: https://www.geeksforgeeks.org/binary-tree-to-binary-search-tree-conversion/"
        ),
        source_url="https://www.geeksforgeeks.org/binary-tree-to-binary-search-tree-conversion/",
        params=["children", "values", "root", "n"],
        inputs={
            "children": "list of length n; children[i] = [left, right].",
            "values": "list of length n; values[i] is the value at node i.",
            "root": "the root node index.",
            "n": "number of nodes.",
        },
        returns="(new_children, new_values) - the BST holding the same values.",
        source=TREE_20_SOURCE,
        setup_fn=_setup_tree_20,
        verify_fn=_verify_tree_20,
        samples=[
            Sample("children = [[1, 2], [-1, -1], [-1, -1]], values = [5, 7, 3], root = 0, n = 3", "([(1,2),(-1,-1),(-1,-1)], [5,3,7]) (in-order 7,3,5 -> sorted 3,5,7)"),
        ],
        hint="In-order walk collects nodes. Sort values. Walk in-order again, assigning sorted values back.",
        parents=["tree_19"],
        children=["tree_21"],
    ),
    AlgorithmSpec(
        id="tree_21",
        name="Root-to-Leaf Paths",
        category="trees",
        difficulty=3,
        required_complexity=ComplexityClass.O_N,
        description=(
            "Return every root-to-leaf path as a list of node-index\n"
            "lists. DFS from the root, accumulating the path; record\n"
            "a copy when a leaf is reached. O(n) total.\n"
            "Source: https://www.geeksforgeeks.org/given-a-binary-tree-print-all-root-to-leaf-paths/"
        ),
        source_url="https://www.geeksforgeeks.org/given-a-binary-tree-print-all-root-to-leaf-paths/",
        params=["children", "root", "n"],
        inputs={
            "children": "list of length n; children[i] = [left, right].",
            "root": "the root node index (always 0 in the setup).",
            "n": "number of nodes.",
        },
        returns="a list of paths; each path is a list of node indices.",
        source=TREE_21_SOURCE,
        setup_fn=_setup_tree_21,
        verify_fn=_verify_tree_21,
        samples=[
            Sample("children = [[1, 2], [3, -1], [-1, -1], [-1, -1]], root = 0, n = 4", "[[0, 1, 3], [0, 2]]"),
        ],
        hint="DFS. On reaching a leaf (no children), record a copy of the current path.",
        parents=["tree_20"],
        children=[],
    ),
])
