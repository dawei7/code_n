# Travelling Salesperson (Held-Karp DP)

| | |
|---|---|
| **ID** | `graph_20` |
| **Category** | graphs |
| **Complexity (required)** | $O(V^2 * 2^V)$ Time, $O(V * 2^V)$ Space |
| **Difficulty** | 10/10 |
| **Interview relevance** | 2/10 |
| **Wikipedia** | [Held-Karp algorithm](https://en.wikipedia.org/wiki/Held%E2%80%93Karp_algorithm) |

## Problem statement

Given a complete weighted graph (where every node is connected to every other node). Find the absolute shortest possible route that visits every vertex exactly once, and returns to the starting vertex.
This is the legendary Travelling Salesperson Problem (TSP).

**Input:** Number of vertices `V`, and a 2D adjacency matrix `matrix`.
**Output:** An integer representing the minimum cost of the tour.

## When to use it

- To solve TSP exactly for small graphs (V \le 20).
- *Note:* Pure permutation brute-force checks $O(V!)$ paths. 20! is 2.4 x 10^{18} (impossible). Held-Karp's $O(V^2 2^V)$ reduces this to 20^2 x 2^{20} ~= 4 x 10^8 operations, which takes less than a second!

## Approach

**1. The Overlapping Subproblems (Why DP works):**
Imagine V=5. We start at node 0.
Path A: 0 \rightarrow 1 \rightarrow 2 \rightarrow 3.
Path B: 0 \rightarrow 2 \rightarrow 1 \rightarrow 3.
Notice that both paths are currently sitting at node `3`, and both paths have visited the exact same set of cities `{0, 1, 2, 3}`!
To finish the tour, both paths need to visit node `4` and return to `0`. The *future optimal choices* from node `3` are completely identical! We should only calculate the optimal completion path from (Node `3`, Set `{0,1,2,3}`) ONCE, and cache the result!

**2. Bitmasking the Set:**
We represent the "Set of visited cities" as an integer Bitmask.
If we visited cities 0, 1, and 3, the bitmask is `1011` (binary for 11).
Our DP state is `dp(mask, curr_node)`.
This represents: "What is the minimum cost to visit all REMAINING unvisited nodes in the graph, starting from `curr_node`, given that we have already visited the nodes in `mask`?"

**3. The Recurrence Relation:**
From `curr_node`, we can try jumping to any `next_node` that is NOT currently activated in the `mask`.
The cost of that choice is:
`weight(curr_node, next_node) + dp( mask | (1 << next_node), next_node )`
We take the absolute minimum across all valid choices for `next_node`.

**4. The Base Case:**
When all bits in `mask` are 1 (`mask == (1 << V) - 1`), it means we have visited every single city exactly once.
The only thing left to do is return to the starting node (Node 0).
Return `matrix[curr_node][0]`.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for graph_20: Travelling Salesman (Held-Karp DP).

dp[mask][i] = min cost to start at 0, visit exactly the
cities in ``mask``, and end at city i. Recurrence:
dp[mask][i] = min over j in mask of dp[mask ^ (1<<i)][j] + dist[j][i].
Final answer: min over i of dp[all][i] + dist[i][0].
"""


def solve(dist, n):
    if n <= 1:
        return 0
    INF = float("inf")
    dp = [[INF] * n for _ in range(1 << n)]
    dp[1][0] = 0
    for mask in range(1, 1 << n):
        if not (mask & 1):
            continue
        for i in range(n):
            if not (mask & (1 << i)) or dp[mask][i] == INF:
                continue
            for j in range(n):
                if mask & (1 << j):
                    continue
                new_mask = mask | (1 << j)
                new_cost = dp[mask][i] + dist[i][j]
                if new_cost < dp[new_mask][j]:
                    dp[new_mask][j] = new_cost
    full = (1 << n) - 1
    best = INF
    for i in range(n):
        if dp[full][i] < INF:
            cycle = dp[full][i] + dist[i][0]
            if cycle < best:
                best = cycle
    return best
```

</details>

## Walk-through

`V = 3`. Starting at node 0. `VISITED_ALL = 7` (binary `111`).
`dp(1, 0)`: (Mask `001`, Curr `0`)
  - Try next `1`. Cost = `matrix[0][1] + dp(3, 1)`. (Mask `011`)
  - Try next `2`. Cost = `matrix[0][2] + dp(5, 2)`. (Mask `101`)

Evaluate `dp(3, 1)`: (Mask `011`, Curr `1`)
  - Try next `2`. Cost = `matrix[1][2] + dp(7, 2)`. (Mask `111`)

Evaluate `dp(7, 2)`: (Mask `111` == VISITED_ALL)
  - Base case! Return `matrix[2][0]`.

Path `0 -> 1 -> 2 -> 0` cost resolves.
The tree evaluates all paths, memoizing identical sub-paths (though with V=3 there is no overlap yet, overlaps only occur V \ge 4).
Return the minimum. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(V^2 * 2^V)$ | $O(V * 2^V)$ |
| **Average** | $O(V^2 * 2^V)$ | $O(V * 2^V)$ |
| **Worst** | $O(V^2 * 2^V)$ | $O(V * 2^V)$ |

How many unique states are in the memo table? The `mask` can be any value from 0 to 2^V - 1, and `curr` can be any node from 0 to V - 1. Total states = V \cdot 2^V.
Inside the `dp()` function, computing a state takes $O(V)$ time because of the `for nxt in range(V)` loop.
Therefore, total time is (V \cdot 2^V) \cdot V = $O(V^2 2^V)$.
Space complexity is $O(V \cdot 2^V)$ to store the `memo` table.
While exponential, it is a colossal improvement over the $O(V!)$ brute force logic.

## Variants & optimizations

- **Christofides Algorithm (Approximation):** For metric graphs (where the triangle inequality holds), Christofides mathematically guarantees finding a route that is AT MOST 1.5x longer than the true optimal route, and does so in $O(V^3)$ polynomial time! (It relies on finding an MST, then finding a Minimum Weight Perfect Matching on the odd-degree nodes).
- **Genetic Algorithms / Simulated Annealing:** For massive instances (V = 100,000), AI meta-heuristics are used to quickly find "good enough" routes, since both V! and 2^V are physically impossible to compute.

## Real-world applications

- **Logistics & Delivery (FedEx/UPS):** Daily route planning for delivery trucks dropping off 15-20 packages.
- **PCB Manufacturing:** Optimizing the path of the robotic laser drill that must punch hundreds of holes in a motherboard.

## Related algorithms in cOde(n)

- **[dp_03 - Top-Down Memoization](../dynamic/dp_03_top-down-memoization.md)** — The foundation of the exact technique used here.
- **[bit_01 - Check if i-th bit is set](../bit_manipulation/bit_01_check-if-i-th-bit-is-set.md)** — The bitwise arithmetic used to flip bits in the `mask`.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
