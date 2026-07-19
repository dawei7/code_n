"""Optimal app-local solution for LeetCode 1506."""


def solve(tree):
    """Return the root value from [value, child_values] node records."""
    root_value = 0
    for value, children in tree:
        root_value ^= value
        for child_value in children:
            root_value ^= child_value
    return root_value
