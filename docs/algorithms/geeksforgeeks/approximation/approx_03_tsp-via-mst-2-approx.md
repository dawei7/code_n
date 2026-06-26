# TSP via MST (2-Approximation)

| | |
|---|---|
| **ID** | `approx_03` |
| **Category** | approximation |
| **Complexity (required)** | $O(V^2 log V)$ |
| **Difficulty** | 6/10 |
| **Interview relevance** | 4/10 |
| **Wikipedia** | [Travelling salesman problem](https://en.wikipedia.org/wiki/Travelling_salesman_problem) |

## Problem statement

Given a fully connected graph representing cities and distances between them, find the shortest possible route that visits every city exactly once and returns to the origin city.
This is the **Travelling Salesman Problem (TSP)**, an NP-Hard problem.
Assume the graph obeys the **Triangle Inequality** (the direct path between A and B is always shorter than or equal to going through an intermediary C).
Design an algorithm that finds a route guaranteed to be no more than **twice** the length of the optimal route.

**Input:** An adjacency matrix representing distances between vertices.
**Output:** A list of vertices representing the tour, and the total distance.

## When to use it

- When V is large (e.g. 1000 cities), making exact $O(2^V)$ DP solutions completely impossible.
- As a stepping stone to understanding the 1.5-approximation Christofides algorithm.

## Approach

The optimal TSP tour is a cycle that visits all vertices. If we remove one edge from this cycle, we get a spanning tree!
Therefore, the weight of the Minimum Spanning Tree (MST) of the graph MUST be less than the weight of the optimal TSP tour! `Weight(MST) < Weight(OPT)`.

**The Algorithm:**
1. **Find the MST:** Find the Minimum Spanning Tree of the graph using Prim's or Kruskal's algorithm.
2. **Double the Edges:** Imagine walking along the MST. If we walk down every edge and then walk back up it, we will visit every node and return to the start. The cost of this walk is exactly `2 * Weight(MST)`. Since `Weight(MST) < Weight(OPT)`, this walk is `< 2 * Weight(OPT)`!
3. **Euler Tour (Preorder Traversal):** We trace the doubled MST.
4. **Shortcuts:** The doubled MST walk visits vertices multiple times. Because the graph obeys the triangle inequality, taking a direct shortcut to an unvisited node is ALWAYS cheaper than revisiting old nodes! We perform a **Preorder Traversal (DFS)** on the MST, adding a node to our tour only the *first* time we see it.

The resulting tour is valid (visits everyone once) and its cost is strictly \le 2 x OPT.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for approx_03: TSP via MST (2-Approx).

Given a complete graph with edge costs that satisfy
"""


def solve(cost, n):
    """MST-based 2-approximate TSP.

    1. Build MST rooted at 0 via Prim's.
    2. Preorder walk of the MST to produce a tour.
    3. Sum the costs along the tour (including the return
       edge from the last vertex back to 0).
    """
    if n <= 1:
        return 0
    INF = float("inf")
    # Prim's MST.
    in_mst = [False] * n
    in_mst[0] = True
    # parent[i] = the node that brought i into the MST.
    parent = [-1] * n
    for _ in range(n - 1):
        best_w = INF
        best_v = -1
        for u in range(n):
            if not in_mst[u]:
                continue
            for v in range(n):
                if in_mst[v]:
                    continue
                if cost[u][v] < best_w:
                    best_w = cost[u][v]
                    best_v = v
                    parent[v] = u
        if best_v == -1:
            break
        in_mst[best_v] = True
    # Preorder DFS walk of the MST.
    children = [[] for _ in range(n)]
    for v in range(n):
        p = parent[v]
        if p != -1:
            children[p].append(v)
    tour = []
    def dfs(u):
        tour.append(u)
        for c in children[u]:
            dfs(c)
    dfs(0)
    # Sum tour cost (including the return edge).
    total = 0
    for i in range(len(tour) - 1):
        total += cost[tour[i]][tour[i + 1]]
    total += cost[tour[-1]][0]
    return total
```

</details>

## Walk-through

Graph: 3 nodes in a triangle. `dist(0,1)=10`, `dist(1,2)=10`, `dist(0,2)=15`.
*(Optimal TSP: 0 -> 1 -> 2 -> 0. Cost = 10 + 10 + 15 = 35).*

1. **MST (Prim's):**
   - Start at 0. Edges: `(0,1: 10)`, `(0,2: 15)`.
   - Pop `(0,1)`. Add 1. MST edges: `[(0,1)]`.
   - From 1, edges: `(1,2: 10)`.
   - Pop `(1,2)`. Add 2. MST edges: `[(0,1), (1,2)]`. Weight is 20.
2. **Preorder Traversal (DFS):**
   - Start at 0. Add 0.
   - Go to 1. Add 1.
   - Go to 2. Add 2.
3. **Finish Tour:**
   - Append start node 0.
   - Tour = `[0, 1, 2, 0]`.
4. **Distance Calculation:**
   - `0->1` (10) + `1->2` (10) + `2->0` (15) = 35.

Result: 35. Our 2-approximation found the exact optimal route! ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(V^2 log V)$ | $O(V^2)$ |
| **Average** | $O(V^2 log V)$ | $O(V^2)$ |
| **Worst** | $O(V^2 log V)$ | $O(V^2)$ |

Building the MST on a dense fully-connected graph (where E = V^2) using Prim's algorithm with a binary heap takes $O(E log V)$ = $O(V^2 log V)$. The subsequent DFS takes $O(V)$ time. Total time is dominated by the MST construction.
Space complexity is $O(V^2)$ to store the adjacency matrix and Priority Queue.

## Variants & optimizations

- **Christofides Algorithm:** A 1.5-approximation. It also starts with an MST. But instead of just blindly doing a DFS (which relies on taking expensive shortcuts to fix the odd-degree nodes created by the doubled edges), Christofides finds a Minimum-Weight Perfect Matching strictly for the nodes with odd degrees, and adds those specific edges to the MST. This creates an Eulerian circuit directly, dropping the approximation bound to exactly 1.5 x OPT!
- **Held-Karp DP:** The $O(V^2 2^V)$ dynamic programming exact solution.

## Real-world applications

- **Delivery Routing:** A UPS truck determining the delivery route for 100 packages. The distances between houses obey the triangle inequality, so approximations work flawlessly.
- **Circuit Board Drilling:** Optimizing the path of a laser drill creating holes in a PCB.

## Related algorithms in cOde(n)

- **[graph_10 - Prim's MST](../graphs/graph_10_prim-s-mst.md)** — The exact MST algorithm used as the foundational step here.
- **[approx_04 - Christofides TSP](approx_04_christofides-tsp-3-2-approx.md)** — The 1.5-approximation improvement.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
