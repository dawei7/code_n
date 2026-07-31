def solve(conversions: list[list[int]]) -> list[int]:
    modulo = 1_000_000_007
    unit_count = len(conversions) + 1
    graph = [[] for _ in range(unit_count)]

    for source, target, factor in conversions:
        graph[source].append((target, factor))

    result = [0] * unit_count
    result[0] = 1
    stack = [0]

    while stack:
        source = stack.pop()
        for target, factor in graph[source]:
            result[target] = result[source] * factor % modulo
            stack.append(target)

    return result
