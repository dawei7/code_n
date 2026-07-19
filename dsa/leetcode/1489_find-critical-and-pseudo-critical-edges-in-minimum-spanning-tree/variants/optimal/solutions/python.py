class DisjointSet:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, node):
        while self.parent[node] != node:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return node

    def union(self, first, second):
        first_root = self.find(first)
        second_root = self.find(second)
        if first_root == second_root:
            return False

        if self.rank[first_root] < self.rank[second_root]:
            first_root, second_root = second_root, first_root
        self.parent[second_root] = first_root
        if self.rank[first_root] == self.rank[second_root]:
            self.rank[first_root] += 1
        return True


def solve(n, edges):
    indexed = sorted(
        (weight, first, second, index)
        for index, (first, second, weight) in enumerate(edges)
    )
    components = DisjointSet(n)
    critical = []
    pseudo_critical = []
    cursor = 0

    while cursor < len(indexed):
        end = cursor + 1
        weight = indexed[cursor][0]
        while end < len(indexed) and indexed[end][0] == weight:
            end += 1

        adjacency = {}
        candidates = []

        for _, first, second, index in indexed[cursor:end]:
            first_root = components.find(first)
            second_root = components.find(second)
            if first_root == second_root:
                continue

            candidates.append((first_root, second_root, index))
            adjacency.setdefault(first_root, []).append((second_root, index))
            adjacency.setdefault(second_root, []).append((first_root, index))

        discovery = {}
        low = {}
        bridges = set()
        timestamp = 0

        def find_bridges(node, parent_edge):
            nonlocal timestamp
            discovery[node] = timestamp
            low[node] = timestamp
            timestamp += 1

            for neighbor, edge_index in adjacency[node]:
                if edge_index == parent_edge:
                    continue
                if neighbor not in discovery:
                    find_bridges(neighbor, edge_index)
                    low[node] = min(low[node], low[neighbor])
                    if low[neighbor] > discovery[node]:
                        bridges.add(edge_index)
                else:
                    low[node] = min(low[node], discovery[neighbor])

        for node in adjacency:
            if node not in discovery:
                find_bridges(node, -1)

        for _, _, index in candidates:
            if index in bridges:
                critical.append(index)
            else:
                pseudo_critical.append(index)

        for _, first, second, _ in indexed[cursor:end]:
            components.union(first, second)

        cursor = end

    return [sorted(critical), sorted(pseudo_critical)]
