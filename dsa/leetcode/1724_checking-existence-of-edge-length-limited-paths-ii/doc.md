# Checking Existence of Edge Length Limited Paths II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1724 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Depth-First Search, Union-Find, Graph Theory, Design, Sorting, Heap (Priority Queue), Minimum Spanning Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths-ii/) |

## Problem Description

### Goal

Implement `DistanceLimitedPathsExist` for an undirected weighted graph with nodes labeled from $0$ through $n-1$. Each entry `[u, v, distance]` in `edgeList` adds an edge of that weight; parallel edges may occur, and the graph need not be connected.

After construction, `query(p, q, limit)` must report whether some path connects `p` and `q` using only edges whose individual weights are strictly less than `limit`. Queries arrive online and do not modify the graph.

### Function Contract

**Inputs**

- Construction receives `n`, where $2 \le n \le 10^4$, and `edgeList`, containing at most $10^4$ entries `[u, v, distance]`.
- Every endpoint satisfies $0 \le u,v<n$ with $u \ne v$, and $1 \le \texttt{distance} \le 10^9$.
- Each `query(p, q, limit)` uses distinct valid nodes and $1 \le \texttt{limit} \le 10^9$.
- Let $m = \lvert\texttt{edgeList}\rvert$ and let $q$ be the number of queries, with $q \le 10^4$.

**Return value**

- Construction returns no value. Each query returns `true` exactly when an eligible path exists, and otherwise returns `false`.

### Examples

**Example 1**

- Input: `operations = ["DistanceLimitedPathsExist","query","query","query","query"]`, `arguments = [[6,[[0,2,4],[0,3,2],[1,2,3],[2,3,1],[4,5,5]]],[2,3,2],[1,3,3],[2,0,3],[0,5,6]]`
- Output: `[null,true,false,true,false]`
- Explanation: The edge from $2$ to $3$ has weight $1$; the path $2\to3\to0$ uses weights below $3$; node $5$ lies in another component.

**Example 2**

- Input: graph edges `[[0,1,10],[0,1,3]]`, then queries `(0,1,3)` and `(0,1,4)`
- Output: `[null,false,true]`
- Explanation: The comparison is strict, while the parallel edge of weight $3$ becomes eligible once the limit is $4$.

**Example 3**

- Input: graph edges `[[0,2,10],[0,1,4],[1,2,5]]`, then queries `(0,2,6)` and `(0,2,5)`
- Output: `[null,true,false]`
- Explanation: The indirect path has bottleneck weight $5$, which is below $6$ but not below $5$.

### Required Complexity

- **Time:** $O(m\log m+n\log n+q\log n)$
- **Space:** $O(n\log n)$

<details>
<summary>Approach</summary>

#### General

**Preserve every minimum-bottleneck connection**

Sort edges by weight and run Kruskal's algorithm. Whenever an edge joins two previously separate components, add it to a minimum spanning forest. For any connected pair of nodes, the unique forest path minimizes the largest edge weight among all original-graph paths. Therefore a query is true exactly when the maximum forest edge on its path is below `limit`.

**Root each tree and record binary ancestors**

Traverse every tree in the forest to record each node's depth, immediate parent, and parent-edge weight. Build binary-lifting tables: at level $j$, store the $2^j$th ancestor and the maximum edge on that upward segment. Disjoint-set representatives retained from Kruskal identify pairs that have no path at any limit.

**Lift endpoints while accumulating the bottleneck**

For a query in one component, first lift the deeper endpoint to equal depth, updating the largest encountered weight. Then lift both endpoints from the highest binary level downward whenever their ancestors differ. Finally include the two edges to their lowest common ancestor. The collected maximum is the minimum possible path bottleneck, so return whether it is strictly less than `limit`.

#### Complexity detail

Sorting $m$ edges takes $O(m\log m)$. Kruskal processing is $O(m\alpha(n))$; forest traversal and construction of $\lceil\log_2 n\rceil$ ancestor levels take $O(n\log n)$. Each of the $q$ queries examines $O(\log n)$ levels. The total time is $O(m\log m+n\log n+q\log n)$ and the forest plus lifting tables use $O(n\log n)$ space.

#### Alternatives and edge cases

- **Kruskal reconstruction tree:** Create a merge node for every successful union; the weight at the lowest common ancestor of two original nodes is their minimum bottleneck, with the same logarithmic-query strategy.
- **Threshold BFS per query:** Traverse only edges below the requested limit. This is correct but can take $O(q(n+m))$ total time.
- **Persistent union-find:** Record component history by edge weight and answer each threshold query from the appropriate version, at the cost of a more specialized data structure.
- **Strict threshold:** An edge whose weight equals `limit` is forbidden.
- **Disconnected nodes:** Different minimum-spanning-forest components always return `false`.
- **Parallel edges:** Kruskal naturally keeps only an edge that improves connectivity; heavier duplicates cannot improve a bottleneck.
- **Cycles:** Edges closing a component cycle are unnecessary for every minimum-bottleneck path.

</details>
