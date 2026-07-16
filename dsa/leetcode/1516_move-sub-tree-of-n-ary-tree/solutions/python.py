"""Optimal app-local solution for LeetCode 1516."""

from collections import deque


def solve(tree, p, q):
    """Move the subtree rooted at value p below value q and serialize the result."""
    children = {value: list(child_values) for value, child_values in tree}
    parent = {}

    for value, child_values in children.items():
        for child in child_values:
            parent[child] = value

    root = next(value for value in children if value not in parent)
    p_parent = parent.get(p)

    if p_parent == q:
        return _level_order_records(root, children)

    current = q
    q_is_below_p = False
    while current in parent:
        if current == p:
            q_is_below_p = True
            break
        current = parent[current]
    if current == p:
        q_is_below_p = True

    if q_is_below_p:
        q_parent = parent[q]
        children[q_parent].remove(q)
        if p_parent is None:
            root = q
        else:
            p_index = children[p_parent].index(p)
            children[p_parent][p_index] = q
    else:
        children[p_parent].remove(p)

    children[q].append(p)
    return _level_order_records(root, children)


def _level_order_records(root, children):
    records = []
    queue = deque([root])
    while queue:
        value = queue.popleft()
        child_values = children[value]
        records.append([value, child_values])
        queue.extend(child_values)
    return records
