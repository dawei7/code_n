"""Optimal app-local solution for LeetCode 399: Evaluate Division."""


def solve(
    equations: list[list[str]],
    values: list[float],
    queries: list[list[str]],
) -> list[float]:
    parent: dict[str, str] = {}
    weight: dict[str, float] = {}

    def add(variable: str) -> None:
        if variable not in parent:
            parent[variable] = variable
            weight[variable] = 1.0

    def find(variable: str) -> str:
        if parent[variable] != variable:
            old_parent = parent[variable]
            parent[variable] = find(old_parent)
            weight[variable] *= weight[old_parent]
        return parent[variable]

    for (numerator, denominator), value in zip(equations, values, strict=True):
        add(numerator)
        add(denominator)
        numerator_root = find(numerator)
        denominator_root = find(denominator)
        if numerator_root != denominator_root:
            parent[numerator_root] = denominator_root
            weight[numerator_root] = value * weight[denominator] / weight[numerator]

    results: list[float] = []
    for numerator, denominator in queries:
        if numerator not in parent or denominator not in parent:
            results.append(-1.0)
        elif find(numerator) != find(denominator):
            results.append(-1.0)
        else:
            results.append(weight[numerator] / weight[denominator])

    return results
