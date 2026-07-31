# Number of Ways to Assign Edge Weights I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3558 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Tree, Depth-First Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-i/) |

## Problem Description

### Goal

An undirected tree has nodes labeled from `1` through `n` and is rooted at node `1`. It is described by `n - 1` edges. Every edge initially has weight zero, but an edge on the relevant path may instead be assigned weight `1` or `2`.

Choose any node `x` having maximum depth. Consider only the unique path from root `1` to `x`; edges outside that path are ignored. Count the assignments of weights `1` and `2` to the path edges for which their total weight is odd. Every maximum-depth node produces a path of the same length, so the choice of `x` does not change the count.

Return the count modulo $10^9+7$.

### Function Contract

**Inputs**

- `edges`: The `n - 1` undirected edges `[u, v]` of a valid tree on nodes `1` through `n`.

The constraints are $2 \le n \le 10^5$, `edges.length == n - 1`, and every endpoint lies from `1` through `n`.

**Return value**

Return, modulo $10^9+7$, the number of assignments of weights `1` and `2` to the root-to-deepest-node path whose sum is odd.

### Examples

**Example 1**

- Input: `edges = [[1,2]]`
- Output: `1`
- Explanation: Weight `1` gives the only odd path cost; weight `2` gives an even cost.

**Example 2**

- Input: `edges = [[1,2],[1,3],[3,4],[3,5]]`
- Output: `2`
- Explanation: A deepest path has two edges. Assignments `(1,2)` and `(2,1)` have odd total cost.

---
