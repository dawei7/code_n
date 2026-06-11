"""Optimal solution for tree_10: Max Path Sum.

Max root-to-leaf path sum (non-negative values).
"""


def solve(children, values, root, n):
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

    walk(root)
    return best
