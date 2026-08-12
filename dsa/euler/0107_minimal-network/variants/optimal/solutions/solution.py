import urllib.request


def solve() -> int:
    """Find maximum saving achieved by computing Minimum Spanning Tree (MST) of 40-vertex network.
    
    Time Complexity: O(E log E)
    Space Complexity: O(V + E)
    """
    url = "https://projecteuler.net/resources/documents/0107_network.txt"
    with urllib.request.urlopen(url, timeout=5) as resp:
        text = resp.read().decode("utf-8")

    lines = [line.strip().split(",") for line in text.strip().splitlines() if line.strip()]
    n = len(lines)

    edges = []
    total_weight = 0

    for i in range(n):
        for j in range(i + 1, n):
            val = lines[i][j]
            if val != "-":
                w = int(val)
                edges.append((w, i, j))
                total_weight += w

    edges.sort()

    parent = list(range(n))

    def find(i):
        if parent[i] == i:
            return i
        parent[i] = find(parent[i])
        return parent[i]

    def union(i, j):
        root_i = find(i)
        root_j = find(j)
        if root_i != root_j:
            parent[root_i] = root_j
            return True
        return False

    mst_weight = 0
    edge_count = 0

    for w, u, v in edges:
        if union(u, v):
            mst_weight += w
            edge_count += 1
            if edge_count == n - 1:
                break

    return total_weight - mst_weight
