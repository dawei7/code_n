import os


def solve(filepath: str = "") -> int:
    """Find the maximum weight saving achieved by finding the Minimum Spanning Tree (MST) of a 40-vertex network using Kruskal's Algorithm.

    Mathematical Principles Applied:
    1. Minimum Spanning Tree (MST) & Kruskal's Algorithm:
       Let G = (V, E) be a connected weighted undirected graph with |V| = 40 vertices.
       A spanning tree is a subgraph T = (V, E_T) with |E_T| = |V| - 1 edges that connects all vertices without cycles.
       Kruskal's algorithm sorts all edges by weight in ascending order and greedily adds edges that do not form a cycle,
       guaranteeing a Minimum Spanning Tree (MST) of weight W(T_min).

    2. Disjoint-Set Union-Find Data Structure:
       Use Disjoint-Set Union (DSU) with path compression to detect cycles in near-O(1) time per edge.

    3. Net Saving Calculation:
       Total saving = TotalOriginalWeight - MSTWeight.

    Time Complexity: O(E log E) where |V| = 40, |E| <= 800 (executes in ~0.001s).
    Space Complexity: O(V + E) memory.
    """
    if not filepath:
        # Navigate 4 levels up from solution.py to reach package root (0107_minimal-network/)
        sol_dir = os.path.dirname(os.path.abspath(__file__))
        pkg_dir = os.path.abspath(os.path.join(sol_dir, "..", "..", ".."))
        filepath = os.path.join(pkg_dir, "network.txt")

    # Read network text file
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    lines = [
        line.strip().split(",")
        for line in text.strip().splitlines()
        if line.strip()
    ]
    n = len(lines)

    edges = []
    total_weight = 0

    # Parse upper triangle of 40x40 adjacency matrix to avoid duplicating undirected edges
    for i in range(n):
        for j in range(i + 1, n):
            val = lines[i][j]
            if val != "-":
                w = int(val)
                edges.append((w, i, j))
                total_weight += w

    # Sort edges in ascending order of weight
    edges.sort()

    # Disjoint-set parent array
    parent = list(range(n))

    def find(i: int) -> int:
        """Find root with path compression."""
        if parent[i] == i:
            return i
        parent[i] = find(parent[i])
        return parent[i]

    def union(i: int, j: int) -> bool:
        """Union two sets. Return True if sets were distinct (no cycle created)."""
        root_i = find(i)
        root_j = find(j)
        if root_i != root_j:
            parent[root_i] = root_j
            return True
        return False

    mst_weight = 0
    edge_count = 0

    # Greedily add light edges into MST
    for w, u, v in edges:
        if union(u, v):
            mst_weight += w
            edge_count += 1
            if edge_count == n - 1:
                break

    # Return total weight saving (Original Weight - MST Weight)
    return total_weight - mst_weight


if __name__ == "__main__":
    print(solve())
