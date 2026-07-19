# Most Stones Removed with Same Row or Column

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 947 |
| Difficulty | Medium |
| Topics | Hash Table, Depth-First Search, Union-Find, Graph Theory |
| Official Link | [LeetCode](https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/) |

## Problem Description

### Goal

There are $n$ stones at distinct integer coordinate points on a two-dimensional plane. A stone may be removed only when at least one other stone that has not yet been removed lies in the same row or in the same column.

Given every stone position as `[x, y]`, choose a legal removal order that deletes as many stones as possible. Return that maximum number; stones that no longer share a row or column with any remaining stone must stay on the plane.

### Function Contract

Let $n$ be the number of stones, and let $\alpha(n)$ denote the inverse Ackermann factor for disjoint-set operations.

**Inputs**

- `stones`: a list of $n$ distinct coordinate pairs with $1 \le n \le 1000$.
- Each pair `[x, y]` satisfies $0 \le x,y \le 10^4$, and no coordinate point appears twice.

**Return value**

Return the largest number of stones that can be removed under the same-row-or-same-column rule.

### Examples

**Example 1**

- Input: `stones = [[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]`
- Output: `5`

All six stones belong to one row-or-column connected component, so one stone must remain and five can be removed.

**Example 2**

- Input: `stones = [[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]`
- Output: `3`

The isolated stone `[1, 1]` forms one component and the other four stones form another, leaving two stones in total.

**Example 3**

- Input: `stones = [[0, 0]]`
- Output: `0`
