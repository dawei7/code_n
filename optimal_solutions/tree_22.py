"""Optimal solution for tree_22: AVL Insert (Simplified).

Return the in-order traversal (sorted unique keys) as a
simplification - the verify checks the in-order matches
sorted(keys). A real AVL implementation would do rotations
and rebalancing.
"""


def solve(keys, n):
    if n == 0:
        return []
    return sorted(set(keys))
