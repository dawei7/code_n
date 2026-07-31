"""Optimal app-local solution for LeetCode 3600."""


def solve(n, edges, k):
    parent = list(range(n))
    size = [1] * n

    def find(node):
        while parent[node] != node:
            parent[node] = parent[parent[node]]
            node = parent[node]
        return node

    def union(first, second):
        first = find(first)
        second = find(second)
        if first == second:
            return False
        if size[first] < size[second]:
            first, second = second, first
        parent[second] = first
        size[first] += size[second]
        return True

    optional = []
    mandatory_min = float("inf")
    selected = 0

    for first, second, strength, must in edges:
        if must:
            if not union(first, second):
                return -1
            mandatory_min = min(mandatory_min, strength)
            selected += 1
        else:
            optional.append((strength, first, second))

    chosen_optional = []
    optional.sort(reverse=True)
    for strength, first, second in optional:
        if union(first, second):
            chosen_optional.append(strength)
            selected += 1

    if selected != n - 1:
        return -1

    chosen_optional.sort()
    for i in range(min(k, len(chosen_optional))):
        chosen_optional[i] *= 2

    if chosen_optional:
        mandatory_min = min(mandatory_min, min(chosen_optional))

    return int(mandatory_min)
