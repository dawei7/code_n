class Solution:
    def calcEquation(
        self,
        equations: List[List[str]],
        values: List[float],
        queries: List[List[str]],
    ) -> List[float]:
        parent = {}
        weight = {}

        def add(variable):
            if variable not in parent:
                parent[variable] = variable
                weight[variable] = 1.0

        def find(variable):
            if parent[variable] != variable:
                old_parent = parent[variable]
                parent[variable] = find(old_parent)
                weight[variable] *= weight[old_parent]
            return parent[variable]

        for (numerator, denominator), value in zip(equations, values):
            add(numerator)
            add(denominator)
            numerator_root = find(numerator)
            denominator_root = find(denominator)
            if numerator_root != denominator_root:
                parent[numerator_root] = denominator_root
                weight[numerator_root] = value * weight[denominator] / weight[numerator]

        results = []
        for numerator, denominator in queries:
            if numerator not in parent or denominator not in parent:
                results.append(-1.0)
            elif find(numerator) != find(denominator):
                results.append(-1.0)
            else:
                results.append(weight[numerator] / weight[denominator])

        return results
