"""Optimal app-local solution for LeetCode 952."""


def solve(nums):
    parent = list(range(len(nums)))
    size = [1] * len(nums)

    def find(node):
        while parent[node] != node:
            parent[node] = parent[parent[node]]
            node = parent[node]
        return node

    def union(first, second):
        first = find(first)
        second = find(second)
        if first == second:
            return
        if size[first] < size[second]:
            first, second = second, first
        parent[second] = first
        size[first] += size[second]

    owner = {}
    for index, number in enumerate(nums):
        remaining = number
        factor = 2
        while factor * factor <= remaining:
            if remaining % factor == 0:
                if factor in owner:
                    union(index, owner[factor])
                else:
                    owner[factor] = index
                while remaining % factor == 0:
                    remaining //= factor
            factor += 1
        if remaining > 1:
            if remaining in owner:
                union(index, owner[remaining])
            else:
                owner[remaining] = index

    counts = {}
    for index in range(len(nums)):
        root = find(index)
        counts[root] = counts.get(root, 0) + 1
    return max(counts.values())
