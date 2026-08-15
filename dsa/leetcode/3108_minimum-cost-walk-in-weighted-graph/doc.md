# Minimum Cost Walk in Weighted Graph

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3108 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Bit Manipulation, Union-Find, Graph Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [minimum-cost-walk-in-weighted-graph](https://leetcode.com/problems/minimum-cost-walk-in-weighted-graph/) |

## Problem Description

### Goal

An undirected weighted graph has `n` vertices labeled from $0$ through $n-1$. Each entry `edges[i] = [u_i, v_i, w_i]` represents an edge of weight $w_i$ joining the distinct vertices $u_i$ and $v_i$.

A walk is an alternating sequence of vertices and connecting edges. It may revisit a vertex or traverse an edge more than once. If a walk encounters edge weights $w_0,w_1,\ldots,w_r$, its cost is their bitwise AND,

$$
w_0 \mathbin{\&} w_1 \mathbin{\&} \cdots \mathbin{\&} w_r.
$$

For every entry `query[i] = [s_i, t_i]`, find the minimum possible cost of a walk that begins at $s_i$ and ends at the distinct vertex $t_i$. If no such walk exists, the answer for that query is $-1$. Return all query answers in their original order.

### Function Contract

Let $m$ be the number of edges and $q$ be the number of queries.

**Inputs**

- `n`: The number of vertices, where $2 \le n \le 10^5$.
- `edges`: A list of $m$ triples `[u, v, w]`, where $0 \le m \le 10^5$, $0 \le u,v<n$, $u \ne v$, and $0 \le w \le 10^5$. Parallel edges are permitted.
- `query`: A list of $q$ pairs `[s, t]`, where $1 \le q \le 10^5$, $0 \le s,t<n$, and $s \ne t$.

**Return value**

- A length-$q$ list whose $i$th value is the minimum walk cost from `query[i][0]` to `query[i][1]`, or $-1$ if those vertices are disconnected.

### Examples

#### Example 1

- **Input:** `n = 5, edges = [[0,1,7],[1,3,7],[1,2,1]], query = [[0,3],[3,4]]`
- **Output:** `[1, -1]`
- **Explanation:** A walk from $0$ to $3$ can detour through the weight-$1$ edge and traverse it again, giving cost $7 \mathbin{\&} 1 \mathbin{\&} 1 \mathbin{\&} 7=1$. Vertex $4$ is disconnected from vertex $3$.

#### Example 2

- **Input:** `n = 3, edges = [[0,2,7],[0,1,15],[1,2,6],[1,2,1]], query = [[1,2]]`
- **Output:** `[0]`
- **Explanation:** The parallel edges of weights $6$ and $1$ may both appear in a walk, reducing its cost to $0$.
