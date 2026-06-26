"""Optimal solution for tree_07: Tree Diameter.

For each node, the longest path through it is the sum of the two
tallest subtree depths. The diameter is the max of that sum.
"""


def solve(children, root, n):
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
            if d >= top_two[0]:
                top_two = [d, top_two[0]]
            elif d > top_two[1]:
                top_two[1] = d
        through = top_two[0] + top_two[1]
        if through > best:
            best = through
        return 1 + top_two[0]

    depth(root)
    return best
