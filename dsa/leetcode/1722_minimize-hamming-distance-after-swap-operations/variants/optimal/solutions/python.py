from collections import Counter, defaultdict


def solve(
    source: list[int],
    target: list[int],
    allowedSwaps: list[list[int]],
) -> int:
    parent = list(range(len(source)))
    size = [1] * len(source)

    def find(node: int) -> int:
        while node != parent[node]:
            parent[node] = parent[parent[node]]
            node = parent[node]
        return node

    for first, second in allowedSwaps:
        root_first = find(first)
        root_second = find(second)
        if root_first == root_second:
            continue
        if size[root_first] < size[root_second]:
            root_first, root_second = root_second, root_first
        parent[root_second] = root_first
        size[root_first] += size[root_second]

    available: dict[int, Counter[int]] = defaultdict(Counter)
    for index, value in enumerate(source):
        available[find(index)][value] += 1

    distance = 0
    for index, value in enumerate(target):
        counts = available[find(index)]
        if counts[value]:
            counts[value] -= 1
        else:
            distance += 1
    return distance
