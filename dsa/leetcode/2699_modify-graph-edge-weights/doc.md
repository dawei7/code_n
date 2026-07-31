# Modify Graph Edge Weights

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2699 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Graph Theory, Heap (Priority Queue), Shortest Path |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/modify-graph-edge-weights/) |

## Problem Description

### Goal

An undirected, weighted, connected graph has `n` vertices numbered from $0$ through $n-1$. Each row `[u, v, w]` in `edges` describes one edge. A positive `w` is fixed and cannot be changed; a weight of `-1` is unknown.

Assign every unknown edge a positive integer weight from $1$ through $2 \cdot 10^9$ so that the shortest-path distance from `source` to `destination` is exactly `target`. Different unknown edges may receive different values, and any complete assignment satisfying the distance requirement is acceptable.

Return all graph edges, including the originally fixed ones, in any order after a valid assignment. If no assignment can make the shortest distance exactly `target`, return an empty list.

### Function Contract

Let $m = \lvert\texttt{edges}\rvert$.

**Inputs**

- `n`: The number of vertices, with $1 \leq n \leq 100$.
- `edges`: Between $1$ and $n(n-1)/2$ rows `[u, v, w]`. Endpoints are distinct valid vertices, no undirected edge is repeated, and each weight is either `-1` or from $1$ through $10^7$.
- `source`: The starting vertex.
- `destination`: A vertex distinct from `source`.
- `target`: The required shortest-path distance, with $1 \leq \texttt{target} \leq 10^9$.

The input graph is connected.

**Return value**

Return a complete legal edge assignment whose shortest `source`-to-`destination` distance equals `target`, or `[]` when no such assignment exists. Originally positive weights must be unchanged.

### Examples

**Example 1**

- Input: `n = 5`, `edges = [[4,1,-1],[2,0,-1],[0,3,-1],[4,3,-1]]`, `source = 0`, `destination = 1`, `target = 5`
- Output: `[[4,1,1],[2,0,1],[0,3,3],[4,3,1]]`
- Explanation: This is one valid assignment whose shortest distance from $0$ to $1$ is $5$.

**Example 2**

- Input: `n = 3`, `edges = [[0,1,-1],[0,2,5]]`, `source = 0`, `destination = 2`, `target = 6`
- Output: `[]`
- Explanation: The fixed edge of weight $5$ is already a shorter route and cannot be increased.

**Example 3**

- Input: `n = 4`, `edges = [[1,0,4],[1,2,3],[2,3,5],[0,3,-1]]`, `source = 0`, `destination = 2`, `target = 6`
- Output: `[[1,0,4],[1,2,3],[2,3,5],[0,3,1]]`
- Explanation: Assigning the direct unknown edge weight $1$ makes the shortest distance equal $6$.
