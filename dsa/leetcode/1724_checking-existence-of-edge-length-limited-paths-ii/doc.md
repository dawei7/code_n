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
