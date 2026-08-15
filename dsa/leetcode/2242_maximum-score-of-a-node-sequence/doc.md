# Maximum Score of a Node Sequence

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2242 |
| Difficulty | Hard |
| Topics | Array, Graph, Sorting, Heap (Priority Queue) |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-score-of-a-node-sequence/) |

## Problem Description

### Goal

An undirected graph has $n$ nodes numbered from $0$ through $n-1$. Node $i$
has value `scores[i]`, and every pair in `edges` identifies one undirected
connection. The graph has no self-loops or duplicate edges.

A valid node sequence contains exactly four distinct nodes. Each consecutive
pair in the sequence must share an edge, so the four nodes form a simple path
of three edges, although other edges among them are allowed. Its score is the
sum of its four node values. Return the greatest score among all valid
four-node sequences, or `-1` when no such sequence exists.

### Function Contract

**Inputs**

- `scores`: An array of $n$ positive node scores, where $4\le n\le 5\cdot 10^4$ and $1\le\texttt{scores[i]}\le 10^8$.
- `edges`: At most $5\cdot 10^4$ distinct pairs `[a, b]` with $0\le a,b<n$ and $a\ne b$.

**Return value**

Return the maximum sum of four distinct nodes `[a, b, c, d]` for which
`[a, b]`, `[b, c]`, and `[c, d]` are graph edges. Return `-1` if no such
sequence exists.

### Examples

#### Example 1

- **Input:** `scores = [5,2,9,8,4], edges = [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]`
- **Output:** `24`

#### Example 2

- **Input:** `scores = [9,20,6,4,11,12], edges = [[0,3],[5,3],[2,4],[1,3]]`
- **Output:** `-1`

#### Example 3

- **Input:** `scores = [1,2,3,4], edges = [[0,1],[1,2],[2,3]]`
- **Output:** `10`
