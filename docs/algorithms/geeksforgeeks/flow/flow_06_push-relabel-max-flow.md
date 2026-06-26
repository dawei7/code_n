# Push-Relabel (Max Flow)

| | |
|---|---|
| **ID** | `flow_06` |
| **Category** | flow |
| **Complexity (required)** | $O(V^3)$ |
| **Difficulty** | 9/10 |
| **Interview relevance** | 2/10 |
| **Wikipedia** | [Push–relabel maximum flow algorithm](https://en.wikipedia.org/wiki/Push%E2%80%93relabel_maximum_flow_algorithm) |

## Problem statement

Given a directed graph representing a network of pipes with capacities, find the maximum possible flow from a source node S to a sink node T.
You must solve this using the **Push-Relabel** framework. Instead of finding augmenting paths from S to T (like Ford-Fulkerson or Dinic's), this algorithm completely ignores paths. It operates entirely locally, pushing "excess water" between adjacent nodes like a series of cascading waterfalls.

**Input:** A directed graph with capacities, a source node `s`, and a sink node `t`.
**Output:** An integer representing the maximum total flow.

## When to use it

- Push-Relabel algorithms (specifically the "Highest-Label Preflow Push" variant) are empirically the fastest Max Flow algorithms in existence for dense graphs, outperforming Dinic's in extreme real-world workloads.
- The fundamental mechanism used heavily in distributed network flow calculations, as nodes only need to communicate with their immediate neighbors.

## Approach

Imagine the nodes are buckets of water suspended at different heights. Water naturally flows downhill.

1. **Initialization (Heights & Preflow):**
   - Every node starts at `height = 0`. The Source S is raised to `height = V` (the highest point).
   - S immediately floods all of its neighbors with as much water as their pipes can handle (saturating the outgoing edges).
   - These neighbors now have "Excess Flow" (they have water in their buckets, but haven't sent it anywhere yet).

2. **The Operations:**
   We process any node (except S or T) that currently has `excess > 0`. We can do two things:
   - **PUSH:** If the node has excess water, and it has a neighbor that is strictly *downhill* (`height[u] == height[v] + 1`), and the pipe between them has residual capacity, we "Push" as much water as possible down the pipe.
   - **RELABEL:** If the node has excess water, but ALL of its neighbors with available pipe capacity are at the same height or strictly *higher*, the water is trapped! We must "Relabel" (lift) the node. We increase its height to be exactly 1 higher than the lowest available neighbor.

3. **Termination:**
   We keep Pushing and Relabeling until absolutely no node has any excess water.
   - Any water that makes it to T stays in T. This is our Max Flow!
   - Any water trapped in the network eventually gets lifted so high that it flows *backward* down the residual edges all the way back into the Source S!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for flow_06: Push-Relabel Max Flow.

Compute the max s-t flow using the Goldberg-Tarjan
"""


def solve(n, edges):
    """Goldberg-Tarjan push-relabel max flow.

    Generic O(V^3) variant. The residual capacity of an edge
    (u, v) is maintained as a direct value (not cap-flow),
    so a push that decreases residual[u][v] increases
    residual[v][u] by the same amount.
    """
    # residual[u][v] = remaining forward capacity from u to v.
    residual = [[0] * n for _ in range(n)]
    for u, v, c in edges:
        residual[u][v] += c
    height = [0] * n
    excess = [0] * n
    height[0] = n
    # Initial push from source: saturate every outgoing edge.
    for v in range(n):
        if residual[0][v] > 0:
            pushed = residual[0][v]
            residual[0][v] -= pushed
            residual[v][0] += pushed
            excess[v] += pushed

    def push(u, v):
        d = min(excess[u], residual[u][v])
        if d <= 0:
            return False
        residual[u][v] -= d
        residual[v][u] += d
        excess[u] -= d
        excess[v] += d
        return True

    def relabel(u):
        best = float("inf")
        for v in range(n):
            if residual[u][v] > 0 and height[v] < best:
                best = height[v]
        if best < float("inf"):
            height[u] = best + 1

    # Main loop: discharge active vertices (those with positive
    # excess that are not s or t). When a push creates new
    # excess at an inner vertex, add it to the active list.
    active = set()
    for i in range(1, n - 1):
        if excess[i] > 0:
            active.add(i)
    while active:
        # Highest-label selection.
        u = max(active, key=lambda x: height[x])
        old_h = height[u]
        # Discharge: try to push, or relabel.
        while excess[u] > 0:
            pushed = False
            for v in range(n):
                if residual[u][v] > 0 and height[u] == height[v] + 1:
                    if push(u, v):
                        pushed = True
                        if v != 0 and v != n - 1 and excess[v] > 0:
                            active.add(v)
                        break
            if not pushed:
                relabel(u)
        if excess[u] == 0:
            active.discard(u)
    return excess[n - 1]
```

</details>

## Walk-through

*(Conceptual)*
`S -> A (cap 10)`. `A -> T (cap 5)`.
1. **Initialize:** `height[S] = 4`. All others 0. `S` pushes 10 to `A`. `excess[A] = 10`.
2. **Push:** `A` is active. Neighbor `T` is downhill (`height[A]=0`, `height[T]=0` ... wait! They are at the same height!). `A` cannot push!
3. **Relabel:** `A` is trapped. Lowest neighbor with capacity is `T` (height 0). `A` is lifted to `height = 1`.
4. **Push:** Now `height[A]=1` and `height[T]=0`. `A` pushes 5 units to `T`.
   - `excess[T] = 5`.
   - `excess[A] = 5`. `A` is still active!
5. **Relabel:** `A` tries to push to `T`, but the pipe is fully saturated. The only neighbor with residual capacity is S (via the backward "Undo" edge). `height[S] = 4`.
   - `A` is lifted to `height = 4 + 1 = 5`!
6. **Push:** Now `height[A]=5` and `height[S]=4`. `A` pushes its remaining 5 excess back into S.
7. **Settle:** No active nodes. Sink `T` has exactly 5 units. Max flow = 5. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(V^2)$ | $O(V^2)$ |
| **Average** | Much faster than V^3 | $O(V^2)$ |
| **Worst** | $O(V^3)$ | $O(V^2)$ |

The theoretical worst-case time for the generic FIFO Push-Relabel algorithm is mathematically bounded to exactly $O(V^3)$ (or $O(V^2 \sqrt{E})$ if selecting the Highest active node). This makes it strictly superior to Edmonds-Karp ($O(V \cdot E^2)$) on dense graphs where E ~= V^2.
Space complexity is $O(V^2)$ to store the capacity and flow matrices.

## Variants & optimizations

- **Gap Heuristic:** The most critical optimization in production code. If during a Relabel operation, you notice that *no nodes* in the entire graph exist at `height = X`, then any node with a height > X is mathematically proven to be completely disconnected from the Sink! You can instantly lift all those nodes to `height = V`, forcing them to immediately drain back to S, skipping thousands of useless intermediate relabel operations.

## Real-world applications

- **Distributed Systems:** Calculating aggregate data flow throughputs in massive peer-to-peer torrenting swarms, where global pathfinding is impossible but local "pushing" is trivial.

## Related algorithms in cOde(n)

- **[flow_04 - Dinic's Algorithm](flow_04_dinic-s-max-flow.md)** — The augmenting-path rival that is generally easier to code and preferred in standard algorithmic competitions.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
