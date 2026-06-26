# Minimize the Difference Between Target and Chosen Elements

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1981 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Matrix |
| Official Link | [minimize-the-difference-between-target-and-chosen-elements](https://leetcode.com/problems/minimize-the-difference-between-target-and-chosen-elements/) |

## Problem Description & Examples
### Goal
Choose exactly one number from each matrix row so the resulting sum is as close as possible to `target`.

### Function Contract
**Inputs**

- `mat`: a matrix of positive integers.
- `target`: the desired sum.

**Return value**

Return the minimum absolute difference between an achievable row-choice sum and `target`.

### Examples
**Example 1**

- Input: `mat = [[1,2,3],[4,5,6],[7,8,9]], target = 13`
- Output: `0`

**Example 2**

- Input: `mat = [[1],[2],[3]], target = 100`
- Output: `94`

**Example 3**

- Input: `mat = [[1,2,9,8,7]], target = 6`
- Output: `1`

---

## Underlying Base Algorithm(s)
Keep the set of reachable sums after each row. After adding a row, optionally discard sums far above the target once a better bound is impossible. At the end, take the minimum absolute difference.

---

## Complexity Analysis
- **Time Complexity**: `O(m * S * n)` for `S` tracked sums and `n` columns.
- **Space Complexity**: `O(S)`
