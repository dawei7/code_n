# Find Edges in Shortest Paths

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3123 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Depth-First Search, Breadth-First Search, Graph Theory, Heap (Priority Queue), Shortest Path |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-edges-in-shortest-paths/) |

## Problem Description

### Goal

You are given an undirected weighted graph with `n` nodes numbered from 0 through `n - 1`. Each entry `edges[i] = [a_i, b_i, w_i]` describes an undirected edge between `a_i` and `b_i` with positive weight `w_i`. Edge entries are distinct, and the graph is not guaranteed to be connected.

Consider every shortest path from node 0 to node `n - 1`. Return a boolean array `answer` in the original edge order, where `answer[i]` is `true` exactly when `edges[i]` belongs to at least one of those shortest paths. If the destination is unreachable, no edge belongs to such a path.

### Function Contract

**Inputs**

- `n`: The number of graph nodes.
- `edges`: A list of $m$ distinct undirected edges `[start, end, weight]`.

The constraints are $2 \le n \le 5\cdot 10^4$, $1 \le m \le \min(5\cdot 10^4, n(n-1)/2)$, $0 \le \texttt{start},\texttt{end}<n$, and $1 \le \texttt{weight} \le 10^5$. Every edge joins two different nodes.

**Return value**

Return $m$ booleans in input order, marking every edge that appears on at least one shortest path from node 0 to node `n - 1`.

### Examples

**Example 1**

- Input: `n = 6, edges = [[0,1,4],[0,2,1],[1,3,2],[1,4,3],[1,5,1],[2,3,1],[3,5,3],[4,5,2]]`
- Output: `[true,true,true,false,true,true,true,false]`
- Explanation: Three shortest paths have total weight 5; the marked edges are those used by at least one of them.

**Example 2**

- Input: `n = 4, edges = [[2,0,1],[0,1,1],[0,3,4],[3,2,2]]`
- Output: `[true,false,false,true]`
- Explanation: The unique shortest route is `0 -> 2 -> 3` with total weight 3.
