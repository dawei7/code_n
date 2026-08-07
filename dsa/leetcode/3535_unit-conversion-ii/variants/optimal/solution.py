class Solution:
    def queryConversions(self, conversions: List[List[int]], queries: List[List[int]]) -> List[int]:
        modulus = 1_000_000_007
        unit_count = len(conversions) + 1
        graph = [[] for _ in range(unit_count)]

        for source, target, factor in conversions:
            graph[source].append((target, factor))
            graph[target].append(
                (
                    source,
                    pow(factor, modulus - 2, modulus),
                )
            )

        from_root = [0] * unit_count
        from_root[0] = 1
        stack = [0]

        while stack:
            unit = stack.pop()
            for neighbor, factor in graph[unit]:
                if from_root[neighbor] == 0:
                    from_root[neighbor] = (from_root[unit] * factor) % modulus
                    stack.append(neighbor)

        return [
            from_root[target] * pow(from_root[source], modulus - 2, modulus) % modulus for source, target in queries
        ]
