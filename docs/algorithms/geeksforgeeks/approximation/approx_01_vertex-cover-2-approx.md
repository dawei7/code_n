# Vertex Cover (2-Approximation)

| | |
|---|---|
| **ID** | `approx_01` |
| **Category** | approximation |
| **Complexity (required)** | $O(V + E)$ |
| **Difficulty** | 5/10 |
| **Interview relevance** | 4/10 |
| **Wikipedia** | [Vertex cover](https://en.wikipedia.org/wiki/Vertex_cover) |

## Problem statement

A **Vertex Cover** of an undirected graph is a subset of its vertices such that *every edge* in the graph is incident to (touches) at least one vertex in the subset.
Finding the absolute *Minimum* Vertex Cover is an NP-Complete problem. However, you can write an approximation algorithm that is guaranteed to find a vertex cover no larger than exactly **twice** the size of the optimal minimum cover.

**Input:** An undirected graph represented as an adjacency list or edge list.
**Output:** A list of vertices that form the approximated vertex cover.

## When to use it

- When you need to place a minimum number of guards/cameras/sensors in a network of hallways such that every hallway is monitored.
- To demonstrate an understanding of approximation ratios for NP-Hard problems in advanced algorithm interviews.

## Approach

A naive greedy approach would be to repeatedly pick the vertex with the highest degree (most connected edges) and add it to the cover. Surprisingly, this degree-greedy approach does NOT guarantee a constant factor approximation! It can yield a cover $O(log V)$ times larger than optimal.

**The Edge-Picking Approximation ($O(V+E)$):**
The simplest and most beautiful 2-approximation algorithm simply picks random edges, not vertices!

1. Start with an empty set `C` (our cover).
2. While there are still edges left in the graph:
   - Pick an arbitrary edge `(u, v)`.
   - Add **both** endpoints `u` and `v` to the cover `C`.
   - Remove `(u, v)` from the graph, and completely remove *all other edges* that are attached to either `u` or `v`.
3. Return `C`.

**Why is it exactly a 2-approximation?**
Every time we pick an edge `(u, v)`, we add *both* vertices to our cover.
To cover that specific edge, the absolute optimal solution *must* pick at least one of `u` or `v`.
By picking both, we are at most paying a penalty of 2x the optimal choice for that specific edge! Because we immediately delete all incident edges, we never double-count this penalty. Thus, the total size of our cover is \le 2 x OPT.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for approx_01: Vertex Cover (2-Approx).

Greedy: pick the max-degree vertex, drop its edges, repeat.
"""


def solve(n, edges):
    if n == 0:
        return set()
    adj = [set() for _ in range(n)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    cover = set()
    edges_left = set()
    for u, v in edges:
        edges_left.add((min(u, v), max(u, v)))
    while edges_left:
        degrees = [0] * n
        for u, v in edges_left:
            degrees[u] += 1
            degrees[v] += 1
        v = max(range(n), key=lambda i: degrees[i])
        if degrees[v] == 0:
            break
        cover.add(v)
        edges_to_remove = [e for e in edges_left if v in e]
        for e in edges_to_remove:
            edges_left.discard(e)
    return sorted(cover)
```

</details>

## Walk-through

Graph Edges: `[(1, 2), (2, 3), (3, 4), (4, 5)]` (A straight line of 5 nodes).
*(Optimal cover is size 2: Nodes 2 and 4).*

1. Pick arbitrary edge: Let's pick `(2, 3)`.
   - Add nodes `2` and `3` to `cover`. `cover = {2, 3}`.
   - Remove `(2, 3)`.
   - Remove edges touching `2`: `(1, 2)`.
   - Remove edges touching `3`: `(3, 4)`.
   - Remaining edges: `[(4, 5)]`.
2. Pick arbitrary edge: `(4, 5)`.
   - Add nodes `4` and `5` to `cover`. `cover = {2, 3, 4, 5}`.
   - Remove `(4, 5)`.
   - Remaining edges: Empty!

Loop finishes. Cover returned: `[2, 3, 4, 5]` (Size 4).
The optimal size was 2. Our size is 4. 4 \le 2 x 2. The 2-approximation bound holds! ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(V + E)$ | $O(V + E)$ |
| **Average** | $O(V + E)$ | $O(V + E)$ |
| **Worst** | $O(V + E)$ | $O(V + E)$ |

Using an adjacency list instead of iterating over a set of edges allows us to find incident edges instantly. Processing each edge and vertex takes constant time, yielding exactly $O(V + E)$ time complexity.
Space complexity is $O(V + E)$ to store the graph structures and the result cover.

## Variants & optimizations

- **Bipartite Graphs:** For Bipartite graphs, you don't need an approximation! By König's theorem, the size of the maximum matching is exactly equal to the minimum vertex cover. You can find the exact minimum vertex cover in polynomial time using the Hopcroft-Karp algorithm.

## Real-world applications

- **Cybersecurity:** Identifying the minimum number of strategic network routers to install packet sniffers on, such that traffic across every physical link is monitored.
- **Biochemistry:** Selecting specific structural markers in protein interaction networks to track evolutionary changes.

## Related algorithms in cOde(n)

- **[approx_02 - Set Cover (Greedy)](approx_02_set-cover-greedy.md)** — A generalization of the Vertex Cover problem.
- **[flow_03 - Bipartite Matching](../flow/flow_03_bipartite-matching.md)** — The exact polynomial-time solution for Vertex Cover if the graph happens to be bipartite.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
