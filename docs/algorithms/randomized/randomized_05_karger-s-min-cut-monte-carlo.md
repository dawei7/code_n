# Karger's Min-Cut (Monte Carlo)

| | |
|---|---|
| **ID** | `randomized_05` |
| **Category** | randomized |
| **Complexity (required)** | $O(V^2 E)$ Expected |
| **Difficulty** | 7/10 |
| **Interview relevance** | 3/10 |
| **Wikipedia** | [Karger's algorithm](https://en.wikipedia.org/wiki/Karger%27s_algorithm) |

## Problem statement

Given a connected, undirected graph with V vertices and E edges, find the **Global Minimum Cut**.
A cut is a partition of the vertices into two disjoint sets. The size of the cut is the number of edges crossing the partition.
The Minimum Cut is the cut that requires removing the absolute minimum number of edges to disconnect the graph into two separate components.

**Input:** An adjacency list representing the graph.
**Output:** An integer representing the minimum number of edges in the cut.

## When to use it

- To partition clusters in network topology.
- It is the defining example of a **Monte Carlo Algorithm**. Unlike Las Vegas algorithms (which guarantee correct answers but have random running times, like Quicksort), Monte Carlo algorithms have strictly bounded running times but have a random probability of returning the *wrong* answer! You run them many times to amplify the probability of correctness to near 100%.

## Approach

**The Core Idea (Edge Contraction):**
1. Pick a completely random edge from the graph.
2. "Contract" this edge. This means merging the two vertices connected by the edge into a single "super-vertex".
3. Any edges connecting to the original two vertices now connect to the super-vertex.
4. Remove any self-loops (edges that now connect the super-vertex to itself).
5. Repeat this process until exactly 2 super-vertices remain!
6. The number of edges connecting these final two super-vertices is a *candidate* for the Minimum Cut.

**Why does this work?**
Let the true minimum cut be a specific set of edges C.
If we randomly contract edges, as long as we *never* pick an edge from C, the edges in C will survive to the very end, and we will find the perfect minimum cut!
Because C is by definition the absolute smallest bottleneck in the graph, picking a completely random edge is statistically *highly unlikely* to hit C in the early stages!

**Amplification:**
A single run of Karger's algorithm only has a probability of \ge \frac{2}{V(V-1)} of finding the correct minimum cut. This is terrible!
However, if we run the algorithm V^2 log V times and take the minimum result across all runs, the probability of failing *every single time* drops to \le \frac{1}{V}, making it practically guaranteed to be correct!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for randomized_05: Karger's Min-Cut (Monte Carlo).

Given an undirected unweighted graph (with
"""


def solve(edges, n, trials):
    """Karger's min-cut algorithm with multiple trials.

    Each trial: randomly contract edges until 2 vertices
    remain. The number of remaining edges is the cut size
    for that trial. Return the minimum cut across all
    trials.
    """
    import random
    if n <= 1:
        return 0
    if n == 2:
        return len(edges)
    best = float("inf")
    for _ in range(max(1, trials)):
        # Union-Find: each vertex has a parent representative.
        parent = list(range(n))
        rank = [0] * n
        def find(x):
            r = x
            while parent[r] != r:
                r = parent[r]
            # Path compression.
            while parent[x] != r:
                parent[x], x = r, parent[x]
            return r
        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if rank[ra] < rank[rb]:
                parent[ra] = rb
            elif rank[ra] > rank[rb]:
                parent[rb] = ra
            else:
                parent[rb] = ra
                rank[ra] += 1
        # Run one trial: shuffle edges and contract until
        # 2 components remain. The contracted multigraph
        # has parallel edges; we model it by keeping all
        # edges and counting "alive" ones.
        live_edges = list(edges)
        random.shuffle(live_edges)
        # Number of components = number of distinct roots.
        num_components = n
        for u, v in live_edges:
            if num_components <= 2:
                break
            ru, rv = find(u), find(v)
            if ru == rv:
                # Self-loop in the contracted graph; ignore.
                continue
            union(ru, rv)
            num_components -= 1
        # Count cut edges: edges (u, v) with find(u) != find(v).
        cut = 0
        for u, v in edges:
            if find(u) != find(v):
                cut += 1
        if cut < best:
            best = cut
    return best
```

</details>

## Walk-through

Graph is a square: `A-B, B-C, C-D, D-A`.
True min cut is 2 (e.g. cut `A-B` and `C-D` to separate `A,D` from `B,C`).

**Run 1:**
- Pick edge `B-C`. Contract `C` into `B`. Graph is now triangle: `A-B, B-D` (this is the old C-D edge), and `D-A`.
- Pick edge `A-B`. Contract `B` into `A`.
- Only `A` and `D` remain.
- Edges between `A` and `D`: The original `A-D` edge, and the `B-D` edge (which was originally `C-D`).
- Cut size = 2. It found the optimal cut!

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(V^2 E)$ Expected | $O(V + E)$ |
| **Average** | $O(V^2 E)$ Expected | $O(V + E)$ |
| **Worst** | $O(V^2 E)$ Expected | $O(V + E)$ |

A single contraction takes $O(E)$ time. Contracting the whole graph down to 2 nodes takes $O(V \cdot E)$. We repeat this V^2 times for amplification. Total time is $O(V^3 E)$.
Space complexity is $O(V + E)$ to maintain the multigraph in memory during contraction.

## Variants & optimizations

- **Karger-Stein Algorithm ($O(V^2 log^3 V)$):** Karger noticed that the probability of accidentally picking an edge in the minimum cut is extremely low at the beginning, but gets dangerously high at the end when very few vertices are left. Karger-Stein runs the contraction down to V / \sqrt{2} vertices, and then branches into *two* separate recursive copies. This radically reduces the necessary amplification iterations, dropping the time complexity drastically!
- **Stoer-Wagner Algorithm:** The deterministic $O(V E + V^2 log V)$ alternative that does not use randomization.

## Real-world applications

- **Image Segmentation:** Used in computer vision to partition an image into foreground and background by finding the minimum cut in a pixel-similarity graph.

## Related algorithms in cOde(n)

- **[randomized_01 - Randomized Quicksort](randomized_01_randomized-quicksort.md)** — Las Vegas randomization (Guarantees correctness, variable time). Karger's is Monte Carlo (Guarantees time, variable correctness).

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
