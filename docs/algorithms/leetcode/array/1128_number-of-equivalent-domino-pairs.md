# Number of Equivalent Domino Pairs

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1128 |
| Difficulty | Easy |
| Topics | Array, Hash Table, Counting |
| Official Link | [number-of-equivalent-domino-pairs](https://leetcode.com/problems/number-of-equivalent-domino-pairs/) |

## Problem Description & Examples
### Goal
Count pairs of dominoes that show the same two numbers, allowing the two halves of a domino to be swapped.

### Function Contract
**Inputs**

- `dominoes`: list of two-number dominoes `[a, b]`.

**Return value**

The number of index pairs `(i, j)` with `i < j` whose dominoes are equivalent.

### Examples
**Example 1**

- Input: `dominoes = [[1,2],[2,1],[3,4],[5,6]]`
- Output: `1`

**Example 2**

- Input: `dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]`
- Output: `3`

**Example 3**

- Input: `dominoes = [[2,2],[2,2],[2,2]]`
- Output: `3`

---

## Underlying Base Algorithm(s)
Canonical key normalization and frequency counting.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)` for the fixed domino value range, or `O(k)` for `k` distinct normalized dominoes.
