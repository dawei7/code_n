"""Optimal app-local solution for LeetCode 839."""


def solve(strs):
    count = len(strs)
    parent = list(range(count))
    component_size = [1] * count

    def find(node):
        while parent[node] != node:
            parent[node] = parent[parent[node]]
            node = parent[node]
        return node

    def union(first, second):
        first_root = find(first)
        second_root = find(second)
        if first_root == second_root:
            return
        if component_size[first_root] < component_size[second_root]:
            first_root, second_root = second_root, first_root
        parent[second_root] = first_root
        component_size[first_root] += component_size[second_root]

    for first in range(count):
        for second in range(first):
            mismatches = 0
            for left, right in zip(strs[first], strs[second]):
                if left != right:
                    mismatches += 1
                    if mismatches > 2:
                        break
            if mismatches <= 2:
                union(first, second)

    return sum(find(index) == index for index in range(count))
