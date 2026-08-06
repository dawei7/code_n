"""Proposed app-local solution for LeetCode 399: Evaluate Division."""


def solve(
    equations: list[list[str]],
    values: list[float],
    queries: list[list[str]],
) -> list[float]:
    parent = {}
    weight = {}
    size = {}

    def add(variable):
        if variable not in parent:
            parent[variable] = variable
            weight[variable] = 1.0
            size[variable] = 1

    def find(variable):
        if parent[variable] != variable:
            old_parent = parent[variable]
            parent[variable] = find(old_parent)
            weight[variable] *= weight[old_parent]
        return parent[variable]

    for (numerator, denominator), ratio in zip(equations, values):
        add(numerator)
        add(denominator)
        numerator_root = find(numerator)
        denominator_root = find(denominator)
        if numerator_root == denominator_root:
            continue

        root_ratio = ratio * weight[denominator] / weight[numerator]
        if size[numerator_root] < size[denominator_root]:
            parent[numerator_root] = denominator_root
            weight[numerator_root] = root_ratio
            size[denominator_root] += size[numerator_root]
        else:
            parent[denominator_root] = numerator_root
            weight[denominator_root] = 1.0 / root_ratio
            size[numerator_root] += size[denominator_root]

    results = []
    for numerator, denominator in queries:
        if numerator not in parent or denominator not in parent:
            results.append(-1.0)
        elif find(numerator) != find(denominator):
            results.append(-1.0)
        else:
            results.append(weight[numerator] / weight[denominator])

    return results
