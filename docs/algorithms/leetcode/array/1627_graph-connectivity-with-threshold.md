# Graph Connectivity With Threshold

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1627 |
| Difficulty | Hard |
| Topics | Array, Math, Union-Find, Number Theory |
| Official Link | [graph-connectivity-with-threshold](https://leetcode.com/problems/graph-connectivity-with-threshold/) |

## Problem Description & Examples
### Goal
Answer whether pairs of nodes are connected when two nodes are connected if
they share a common divisor greater than `threshold`.

### Function Contract
**Inputs**

- `n`: nodes labeled `1` through `n`.
- `threshold`: the minimum allowed common divisor is `threshold + 1`.
- `queries`: node pairs to test.

**Return value**

A boolean answer for each query.

### Examples
**Example 1**

- Input: `n = 6, threshold = 2, queries = [[1, 4], [2, 5], [3, 6]]`
- Output: `[false, false, true]`

**Example 2**

- Input: `n = 6, threshold = 0, queries = [[4, 5], [3, 4], [3, 2], [2, 6], [1, 3]]`
- Output: `[true, true, true, true, true]`

**Example 3**

- Input: `n = 5, threshold = 1, queries = [[4, 5], [4, 2], [3, 2], [2, 5]]`
- Output: `[false, true, false, false]`

---

## Underlying Base Algorithm(s)
Use union-find. For every divisor `d > threshold`, union `d` with each multiple
of `d` up to `n`. After all unions, two queried nodes are connected exactly when
they have the same representative.

---

## Complexity Analysis
- **Time Complexity**: `O(n log n + q * alpha(n))` approximately, from processing divisor multiples and queries.
- **Space Complexity**: `O(n)`.
