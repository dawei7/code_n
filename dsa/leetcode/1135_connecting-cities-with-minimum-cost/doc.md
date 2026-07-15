# Connecting Cities With Minimum Cost

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1135 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Union-Find, Graph Theory, Heap (Priority Queue), Minimum Spanning Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/connecting-cities-with-minimum-cost/) |

## Problem Description

### Goal

There are `n` cities labeled from `1` through `n`. Each entry `connections[i] = [x_i, y_i, cost_i]` describes an available bidirectional connection between cities `x_i` and `y_i`, together with the cost of using that connection.

Choose available connections so that every pair of cities has at least one path between them. The total cost is the sum of the costs of all chosen connections. Return the minimum possible total cost, or return `-1` when even all available connections cannot make every city reachable from every other city.

### Function Contract

**Inputs**

- `n`: the number of cities, with $1 \le n \le 10^4$.
- `connections`: an array of $m$ available bidirectional connections, where $1 \le m \le 10^4$.
- Every connection has the form `[x_i, y_i, cost_i]`, where $1 \le x_i,y_i \le n$, $x_i \ne y_i$, and $0 \le cost_i \le 10^5$.

Let $m=\lvert\texttt{connections}\rvert$.

**Return value**

The minimum sum of chosen connection costs that connects all `n` cities, or `-1` if no such selection exists.

### Examples

**Example 1**

- Input: `n = 3, connections = [[1, 2, 5], [1, 3, 6], [2, 3, 1]]`
- Output: `6`
- Explanation: Using the connections of costs `1` and `5` reaches all three cities for the smallest possible sum.

**Example 2**

- Input: `n = 4, connections = [[1, 2, 3], [3, 4, 4]]`
- Output: `-1`
- Explanation: The two connected pairs remain separate even when every available connection is used.

### Required Complexity

- **Time:** $O(m\log m)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Recognize the structure that a minimum solution must have.** Any valid selection induces a connected undirected graph. If that selection contains a cycle, removing its most expensive edge preserves connectivity and cannot increase the total cost. Therefore an optimal selection can be a spanning tree with exactly `n - 1` useful connections; the task is to construct a minimum spanning tree or determine that none exists.

**Take safe connections in ascending cost order.** Sort `connections` by cost. Maintain the current connected components with a disjoint-set union structure. For each `[city_a, city_b, cost]`, find the representative of each endpoint. If the representatives match, the connection would create a cycle and can be skipped. Otherwise add `cost` to `total`, merge the two components, and increment `used`.

The greedy choice is safe: immediately before a chosen connection joins two components, those components define a cut of the graph, and this is a minimum-cost still-available connection crossing that cut. The cut property guarantees that some minimum spanning tree contains that choice. Repeating the argument constructs a minimum spanning tree whenever one exists. Path compression and union by size keep component operations efficient.

**Detect an impossible network.** A successful spanning tree uses exactly `n - 1` merging connections. If processing all entries leaves `used < n - 1`, at least two components have no available connection between them, so return `-1`. For `n = 1`, zero connections are needed and the minimum cost is `0`.

#### Complexity detail

Sorting the $m$ connections costs $O(m\log m)$. The disjoint-set operations contribute $O(m\alpha(n))$, where $\alpha$ is the inverse Ackermann function, and are dominated by sorting. The parent and size arrays use $O(n)$ auxiliary space; sorting storage is implementation-dependent and is not larger than $O(m)$ when the input is copied.

#### Alternatives and edge cases

- **Prim's algorithm:** Grow a tree from one city with an adjacency list and a min-heap in $O(m\log n)$ time and $O(n+m)$ space; it is equally valid but stores every connection in adjacency form.
- **Repeated component relabeling:** Kruskal can label every city by component and scan all labels after each merge, but this degrades to $O(m\log m+n^2)$ time.
- **Disconnected graph:** Fewer than `n - 1` successful merges means no selection can connect every city, even if every listed connection is considered.
- **Zero-cost connections:** Cost `0` is valid and should be selected whenever it safely joins two components.
- **Redundant or parallel connections:** A connection whose endpoints are already joined is skipped; among parallel choices, ascending processing naturally considers the cheapest first.
- **Single city:** No connection is required, so the correct minimum total is `0`.

</details>
