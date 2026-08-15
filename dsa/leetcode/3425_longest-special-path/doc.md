# Longest Special Path

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/longest-special-path/) |
| Frontend ID | 3425 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Tree, Depth-First Search, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

An undirected weighted tree is rooted at node `0`. Its $n$ nodes are numbered from `0` through `n - 1`. Each entry `edges[i] = [u_i, v_i, length_i]` connects two nodes by an edge of the given positive length, and `nums[i]` is the value assigned to node `i`.

A special path travels downward from an ancestor to one of its descendants and contains no repeated node value. The ancestor and descendant may be the same node, so a zero-length path containing one node is always allowed. Path length is the sum of its edge lengths, not its number of nodes.

Return two integers. The first is the maximum length of any special path. The second is the minimum number of nodes among all special paths attaining that maximum length.

### Function Contract

**Inputs**

- `edges`: The $n-1$ weighted edges of a valid undirected tree; each entry has the form `[u, v, length]`.
- `nums`: The node values, where `nums[i]` belongs to node `i`.

The input satisfies $2 \le n \le 5 \cdot 10^4$, $1 \le \texttt{length} \le 10^3$, and $0 \le \texttt{nums[i]} \le 5 \cdot 10^4$.

**Return value**

Return `[maximum_length, minimum_node_count]`.

### Examples

#### Example 1

- **Input:** `edges = [[0,1,2],[1,2,3],[1,3,5],[1,4,4],[2,5,6]], nums = [2,1,2,1,3,1]`
- **Output:** `[6,2]`
- **Explanation:** Paths `2 -> 5` and `0 -> 1 -> 4` both have length `6` and unique values. The former uses only two nodes, which wins the tie-break.

#### Example 2

- **Input:** `edges = [[1,0,8]], nums = [2,2]`
- **Output:** `[0,1]`
- **Explanation:** The two-node path repeats value `2`, so only single-node paths are special.
