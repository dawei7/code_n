"""Spec generator input — 2 new tree specs.

Run with:
    cd c:/dawei7/code_n
    python -m challenges.algorithms._generator \\
        --module trees \\
        --input batch_2d_trees.py
"""


SPECS_TO_ADD = [
    {
        "id": "tree_11",
        "name": "Balanced Tree Check",
        "category": "trees",
        "difficulty": 3,
        "complexity": "O_N",
        "description": (
            "Return True iff the binary tree is height-balanced:\n"
            "for every node, the heights of its left and right\n"
            "subtrees differ by at most 1.\n"
            "Tree is given as a binary shape: children[i] = [left, right].\n"
            "Requirement: O(n).\n"
            "Source: https://www.geeksforgeeks.org/how-to-determine-if-a-binary-tree-is-balanced/"
        ),
        "source_url": "https://www.geeksforgeeks.org/how-to-determine-if-a-binary-tree-is-balanced/",
        "params": ["children", "root", "n"],
        "inputs": {
            "children": "list of length n; children[i] = [left, right] (-1 = absent).",
            "root": "the root node index.",
            "n": "number of nodes.",
        },
        "returns": "True iff the tree is height-balanced.",
        "solve": '''
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
''',
        "setup": '''
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
''',
        "verify": '''
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
''',
        "samples": [
            ("children = [[1, 2], [3, 4], [-1, -1], [-1, -1], [-1, -1]], root = 0, n = 5", "True"),
            ("children = [[1, -1], [-1, -1]], root = 0, n = 2", "True"),
            ("children = [[1, 2], [-1, -1], [3, -1], [-1, -1], [-1, -1]], root = 0, n = 5", "False"),
        ],
        "hint": "Recurse. For each node, if the two subtree heights differ by more than 1, the tree is unbalanced.",
        "parents": ["tree_04"],
        "children": ["tree_12"],
    },
    {
        "id": "tree_12",
        "name": "Symmetric Tree Check",
        "category": "trees",
        "difficulty": 3,
        "complexity": "O_N",
        "description": (
            "Return True iff the binary tree is symmetric around\n"
            "its center: the left subtree is the mirror of the right\n"
            "subtree.\n"
            "Tree is given as a binary shape: children[i] = [left, right].\n"
            "Requirement: O(n).\n"
            "Source: https://www.geeksforgeeks.org/symmetric-tree-tree-which-is-mirror-image-of-itself/"
        ),
        "source_url": "https://www.geeksforgeeks.org/symmetric-tree-tree-which-is-mirror-image-of-itself/",
        "params": ["children", "root", "n"],
        "inputs": {
            "children": "list of length n; children[i] = [left, right] (-1 = absent).",
            "root": "the root node index.",
            "n": "number of nodes.",
        },
        "returns": "True iff the tree is symmetric around its root.",
        "solve": '''
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
''',
        "setup": '''
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
''',
        "verify": '''
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
''',
        "samples": [
            ("children = [[1, 2], [3, 4], [4, 3], [-1, -1], [-1, -1]], root = 0, n = 5", "True"),
            ("children = [[1, -1], [-1, -1]], root = 0, n = 2", "True"),
            ("children = [[1, 2], [3, -1], [-1, -1]], root = 0, n = 3", "False"),
        ],
        "hint": "A tree is symmetric iff its left and right subtrees are mirrors of each other.",
        "parents": ["tree_11"],
        "children": [],
    },
]
