# Longest Special Path II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3486 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Tree, Depth-First Search, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/longest-special-path-ii/) |

## Problem Description

### Goal

An undirected weighted tree is rooted at node 0. Its $n$ nodes are numbered from 0 through $n-1$, and `nums[i]` is the value attached to node `i`. Each edge `[u, v, length]` connects two nodes and contributes its positive `length` to any path that uses it.

A special path must travel downward from an ancestor to one of its descendants. Along that path, every node value must be distinct except that at most one value may occur twice. No value may occur three times, and two different values may not both be duplicated.

The length of a path is the sum of its edge lengths. Find the maximum possible length of a special path. Among every special path with that maximum length, also find the minimum number of nodes.

### Function Contract

**Inputs**

- `edges`: The $n-1$ weighted undirected edges, each represented as `[u, v, length]`.
- `nums`: The node-value array, where `nums[i]` belongs to node `i`.

The tree is rooted at node 0. The constraints are $2\le n\le5\cdot10^4$, $1\le\texttt{length}\le10^3$, and $0\le\texttt{nums[i]}\le5\cdot10^4$.

**Return value**

Return `[maximum_length, minimum_nodes]`. The first component is the greatest edge-length sum of any downward special path; the second is the fewest nodes among paths attaining that length.

### Examples

#### Example 1

- **Input:** `edges = [[0,1,1],[1,2,3],[1,3,1],[2,4,6],[4,7,2],[3,5,2],[3,6,5],[6,8,3]]`, `nums = [1,1,0,3,1,2,1,1,0]`
- **Output:** `[9, 3]`

Paths `1 -> 2 -> 4` and `1 -> 3 -> 6 -> 8` both have length 9. The former uses only three nodes, so the tie-breaking component is 3.

#### Example 2

- **Input:** `edges = [[1,0,3],[0,2,4],[0,3,5]]`, `nums = [1,1,0,2]`
- **Output:** `[5, 2]`

The downward edge `0 -> 3` is the longest special path.

#### Example 3

- **Input:** `edges = [[0,1,2],[1,2,3],[2,3,4]]`, `nums = [1,2,1,3]`
- **Output:** `[9, 4]`

The complete root-to-node-3 path is legal because only value 1 is repeated, and it occurs exactly twice.
