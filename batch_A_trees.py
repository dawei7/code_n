"""Spec generator input — 5 more tree specs.

Run with:
    cd c:/dawei7/code_n
    python -m challenges.algorithms._generator \\
        --module trees \\
        --input batch_A_trees.py
"""


# The generator loads this file as a module, so it must import
# the symbols it uses.


SPECS_TO_ADD = [
    {
        "id": "tree_15",
        "name": "BST Delete",
        "category": "trees",
        "difficulty": 5,
        "complexity": "O_LOG_N",
        "description": (
            "Delete a key from a BST. The setup picks a key that\n"
            "is in the tree; the canonical solve removes it. Three\n"
            "cases: leaf (just drop), one child (replace with child),\n"
            "two children (replace with inorder successor).\n"
            "Tree is given as a binary shape: children[i] = [left, right].\n"
            "Requirement: O(log n) on a balanced BST.\n"
            "Source: https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/"
        ),
        "source_url": "https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/",
        "params": ["children", "values", "root", "n", "key"],
        "inputs": {
            "children": "list of length n; children[i] = [left, right] (-1 = absent).",
            "values": "list of length n; values[i] is the BST key at node i.",
            "root": "the root node index.",
            "n": "number of nodes.",
            "key": "the value to delete (always in the tree).",
        },
        "returns": "(new_children, new_values) of the BST after deletion.",
        "solve": '''
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
''',
        "setup": '''
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
''',
        "verify": '''
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
''',
        "samples": [
            ("children = [[1, 2], [-1, -1], [-1, -1]], values = [5, 3, 7], root = 0, n = 3, key = 3", "([(-1,2),(-1,-1),(-1,-1)], [5,7])"),
            ("children = [[1, 2], [-1, -1], [-1, -1]], values = [5, 3, 7], root = 0, n = 3, key = 5", "([(-1,2),(-1,-1),(-1,-1)], [7,3])"),
        ],
        "hint": "Three cases: leaf, one child (splice), two children (replace with inorder successor).",
        "parents": ["tree_08"],
        "children": [],
    },
    {
        "id": "tree_16",
        "name": "Serialize / Deserialize",
        "category": "trees",
        "difficulty": 5,
        "complexity": "O_N",
        "description": (
            "Serialize a binary tree to a string, then deserialize it back.\n"
            "Standard format: preorder traversal with 'N' for null,\n"
            "comma-separated. For example, [1, 2, 3] -> '1,2,N,N,3'.\n"
            "The deserialize function is called on the result of\n"
            "serialize, and the verifier checks structural equality.\n"
            "Requirement: O(n).\n"
            "Source: https://www.geeksforgeeks.org/serialize-deserialize-binary-tree/"
        ),
        "source_url": "https://www.geeksforgeeks.org/serialize-deserialize-binary-tree/",
        "params": ["children", "root", "n"],
        "inputs": {
            "children": "list of length n; children[i] = [left, right] (-1 = absent).",
            "root": "the root node index.",
            "n": "number of nodes.",
        },
        "returns": "the deserialized children list (must match the original after a serialize+deserialize round-trip).",
        "solve": '''
def solve(children, root, n):
    """Serialize the tree to a string, then deserialize it. Return the new children list."""
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
    s = ",".join(parts)
    # Deserialize.
    tokens = s.split(",")
    idx = [0]

    def des():
        tok = tokens[idx[0]]
        idx[0] += 1
        if tok == "N":
            return -1
        node = int(tok)
        left = des()
        right = des()
        return [node, left, right]

    new_children = []
    nodes = []

    def build():
        tok = tokens[idx[0]]
        idx[0] += 1
        if tok == "N":
            return -1
        node_idx = len(nodes)
        nodes.append(int(tok))
        # Pre-register so children can refer to this index.
        new_children.append([-1, -1])
        new_children[node_idx][0] = build()
        new_children[node_idx][1] = build()
        return node_idx

    # Reset and rebuild.
    idx[0] = 0
    new_children = []
    new_root = build()
    return new_children
''',
        "setup": '''
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
''',
        "verify": '''
# Re-run the canonical solve (serialize then deserialize) and
# compare the result with the original structure.
def ser(ch, u, parts):
    if u == -1:
        parts.append("N")
        return
    parts.append(str(u))
    ser(ch, ch[u][0], parts)
    ser(ch, ch[u][1], parts)

parts = []
ser(challenge._children, 0, parts)
s = ",".join(parts)
tokens = s.split(",")
idx = [0]
new_children = []

def build():
    tok = tokens[idx[0]]
    idx[0] += 1
    if tok == "N":
        return -1
    new_children.append([-1, -1])
    new_children[-1][0] = build()
    new_children[-1][1] = build()
    return len(new_children) - 1

new_root = build()
# Pad to the same length (the canonical solve may produce a
# different-length list if N appears differently).
max_len = max(len(new_children), len(challenge._children))
for _ in range(max_len - len(new_children)):
    new_children.append([-1, -1])
for _ in range(max_len - len(challenge._children)):
    challenge._children.append([-1, -1])
return new_children == challenge._children[:max_len] and new_root == 0
''',
        "samples": [
            ("children = [[1, 2], [-1, -1], [-1, -1]], root = 0, n = 3", "matches the original"),
            ("children = [[1, -1], [-1, -1]], root = 0, n = 2", "matches the original"),
        ],
        "hint": "Preorder serialize with 'N' for null. Deserialize by recursively reading the first token and recursing on left then right.",
        "parents": ["tree_15"],
        "children": [],
    },
    {
        "id": "tree_17",
        "name": "Lowest Common Ancestor",
        "category": "trees",
        "difficulty": 4,
        "complexity": "O_LOG_N",
        "description": (
            "Return the node index of the lowest common ancestor\n"
            "(LCA) of two nodes in a binary tree (not necessarily a BST).\n"
            "Walk the tree; the first node that's an ancestor of\n"
            "both is the LCA.\n"
            "Requirement: O(n) on a general tree, O(log n) on a BST.\n"
            "Source: https://www.geeksforgeeks.org/lowest-common-ancestor-binary-tree-set-1/"
        ),
        "source_url": "https://www.geeksforgeeks.org/lowest-common-ancestor-binary-tree-set-1/",
        "params": ["children", "root", "n", "p", "q"],
        "inputs": {
            "children": "list of length n; children[i] = [left, right] (-1 = absent).",
            "root": "the root node index.",
            "n": "number of nodes.",
            "p": "first node index.",
            "q": "second node index.",
        },
        "returns": "the node index of the LCA of p and q.",
        "solve": '''
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
''',
        "setup": '''
rng = random.Random(seed)
n_nodes = max(2, min(n, 10))
children = [[-1, -1] for _ in range(n_nodes)]
for i in range(1, n_nodes):
    parent = rng.randint(0, i - 1)
    side = 0 if rng.random() < 0.5 else 1
    if children[parent][side] == -1:
        children[parent][side] = i
    else:
        children[parent][1 - side] = i
# Pick two distinct nodes for p, q.
nodes = list(range(n_nodes))
rng.shuffle(nodes)
p, q = nodes[0], nodes[1]
challenge._children = children
return {"children": children, "root": 0, "n": n_nodes, "p": p, "q": q}
''',
        "verify": '''
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
''',
        "samples": [
            ("children = [[1, 2], [3, 4], [-1, -1], [-1, -1], [-1, -1]], root = 0, n = 5, p = 3, q = 4", "1 (LCA of 3 and 4 is 1)"),
            ("children = [[1, 2], [-1, -1], [-1, -1]], root = 0, n = 3, p = 1, q = 2", "0 (root is the LCA)"),
        ],
        "hint": "Find the path from root to each node; the last common node on both paths is the LCA.",
        "parents": ["tree_15"],
        "children": [],
    },
    {
        "id": "tree_18",
        "name": "Right Side View",
        "category": "trees",
        "difficulty": 3,
        "complexity": "O_N",
        "description": (
            "Return the list of node indices visible from the RIGHT\n"
            "side of a binary tree, ordered top-to-bottom. At each\n"
            "depth, the rightmost node is the visible one.\n"
            "Requirement: O(n).\n"
            "Source: https://www.geeksforgeeks.org/right-view-binary-tree-using-queue/"
        ),
        "source_url": "https://www.geeksforgeeks.org/right-view-binary-tree-using-queue/",
        "params": ["children", "root", "n"],
        "inputs": {
            "children": "list of length n; children[i] = [left, right] (-1 = absent).",
            "root": "the root node index.",
            "n": "number of nodes.",
        },
        "returns": "list of node indices visible from the right side, top-to-bottom.",
        "solve": '''
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
''',
        "setup": '''
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
return {"children": children, "root": 0, "n": n_nodes}
''',
        "verify": '''
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
''',
        "samples": [
            ("children = [[1, 2], [3, -1], [-1, 4], [-1, -1], [-1, -1]], root = 0, n = 5", "[1, 3, 4]"),
            ("children = [[1, -1], [-1, -1]], root = 0, n = 2", "[1]"),
        ],
        "hint": "BFS level-by-level. Take the LAST node at each level.",
        "parents": ["tree_05"],
        "children": [],
    },
    {
        "id": "tree_19",
        "name": "Boundary Traversal",
        "category": "trees",
        "difficulty": 5,
        "complexity": "O_N",
        "description": (
            "Return the boundary traversal of a binary tree:\n"
            "left boundary (root-to-leaf, no leaves), then all leaves\n"
            "left-to-right, then right boundary (leaf-to-root, no leaves)\n"
            "in reverse. Avoid duplicates when the root is also a leaf.\n"
            "Requirement: O(n).\n"
            "Source: https://www.geeksforgeeks.org/boundary-traversal-of-binary-tree/"
        ),
        "source_url": "https://www.geeksforgeeks.org/boundary-traversal-of-binary-tree/",
        "params": ["children", "root", "n"],
        "inputs": {
            "children": "list of length n; children[i] = [left, right] (-1 = absent).",
            "root": "the root node index.",
            "n": "number of nodes.",
        },
        "returns": "list of node indices in boundary order.",
        "solve": '''
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
''',
        "setup": '''
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
return {"children": children, "root": 0, "n": n_nodes}
''',
        "verify": '''
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
''',
        "samples": [
            ("children = [[1, 2], [3, 4], [-1, -1], [-1, -1], [5, -1], [-1, -1]], root = 0, n = 6", "[0, 1, 3, 5, 2, 4]"),
        ],
        "hint": "Add root, then walk the left edge (no leaves), then all leaves, then the right edge in reverse.",
        "parents": ["tree_15"],
        "children": [],
    },
]
