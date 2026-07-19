# Critical Connections in a Network

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1192 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Depth-First Search, Graph Theory, Biconnected Component |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/critical-connections-in-a-network/) |

## Problem Description

### Goal

A network contains `n` servers numbered from `0` through `n - 1`. Each entry `connections[i] = [a_i,b_i]` represents an undirected server-to-server connection between its two endpoints. The network is initially connected, so every server can reach every other server through some direct or indirect route.

A critical connection is an edge whose removal makes at least one server unable to reach another server. Return every critical connection in any order. Either endpoint order is accepted for an edge because each connection is undirected.

### Function Contract

**Inputs**

- `n`: The number of servers, where $2\le n\le10^5$.
- `connections`: A list of $m$ distinct undirected edges, where $n-1\le m\le10^5$. Each edge has endpoints `a_i` and `b_i` satisfying $0\le a_i,b_i<n$ and $a_i\ne b_i$.

**Return value**

- All edges whose individual removal disconnects the network, in any list order and with either endpoint order.

### Examples

**Example 1**

- Input: `n = 4`, `connections = [[0,1],[1,2],[2,0],[1,3]]`
- Output: `[[1,3]]`

The first three servers lie on a cycle, while server `3` has no alternate route.

**Example 2**

- Input: `n = 2`, `connections = [[0,1]]`
- Output: `[[0,1]]`

The network's only edge is necessarily critical.
