# Maximum Building Height

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/maximum-building-height/) |
| Frontend ID | 1840 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

Construct $n$ buildings in a line, labeled from 1 through $n$, with non-negative integer heights. Building 1 must have height 0, and the heights of two adjacent buildings may differ by at most 1.

Some unique building IDs have additional upper bounds, supplied as `[id, maxHeight]`; building 1 never appears in that list. Choose heights satisfying every rule and return the greatest possible height of the tallest building anywhere in the line.

### Function Contract

**Inputs**

- `n`: the number of buildings, where $2 \le n \le 10^9$.
- `restrictions`: $r$ distinct pairs `[id, maxHeight]`, where $0 \le r \le \min(n-1,10^5)$.
- Every restricted ID is between 2 and $n$, and every maximum height is between 0 and $10^9$.

**Return value**

- Return the maximum height achievable by any building while all endpoint, adjacency, non-negativity, and explicit upper-bound rules hold.

### Examples

**Example 1**

- Input: `n = 5, restrictions = [[2,1],[4,1]]`
- Output: `2`

Heights `[0,1,2,1,2]` satisfy all rules.

**Example 2**

- Input: `n = 6, restrictions = []`
- Output: `5`

Without explicit caps, heights may rise from 0 by one at every building.

**Example 3**

- Input: `n = 10, restrictions = [[5,3],[2,5],[7,4],[10,3]]`
- Output: `5`

One optimal profile is `[0,1,2,3,3,4,4,5,4,3]`.
