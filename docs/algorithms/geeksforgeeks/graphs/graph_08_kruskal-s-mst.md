# Kruskal's Algorithm (Minimum Spanning Tree)

| | |
|---|---|
| **ID** | `graph_08` |
| **Category** | graphs |
| **Complexity (required)** | $O(E log E)$ Time, $O(V)$ Space |
| **Difficulty** | 5/10 |
| **Interview relevance** | 7/10 |
| **Wikipedia** | [Kruskal's algorithm](https://en.wikipedia.org/wiki/Kruskal%27s_algorithm) |

## Problem statement

Given a connected, undirected, and weighted graph. Find a Minimum Spanning Tree (MST) for the graph.
A Minimum Spanning Tree is a subset of the edges that connects all V vertices together, without any cycles, and with the minimum possible total edge weight.

**Input:** Number of vertices `V`, and an edge list `edges` where each edge is `[u, v, weight]`.
**Output:** An integer representing the minimum total weight of the MST, and/or the list of edges in the MST.

## When to use it

- To solve the classic Minimum Spanning Tree problem.
- When the graph is **Sparse** (E is relatively small compared to V^2), Kruskal's is slightly faster and vastly easier to code than Prim's Algorithm.

## Approach

**1. The Greedy Insight:**
If we want the *minimum* total weight, shouldn't we just prioritize the absolute cheapest edges in the entire graph?
Yes! Let's just sort the entire `edges` array from lowest weight to highest weight.

**2. Building the Tree:**
We iterate through our sorted edges, starting with the absolute cheapest edge in existence.
We want to add this edge to our MST. But we must obey one strict rule: **The MST cannot contain cycles!**
If adding this edge connects two nodes that are *already connected* by previous edges we added, it creates a cycle! We must throw this edge away and look at the next cheapest one.

**3. Cycle Detection (The Disjoint Set / Union-Find):**
How do we efficiently check if two nodes are "already connected" by our growing web of MST edges?
We use a **Disjoint Set (Union-Find)** data structure!
- Initially, every vertex is in its own isolated set.
- When we look at an edge `[u, v, weight]`, we check `find(u) == find(v)`.
- If they are the same, they are already in the same connected component. Adding this edge would create a cycle. Discard it!
- If they are different, no cycle is created! We add the edge to our MST, and we immediately merge their components using `union(u, v)`.

**4. Termination:**
A Spanning Tree connecting V vertices will ALWAYS contain exactly V - 1 edges. Once we have successfully `union`'d exactly V - 1 edges, we can terminate early! The MST is complete.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for graph_08: Kruskal's MST.

Greedy edge-by-edge union with DSU. Returns sorted MST edges or
[] if the graph is not connected.
"""


def solve(num_nodes, edges):
    parent = list(range(num_nodes))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        parent[ra] = rb
        return True

    mst = []
    for u, v, w in sorted(edges, key=lambda e: e[2]):
        if union(u, v):
            mst.append((u, v, w))
    if len(mst) != num_nodes - 1:
        return []
    return sorted(mst)
```

</details>

## Walk-through

`V = 4`. Edges: `0-1 (10)`, `0-2 (6)`, `0-3 (5)`, `1-3 (15)`, `2-3 (4)`.

1. **Sort Edges:**
   `2-3 (4)`, `0-3 (5)`, `0-2 (6)`, `0-1 (10)`, `1-3 (15)`.
2. **Edge 2-3 (4):** `find(2)!=find(3)`. Union them.
   `mst_weight = 4`. Sets: `{2, 3}`, `{0}`, `{1}`. `edges_added = 1`.
3. **Edge 0-3 (5):** `find(0)!=find(3)`. Union them.
   `mst_weight = 4+5 = 9`. Sets: `{0, 2, 3}`, `{1}`. `edges_added = 2`.
4. **Edge 0-2 (6):** `find(0) == find(2)`! They are already in the same set! If we add this, it forms the cycle 0-2-3-0. Discard edge!
5. **Edge 0-1 (10):** `find(0)!=find(1)`. Union them.
   `mst_weight = 9+10 = 19`. Sets: `{0, 1, 2, 3}`. `edges_added = 3`.
6. `edges_added == 4 - 1 = 3`. Terminate Early!

Result `mst_weight = 19`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(E log E)$ | $O(V + E)$ |
| **Average** | $O(E log E)$ | $O(V + E)$ |
| **Worst** | $O(E log E)$ | $O(V + E)$ |

Sorting the edges array takes $O(E log E)$.
Iterating through the edges takes $O(E)$. Inside the loop, the Union-Find operations take practically $O(1)$ time due to path compression and union by rank (specifically, inverse Ackermann function \alpha(V)).
Thus, the sort massively dominates the algorithm. Time complexity is $O(E log E)$. (Since E \le V^2, this is mathematically equivalent to $O(E log V)$).
Space complexity is $O(V)$ for the Union-Find parent and rank arrays, plus $O(E)$ if creating a new array to store the MST edges.

## Variants & optimizations

- **Maximum Spanning Tree:** Sort the edges in *descending* order instead of ascending! Everything else is perfectly identical.
- **Prim's Algorithm (`graph_10`):** The alternative to Kruskal's. Instead of sorting all edges globally, you pick a starting node and use a Priority Queue (just like Dijkstra) to slowly grow a single tree outward by picking the cheapest adjacent edge. Prim's is vastly superior for highly dense graphs (E ~= V^2) where sorting E is too slow.

## Real-world applications

- **Network Design:** Laying out the absolute minimum length of expensive fiber-optic cables to ensure V datacenters are all connected to the same grid.

## Related algorithms in cOde(n)

- **[graph_09 - Union-Find](graph_09_union-find.md)** — The mandatory data structure prerequisite required to detect cycles in Kruskal's.
- **[graph_10 - Prim's MST](graph_10_prim-s-mst.md)** — The Priority Queue alternative to solving the exact same MST problem.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
