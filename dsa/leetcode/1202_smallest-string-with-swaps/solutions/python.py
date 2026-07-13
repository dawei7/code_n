from collections import defaultdict


def solve(s, pairs):
    parent = list(range(len(s)))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra

    for a, b in pairs:
        union(a, b)

    groups = defaultdict(list)
    for i, ch in enumerate(s):
        groups[find(i)].append(ch)
    for chars in groups.values():
        chars.sort(reverse=True)

    result = []
    for i in range(len(s)):
        result.append(groups[find(i)].pop())
    return "".join(result)
