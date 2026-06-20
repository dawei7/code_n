# Bipartite Matching (Max Flow)

| | |
|---|---|
| **ID** | `flow_03` |
| **Category** | flow |
| **Complexity (required)** | $O(V * E)$ |
| **Difficulty** | 4/10 |
| **Interview relevance** | 8/10 |
| **Wikipedia** | [Maximum bipartite matching](https://en.wikipedia.org/wiki/Matching_(graph_theory)#In_unweighted_bipartite_graphs) |

## Problem statement

Given a bipartite graph consisting of a left set of vertices (e.g., Applicants) and a right set of vertices (e.g., Jobs), with unweighted edges representing which applicant is qualified for which job.
Each applicant can only take one job, and each job can only be filled by one applicant.
Find the **Maximum Bipartite Matching**: the maximum number of applicants that can be successfully paired with a job.

You must solve this by elegantly mapping the problem into a **Max Flow Network**.

**Input:** An adjacency list or matrix defining edges between the left set L and right set R.
**Output:** An integer representing the maximum number of pairings.

## When to use it

- To solve unweighted assignment and scheduling problems.
- Note: If the edges have *costs* or *weights* (e.g., Applicant A demands 50k for Job 1), Max Flow cannot solve it! You must use Min-Cost Max-Flow, or the Hungarian Algorithm (`bb_02`).

## Approach

We can completely hijack our existing `Edmonds-Karp` or `Ford-Fulkerson` code to solve this with almost zero modifications!

**The Mapping:**
1. Create a "Super Source" node S and a "Super Sink" node T.
2. Draw a directed edge from S to every vertex in the Left set (Applicants). Give these edges a capacity of exactly `1`.
3. Draw a directed edge from every vertex in the Right set (Jobs) to T. Give these edges a capacity of exactly `1`.
4. For every existing qualification edge between Applicant A and Job J, make it directed A \to J, and give it a capacity of exactly `1` (or `Infinity`, it mathematically doesn't matter because the S and T bottlenecks restrict it to 1 anyway).

**The Result:**
Because every applicant can only receive 1 unit of water from S, they can only pass 1 unit of water to a job. Because every job can only pass 1 unit of water to T, it can only receive water from 1 applicant!
Run Max Flow from S to T. The resulting flow is exactly the Maximum Bipartite Matching!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for flow_03: Bipartite Matching.

Reduce to max flow: source -> left (cap 1) -> right (cap 1) -> sink.
Max flow = max matching size.
"""


def solve(left_n, right_n, edges):
    from collections import deque
    n = left_n + right_n + 2
    source = 0
    sink = n - 1
    cap = [[0] * n for _ in range(n)]
    for u, v in edges:
        cap[1 + u][1 + left_n + v] += 1
    for u in range(left_n):
        cap[source][1 + u] += 1
    for v in range(right_n):
        cap[1 + left_n + v][sink] += 1
    flow = 0
    while True:
        parent = [-1] * n
        parent[source] = source
        q = deque([source])
        visited = [False] * n
        visited[source] = True
        while q and parent[sink] == -1:
            u = q.popleft()
            for v in range(n):
                if not visited[v] and cap[u][v] > 0:
                    visited[v] = True
                    parent[v] = u
                    q.append(v)
        if parent[sink] == -1:
            break
        path_flow = float("inf")
        v = sink
        while v != source:
            u = parent[v]
            if cap[u][v] < path_flow:
                path_flow = cap[u][v]
            v = u
        v = sink
        while v != source:
            u = parent[v]
            cap[u][v] -= path_flow
            cap[v][u] += path_flow
            v = u
        flow += path_flow
    return flow
```

</details>

## Walk-through

3 Applicants (`A0, A1, A2`). 3 Jobs (`J0, J1, J2`).
`A0` wants `J0`, `J1`.
`A1` wants `J1`.
`A2` wants `J1`.

1. **Build Network:**
   - S \to A0 (1), S \to A1 (1), S \to A2 (1).
   - J0 \to T (1), J1 \to T (1), J2 \to T (1).
   - A0 \to J0 (1), A0 \to J1 (1).
   - A1 \to J1 (1).
   - A2 \to J1 (1).
2. **Run Edmonds-Karp:**
   - BFS finds `S -> A0 -> J0 -> T`. Pushes 1.
   - BFS finds `S -> A1 -> J1 -> T`. Pushes 1.
   - Now, `A2` wants `J1`, but the pipe `J1 -> T` is fully saturated (0 residual capacity).
   - No more paths exist!
3. **Result:** Max Flow = 2. Optimal matching is (A0-J0, A1-J1). A2 gets nothing. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(V * E)$ | $O(V^2)$ |
| **Average** | $O(E * √V)$ | $O(V^2)$ |
| **Worst** | $O(V * E)$ | $O(V^2)$ |

Because every capacity is exactly 1 (a "Unit Network"), Max Flow algorithms run significantly faster than their theoretical bounds!
Edmonds-Karp on a Unit Network is mathematically guaranteed to run in $O(V \times E)$ instead of $O(V \cdot E^2)$.
Space complexity is $O(V^2)$ if using an adjacency matrix, or $O(V + E)$ if using lists.

## Variants & optimizations

- **Hopcroft-Karp Algorithm:** A highly specialized algorithm specifically designed *only* for Bipartite Matching. It behaves like Dinic's algorithm on a unit network, finding multiple augmenting paths simultaneously. It runs in an astonishing O(E \sqrt{V})$ time.

## Real-world applications

- **Dating Apps:** Finding the maximum number of mutually acceptable pairings for a speed-dating event.
- **Resource Allocation:** Assigning IP addresses from a limited DHCP pool to devices with specific subnet requests.

## Related algorithms in cOde(n)

- **[flow_02 - Edmonds-Karp](flow_02_edmonds-karp.md)** — The core engine driving this solution.
- **[approx_01 - Vertex Cover](../approximation/approx_01_vertex-cover-2-approx.md)** — By König's theorem, in any bipartite graph, the size of the Maximum Matching is exactly equal to the Minimum Vertex Cover!

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
