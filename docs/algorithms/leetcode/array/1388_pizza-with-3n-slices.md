# Pizza With 3n Slices

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1388 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming, Greedy, Heap (Priority Queue) |
| Official Link | [pizza-with-3n-slices](https://leetcode.com/problems/pizza-with-3n-slices/) |

## Problem Description & Examples
### Goal
A circular pizza is split into `3n` slices. Repeatedly choose one slice for yourself while the adjacent slices are taken by others, so you end up with `n` non-adjacent slices. Maximize the total size you take.

### Function Contract
**Inputs**

- `slices`: a circular list of slice sizes with length divisible by `3`.

**Return value**

The maximum total size obtainable by choosing exactly `len(slices) / 3` non-adjacent slices.

### Examples
**Example 1**

- Input: `slices = [1,2,3,4,5,6]`
- Output: `10`

**Example 2**

- Input: `slices = [8,9,8,6,1,1]`
- Output: `16`

**Example 3**

- Input: `slices = [4,1,2,5,8,3]`
- Output: `12`

---

## Underlying Base Algorithm(s)
Circular non-adjacent selection DP. Break the circle into two linear cases: exclude the first slice or exclude the last slice. For each case, use dynamic programming over index and count chosen.

---

## Complexity Analysis
- **Time Complexity**: `O(n^2)` for `3n` slices and choosing `n` of them.
- **Space Complexity**: `O(n^2)`, reducible with rolling rows.
