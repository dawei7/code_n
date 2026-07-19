# Minimum Cost to Reach City With Discounts

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2093 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Graph Theory, Heap (Priority Queue), Shortest Path |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/minimum-cost-to-reach-city-with-discounts/) |

## Problem Description

### Goal

There are $n$ cities numbered from `0` through `n - 1`. Each highway `[city1, city2, toll]` is undirected and may be traveled in either direction by paying `toll`. No pair of cities has more than one highway.

You own a limited number of single-use discounts. Applying one discount to a highway traversal changes that traversal's cost to `toll // 2`, and at most one discount may be used on a traversal. Discounts are optional. Return the minimum cost of reaching city `n - 1` from city `0`, or `-1` if no route exists.

### Function Contract

**Inputs**

- `n`: the city count, where $2 \le n \le 1000$.
- `highways`: $E$ distinct undirected edges `[city1, city2, toll]`, where $1 \le E \le 1000$.
- Each toll is between $0$ and $10^5$.
- `discounts`: the available discount count $K$, where $0 \le K \le 500$.

**Return value**

Return the minimum achievable total toll from city `0` to city `n - 1`, or `-1` when the destination is unreachable.

### Examples

**Example 1**

- Input: `n = 5`, `highways = [[0,1,4],[2,1,3],[1,4,11],[3,2,3],[3,4,2]]`, `discounts = 1`
- Output: `9`
- Explanation: Pay `4` from `0` to `1`, then discount toll `11` to `5`.

**Example 2**

- Input: `n = 4`, `highways = [[1,3,17],[1,2,7],[3,2,5],[0,1,6],[3,0,20]]`, `discounts = 20`
- Output: `8`
- Explanation: The route `0 -> 1 -> 2 -> 3` discounts its tolls to `3`, `3`, and `2`.

**Example 3**

- Input: `n = 4`, `highways = [[0,1,3],[2,3,2]]`, `discounts = 0`
- Output: `-1`

### Required Complexity

- **Time:** $O(E(K+1)\log(n(K+1)))$
- **Space:** $O((n+E)(K+1))$

<details>
<summary>Approach</summary>

#### General

**Why the city alone is not a complete state**

Arriving at the same city with different numbers of discounts already used creates different future options. Represent a state as `(city, used)`, where `used` ranges from $0$ through $K$. A highway of toll $t$ creates a same-layer transition of cost $t$ and, when `used < K`, a transition to the next layer of cost $\lfloor t/2 \rfloor$.

**Running Dijkstra on the layered graph**

Build the undirected city adjacency list and maintain the best distance for every layered state. Start from `(0, 0)` with cost zero. For the cheapest queued state, relax both the full-price and optional discounted transitions for every adjacent highway. Ignore stale heap entries whose cost no longer equals the stored best distance.

**Why the first destination state is optimal**

Every transition cost is nonnegative, including zero tolls and discounted tolls. Dijkstra's extraction order therefore finalizes states in nondecreasing cost. The first extracted state whose city is `n - 1` is cheaper than every unprocessed state, regardless of how many discounts it used, so its cost is the global optimum.

If no destination layer is reached, no sequence of highway traversals connects the endpoints and the answer is `-1`. The construction also permits leaving discounts unused because every state always retains its full-price transitions.

#### Complexity detail

There are $n(K+1)$ layered states and at most $O(E(K+1))$ directed relaxations up to a constant factor. Heap operations give $O(E(K+1)\log(n(K+1)))$ time. The graph, distance table, and heap occupy $O((n+E)(K+1))$ space.

#### Alternatives and edge cases

- **Bellman-Ford on layered states:** Repeated relaxation handles nonnegative costs correctly but can require many full edge passes and is polynomially slower.
- **One shortest path followed by discount placement:** Discounts can change which route is optimal, so optimizing a fixed undiscounted route is not sufficient.
- **City-only Dijkstra:** Keeping only one distance per city discards whether future discounted transitions remain available.
- With zero discounts, the method reduces to ordinary Dijkstra.
- Integer division makes an odd toll $t$ cost $\lfloor t/2 \rfloor$ when discounted.
- Extra discounts need not be used and cannot be stacked on one highway traversal.
- Zero-toll highways remain valid nonnegative edges.

</details>
