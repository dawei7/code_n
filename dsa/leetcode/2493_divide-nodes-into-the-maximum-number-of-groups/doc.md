# Divide Nodes Into the Maximum Number of Groups

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2493 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Depth-First Search, Breadth-First Search, Union-Find, Graph Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/divide-nodes-into-the-maximum-number-of-groups/) |

## Problem Description

### Goal

An undirected graph has `n` nodes labeled from $1$ through $n$ and may be disconnected. Each pair `[a, b]` in `edges` gives one bidirectional edge between two distinct nodes; no pair appears more than once.

Partition every node into exactly one of $m$ groups, numbered from $1$ through $m$. Whenever an edge joins nodes in groups $x$ and $y$, their group indices must satisfy $\lvert x-y\rvert=1$. Empty gaps cannot help maximize the number of groups because removing them preserves every required difference.

Return the largest possible $m$. If no assignment can satisfy every edge, return `-1`.

### Function Contract

**Inputs**

- `n`: The number of nodes, labeled from `1` to `n`.
- `edges`: Distinct undirected edges represented as two-node arrays `[a, b]`.

The constraints satisfy $1 \le n \le 500$ and $1 \le \lvert\texttt{edges}\rvert \le 10^4$. Every endpoint lies between $1$ and $n$, and an edge never joins a node to itself.

**Return value**

Return the maximum number of groups in a valid assignment, or `-1` if no valid assignment exists.

### Examples

**Example 1**

- Input: `n = 6, edges = [[1, 2], [1, 4], [1, 5], [2, 6], [2, 3], [4, 6]]`
- Output: `4`
- Explanation: One valid ordering places node `5`, then node `1`, then nodes `2` and `4`, then nodes `3` and `6`. Every edge crosses between consecutive groups, and no fifth group can be added.

**Example 2**

- Input: `n = 3, edges = [[1, 2], [2, 3], [3, 1]]`
- Output: `-1`
- Explanation: The triangle is an odd cycle. Consecutive-group differences cannot be assigned consistently around it.
